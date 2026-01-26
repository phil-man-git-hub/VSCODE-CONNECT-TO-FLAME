import socket, json
HOST='127.0.0.1'; PORT=5555
code = 'import importlib; m=importlib.import_module("flame_listener"); print("FLAME_FILE:"+str(getattr(m,"__file__",None))); print("HAS_WAIT:"+str(hasattr(m,"wait_for_threads_at_exit"))); print("HAS_RECV:"+str(hasattr(m,"RECV_TIMEOUT") or hasattr(m,"DEFAULT_RECV_TIMEOUT")))'
msg={'command':'execute','id':'tmp1','code':code}
with socket.create_connection((HOST, PORT), timeout=2) as s:
    s.settimeout(5)
    s.sendall(json.dumps(msg).encode('utf-8'))
    data = b''
    while True:
        chunk = s.recv(4096)
        if not chunk: break
        data += chunk
    print(data.decode('utf-8', 'replace'))
