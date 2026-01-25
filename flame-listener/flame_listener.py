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

    When running inside Flame we schedule execution on the main thread and
    wait for completion (up to `timeout` seconds). This ensures Flame API
    calls execute on the UI thread and we still return stdout/stderr.
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
        if HAS_FLAME:
            # Schedule execution on Flame's main thread and wait for completion
            try:
                flame.execute_on_main_thread(_run_exec)
            except Exception:
                # If execute_on_main_thread doesn't run synchronously, try running
                # and waiting on the event (some Flame versions may schedule async)
                threading.Thread(target=flame.execute_on_main_thread, args=(_run_exec,), daemon=True).start()
                finished.wait(timeout)
        else:
            _run_exec()
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
        with self.conn:
            data = b""
            while True:
                chunk = self.conn.recv(4096)
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
                    self.conn.sendall((json.dumps(resp) + '\n').encode('utf-8'))
                    data = b""
                    continue
                cmd = payload.get('command')
                if cmd == 'execute':
                    code = payload.get('code', '')
                    out, err, exc = handle_execute(code)
                    resp = {'id': payload.get('id'), 'stdout': out or '', 'stderr': err or '', 'exception': exc}
                    self.conn.sendall((json.dumps(resp) + '\n').encode('utf-8'))
                elif cmd == 'ping':
                    resp = {'id': payload.get('id'), 'stdout': 'pong', 'stderr': '', 'exception': None}
                    self.conn.sendall((json.dumps(resp) + '\n').encode('utf-8'))
                elif cmd == 'start_debug_server':
                    # Start debugpy if available and return status
                    try:
                        import debugpy  # type: ignore
                        port = payload.get('port', 5678)
                        debugpy.listen(('127.0.0.1', port))
                        resp = {'id': payload.get('id'), 'stdout': f'debugpy listening on 127.0.0.1:{port}', 'stderr': '', 'exception': None}
                    except Exception as e:
                        resp = {'id': payload.get('id'), 'stdout': '', 'stderr': traceback.format_exc(), 'exception': str(e)}
                    self.conn.sendall((json.dumps(resp) + '\n').encode('utf-8'))
                else:
                    resp = {'id': payload.get('id'), 'stdout': '', 'stderr': 'unknown command', 'exception': 'CommandError'}
                    self.conn.sendall((json.dumps(resp) + '\n').encode('utf-8'))
                data = b""


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
