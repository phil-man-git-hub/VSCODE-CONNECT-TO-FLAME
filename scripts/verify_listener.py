#!/usr/bin/env python3
import socket
import json
import time
HOST='127.0.0.1'; PORT=5555
payload = {
    'command': 'execute',
    'id': 'verify1',
    'code': (
        'import importlib\n'
        'm = importlib.import_module("flame_listener")\n'
        'print("FLAME_FILE:" + str(getattr(m, "__file__", None)))\n'
        'print("FLAME_VERSION:" + str(getattr(m, "__version__", None)))\n'
        'print("HAS_WAIT:" + str(hasattr(m, "wait_for_threads_at_exit")))\n'
        'print("HAS_RECV:" + str(hasattr(m, "RECV_TIMEOUT") or hasattr(m, "DEFAULT_RECV_TIMEOUT")))\n'
    )
}

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.settimeout(3)
    s.connect((HOST, PORT))
    s.settimeout(5)
    s.sendall(json.dumps(payload).encode('utf-8'))
    data = b''
    deadline = time.time() + 5
    while time.time() < deadline:
        try:
            chunk = s.recv(4096)
        except Exception:
            break
        if not chunk:
            break
        data += chunk
        try:
            obj = json.loads(data.decode('utf-8'))
            print('reply json:', obj)
            break
        except Exception:
            continue
    else:
        print('no json within timeout; raw:', data.decode('utf-8', 'replace'))
finally:
    try:
        s.close()
    except Exception:
        pass
