#!/usr/bin/env python3
import socket, json, sys
HOST='127.0.0.1'; PORT=5555
payload = {'command':'execute','id':'inspect-json','code':'import importlib; m=importlib.import_module("flame_listener"); print("FLAME_FILE:"+str(getattr(m,"__file__",None))); print("FLAME_VERSION:"+str(getattr(m,"__version__",None))); print("HAS_WAIT:"+str(hasattr(m,"wait_for_threads_at_exit"))); print("HAS_RECV:"+str(hasattr(m,\'RECV_TIMEOUT\') or hasattr(m,\'DEFAULT_RECV_TIMEOUT\')))'}
try:
    with socket.create_connection((HOST, PORT), timeout=2) as s:
        s.sendall(json.dumps(payload).encode('utf-8'))
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
