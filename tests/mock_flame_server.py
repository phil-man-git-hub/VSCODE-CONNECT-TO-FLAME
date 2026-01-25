"""A very small mock server used for extension development and CI tests.

This mimics the minimal subset of the Flame listener protocol: `execute` and `ping`.
"""

import socket
import json

HOST = '127.0.0.1'
PORT = 5555


def run_once():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        conn, _ = s.accept()
        with conn:
            data = conn.recv(4096)
            if not data:
                return
            payload = json.loads(data.decode('utf-8'))
            if payload.get('command') == 'ping':
                conn.sendall((json.dumps({'id': payload.get('id'), 'stdout': 'pong', 'stderr': '', 'exception': None}) + '\n').encode('utf-8'))
            elif payload.get('command') == 'execute':
                code = payload.get('code', '')
                try:
                    # Unsafe eval for mock only
                    exec_globals = {}
                    exec(code, exec_globals)
                    conn.sendall((json.dumps({'id': payload.get('id'), 'stdout': '', 'stderr': '', 'exception': None}) + '\n').encode('utf-8'))
                except Exception as e:
                    conn.sendall((json.dumps({'id': payload.get('id'), 'stdout': '', 'stderr': str(e), 'exception': 'ExecutionError'}) + '\n').encode('utf-8'))


if __name__ == '__main__':
    print('Running mock_flame_server (single request)')
    run_once()
