#!/usr/bin/env python3
import socket, json, sys
HOST='127.0.0.1'; PORT=5555
code = (
    'import importlib\n'
    'import flame_listener as fl\n'
    'fl = importlib.reload(fl)\n'
    'print("RELOADED_FILE:" + str(getattr(fl, "__file__", None)))\n'
    'print("RELOADED_VERSION:" + str(getattr(fl, "__version__", None)))\n'
    'print("DEFAULT_RECV_TIMEOUT:" + str(getattr(fl, "DEFAULT_RECV_TIMEOUT", None)))\n'
    'print("HAS_WAIT:" + str(hasattr(fl, "wait_for_threads_at_exit")))\n'
)
msg = {'command': 'execute', 'id': 'reload1', 'code': code}
try:
    with socket.create_connection((HOST, PORT), timeout=2) as s:
        s.sendall(json.dumps(msg).encode('utf-8'))
        data = b''
        while True:
            chunk = s.recv(4096)
            if not chunk:
                break
            data += chunk
            try:
                obj = json.loads(data.decode('utf-8'))
                print('reply:', obj)
                sys.exit(0)
            except json.JSONDecodeError:
                continue
except Exception as e:
    print('failed:', e)
    sys.exit(1)
print('no-reply')
