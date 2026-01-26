"""Minimal Flame listener prototype

This is a small JSON-over-TCP listener intended to run inside Flame's Python
startup hook. It accepts messages like {"command":"execute","id":"...","code":"..."}
and returns a JSON response with stdout/stderr/exception.

Notes:
- When running inside Flame, prefer scheduling execution on the main thread
  using `flame.execute_on_main_thread()` where available.
- For development, this script can run outside Flame and will execute the
  provided code in a subprocess/thread (but that won't exercise Flame APIs).
"""

import json
import socket
import threading
import traceback
import sys
import io
import atexit
import time
import os
from datetime import datetime

# Track background threads so we can clean up on exit (per Flame docs about threading hooks)
threads = []


def wait_for_threads_at_exit():
    global threads
    if len(threads) > 0:
        for thread in threads:
            try:
                print(f"[flame_listener] Waiting for thread {thread.name}")
                thread.join(timeout=5.0)
            except Exception:
                traceback.print_exc()
    threads = []

# Register cleanup at process exit
atexit.register(wait_for_threads_at_exit)


# Global exception hooks to ensure background thread exceptions and unhandled exceptions
# are visible in Flame logs (helpful for diagnosing crashes and timeouts)
def _thread_excepthook(args):
    try:
        _log(f"thread-exc thread={getattr(args, 'thread', None)}")
        tb = ''.join(traceback.format_exception(args.exc_type, args.exc_value, args.exc_traceback))
        for line in tb.splitlines():
            _log(line)
    except Exception:
        traceback.print_exc()

# Python 3.8+ supports threading.excepthook
try:
    threading.excepthook = _thread_excepthook
except Exception:
    # older Pythons: best-effort only
    pass


def _sys_excepthook(exc_type, exc_value, exc_tb):
    try:
        print("[flame_listener][unhandled-exc]")
        traceback.print_exception(exc_type, exc_value, exc_tb)
    except Exception:
        traceback.print_exc()

sys.excepthook = _sys_excepthook


LOG_FILE = os.environ.get('FLAME_LISTENER_LOG', '/tmp/flame_listener.log')

def _log(msg):
    """Simple structured log with timestamp. Also append to a local log file to aid repro collection."""
    line = f"[flame_listener][{datetime.utcnow().isoformat()}] {msg}"
    try:
        print(line)
    except Exception:
        pass
    try:
        with open(LOG_FILE, 'a') as fh:
            fh.write(line + '\n')
    except Exception:
        # best-effort: don't fail the listener if logging to file fails
        pass


HOST = '127.0.0.1'
PORT = 5555

# Authentication token used to validate incoming requests. Default lookup order:
# 1) FLAME_TOKEN environment variable
# 2) .flame.secrets.json file (token field) in the same directory as the script
# If no token is found, the server will run without token validation (not recommended).
import os
import json

AUTH_TOKEN = None
env_token = os.environ.get('FLAME_TOKEN')
if env_token:
    AUTH_TOKEN = env_token
else:
    # Try to load .flame.secrets.json from the current directory
    try:
        here = os.path.dirname(__file__)
        secrets_path = os.path.join(here, '.flame.secrets.json')
        with open(secrets_path, 'r') as sf:
            data = json.load(sf)
            AUTH_TOKEN = data.get('token')
    except Exception:
        AUTH_TOKEN = None

try:
    import flame  # type: ignore
    HAS_FLAME = True
except Exception:
    HAS_FLAME = False


def handle_execute(code, timeout=5.0):
    """Execute `code` and capture stdout/stderr and exceptions.

    Execution is done in a thread to allow timeouts to be enforced. When running
    inside Flame we prefer scheduling on the main thread (if available) but still
    implement a timeout watchdog.
    """
    result = {'out': '', 'err': '', 'exc': None}
    finished = threading.Event()

    def _run_exec():
        buf_out = io.StringIO()
        buf_err = io.StringIO()
        try:
            # Redirect stdout/stderr locally while executing
            import contextlib
            with contextlib.redirect_stdout(buf_out), contextlib.redirect_stderr(buf_err):
                exec(code, globals(), locals())
        except Exception:
            buf_err.write(traceback.format_exc())
        result['out'] = buf_out.getvalue()
        result['err'] = buf_err.getvalue()
        finished.set()

    try:
        # If Flame is present and has a main-thread executor, attempt to use it but
        # still run the actual execution in a thread so we can enforce timeout from here.
        exec_thread = threading.Thread(target=_run_exec, name=f"exec-{time.time()}", daemon=True)
        threads.append(exec_thread)
        exec_thread.start()

        # Wait for the execution to finish up to timeout seconds
        completed = finished.wait(timeout)
        if not completed:
            # timeout: attempt to provide a helpful error message; we cannot safely kill
            # the thread, so the code may still be running in background and we report a timeout.
            result['err'] = (result.get('err') or '') + f"\nError: execution timed out after {timeout} seconds."
            result['exc'] = 'TimeoutError'
        return result['out'], result['err'], result['exc']
    except Exception as e:
        tb = traceback.format_exc()
        return result['out'], result['err'] + tb, str(e)


