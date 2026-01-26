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

    # Run the mock server with unbuffered stdout so we can detect readiness via its startup message.
    proc = subprocess.Popen([sys.executable, '-u', server_py, str(port)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Wait for the mock server to print a startup message indicating it's ready.
    import select
    deadline = time.time() + 3.0
    ready = False
    while time.time() < deadline:
        if proc.poll() is not None:
            out, err = proc.communicate()
            raise AssertionError(f"Mock server exited prematurely. stdout={out!r} stderr={err!r}")
        r, _, _ = select.select([proc.stdout.fileno()], [], [], 0.05)
        if r:
            line = proc.stdout.readline()
            if 'Running mock_flame_server' in line:
                ready = True
                break
    if not ready:
        try:
            out, err = proc.communicate(timeout=1)
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.wait(timeout=1)
            out, err = proc.communicate()
        raise AssertionError(f"Mock server did not print readiness message. stdout={out!r} stderr={err!r}")

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
        try:
            proc.wait(timeout=3)
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.wait(timeout=1)
        # Ensure we drain stdout/stderr to avoid zombies
        proc.communicate()

if __name__ == '__main__':
    sys.exit(0 if test_start_debug_server() is None else 1)
