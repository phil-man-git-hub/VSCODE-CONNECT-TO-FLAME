import subprocess
import socket
import json
import sys
import os
import time

HOST = '127.0.0.1'


def test_start_debug_server():
    # Launch the mock server (it will handle a single request and exit). Use an ephemeral free port so tests
    # won't fail if real Flame is running on 5555.
    server_py = os.path.join(os.path.dirname(__file__), 'mock_flame_server.py')
    # Pick an unused port
    with socket.socket() as _s:
        _s.bind((HOST, 0))
        port = _s.getsockname()[1]

    proc = subprocess.Popen([sys.executable, server_py, str(port)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(0.1)
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, port))
            payload = {'command': 'start_debug_server', 'id': 't1', 'port': 5678}
            s.sendall(json.dumps(payload).encode('utf-8'))
            data = b''
            while True:
                chunk = s.recv(4096)
                if not chunk:
                    break
                data += chunk
                try:
                    resp = json.loads(data.decode('utf-8'))
                    assert 'Debug server started' in resp.get('stdout', ''), f"Unexpected resp: {resp}"
                    break
                except json.JSONDecodeError:
                    continue
    finally:
        proc.wait(timeout=1)

if __name__ == '__main__':
    sys.exit(0 if test_start_debug_server() is None else 1)
