#!/usr/bin/env python3
import socket, json, os
HOST='127.0.0.1'; PORT=5555
out = '/Volumes/Samsung-T3-1TB/Autodesk/flame/projects/vscode_connect_to_flame_2027_romeo/setups/python/stubs'
code = f"import os, generate_stubs; os.makedirs('{out}', exist_ok=True); print('CALL_OK', generate_stubs.generate_stubs_for_module('flame', '{out}', quiet=False)); print('LS', sorted(os.listdir('{out}')) )"
msg = {'command':'execute','id':'stub-run','code':code}
with socket.create_connection((HOST, PORT), timeout=5) as s:
    s.settimeout(10)
    s.sendall(json.dumps(msg).encode('utf-8'))
    data = b''
    while True:
        chunk = s.recv(4096)
        if not chunk:
            break
        data += chunk
    print(data.decode('utf-8','replace'))
