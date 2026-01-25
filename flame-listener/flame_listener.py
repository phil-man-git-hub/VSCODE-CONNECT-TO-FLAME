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
AUTH_TOKEN = None  # Set to a value for token-based auth

try:
    import flame  # type: ignore
    HAS_FLAME = True
except Exception:
    HAS_FLAME = False


def handle_execute(code):
    """Execute `code` and capture stdout/stderr and exceptions."""
    stdout = io.StringIO()
    stderr = io.StringIO()
    try:
        if HAS_FLAME:
            # Execute on main thread when in Flame
            def _run():
                try:
                    exec(code, globals(), locals())
                except Exception:
                    traceback.print_exc(file=stderr)
            flame.execute_on_main_thread(_run)
        else:
            # Development: run directly
            exec(code, globals(), locals())
        out = stdout.getvalue()
        err = stderr.getvalue()
        return out, err, None
    except Exception as e:
        tb = traceback.format_exc()
        return stdout.getvalue(), stderr.getvalue() + tb, str(e)


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