class ClientHandler(threading.Thread):
    def __init__(self, conn, addr):
        super().__init__(daemon=True)
        self.conn = conn
        self.addr = addr

    def run(self):
        try:
            with self.conn:
                # Ensure we don't block forever on recv from a misbehaving client
                try:
                    recv_timeout = float(os.environ.get('FLAME_LISTENER_RECV_TIMEOUT', '5.0'))
                    self.conn.settimeout(recv_timeout)
                except Exception:
                    pass

                data = b""
                while True:
                    try:
                        chunk = self.conn.recv(4096)
                    except socket.timeout:
                        _log(f"recv timeout from {self.addr}")
                        break
                    except Exception:
                        traceback.print_exc()
                        break

                    if not chunk:
                        break
                    data += chunk
                    try:
                        payload = json.loads(data.decode('utf-8'))
                    except json.JSONDecodeError:
                        # Wait for more data
                        continue

                    # Simple auth
                    if AUTH_TOKEN and payload.get('token') != AUTH_TOKEN:
                        resp = {'id': payload.get('id'), 'stdout': '', 'stderr': 'authentication failed', 'exception': 'AuthError'}
                        try:
                            self.conn.sendall((json.dumps(resp) + '\n').encode('utf-8'))
                        except Exception:
                            traceback.print_exc()
                        data = b""
                        continue

                    cmd = payload.get('command')
                    if cmd == 'execute':
                        code = payload.get('code', '')
                        # Allow the client to specify a timeout per request (seconds)
                        timeout = float(payload.get('timeout', 5.0))
                        req_id = payload.get('id')
                        _log(f"execute request id={req_id} from {self.addr} timeout={timeout}")
                        start_ts = time.time()
                        out, err, exc = handle_execute(code, timeout=timeout)
                        elapsed = time.time() - start_ts
                        _log(f"execute complete id={req_id} elapsed={elapsed:.3f}s exc={exc}")
                        resp = {'id': req_id, 'stdout': out or '', 'stderr': err or '', 'exception': exc}
                        try:
                            self.conn.sendall((json.dumps(resp) + '\n').encode('utf-8'))
                        except Exception:
                            traceback.print_exc()
                    elif cmd == 'ping':
                        resp = {'id': payload.get('id'), 'stdout': 'pong', 'stderr': '', 'exception': None}
                        try:
                            self.conn.sendall((json.dumps(resp) + '\n').encode('utf-8'))
                        except Exception:
                            traceback.print_exc()
                    elif cmd == 'start_debug_server':
                        port = payload.get('port', 5678)
                        resp = {'id': payload.get('id'), 'stdout': f'Starting debug server on 127.0.0.1:{port} (background)', 'stderr': '', 'exception': None}
                        try:
                            self.conn.sendall((json.dumps(resp) + '\n').encode('utf-8'))
                        except Exception:
                            traceback.print_exc()

                        def _start_debug():
                            try:
                                import debugpy  # type: ignore
                                ep = debugpy.listen(('127.0.0.1', port), in_process_debug_adapter=True)
                                _log(f"debug adapter listening: {ep}")
                                try:
                                    debugpy.wait_for_client(timeout=30)
                                    _log(f"debug client attached on {port}")
                                except Exception:
                                    _log(f"debug client did not attach within timeout {port}")
                            except Exception:
                                traceback.print_exc()

                        try:
                            t = threading.Thread(target=_start_debug, name=f"debug-start-{time.time()}", daemon=True)
                            threads.append(t)
                            t.start()
                        except Exception:
                            traceback.print_exc()
                    else:
                        resp = {'id': payload.get('id'), 'stdout': '', 'stderr': 'unknown command', 'exception': 'CommandError'}
                        try:
                            self.conn.sendall((json.dumps(resp) + '\n').encode('utf-8'))
                        except Exception:
                            traceback.print_exc()
                    data = b""
        except Exception:
            traceback.print_exc()


def start_server(host=HOST, port=PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen(5)
        print(f"Flame listener listening on {host}:{port}")
        while True:
            conn, addr = s.accept()
            ClientHandler(conn, addr).start()


if __name__ == '__main__':
    start_server()
