#!/usr/bin/env python3
import socket,json,time,subprocess,sys
HOST='127.0.0.1'; PORT=5555
dbg_port = int(sys.argv[1]) if len(sys.argv)>1 else 5679
msg={'command':'start_debug_server','id':'s1','port':dbg_port}
result = {'sent_port': dbg_port}
try:
    with socket.create_connection((HOST, PORT), timeout=3) as s:
        s.settimeout(5)
        s.sendall(json.dumps(msg).encode('utf-8'))
        data = b''
        try:
            while True:
                chunk = s.recv(4096)
                if not chunk: break
                data += chunk
        except Exception:
            pass
        result['reply_raw'] = data.decode('utf-8', 'replace')
except Exception as e:
    result['send_error'] = repr(e)
# Check whether debug port is listening
proc = subprocess.run(['lsof','-nP','-iTCP:%d' % dbg_port,'-sTCP:LISTEN'], capture_output=True, text=True)
result['lsof_output'] = proc.stdout.strip()
# Try connecting to debug port (non-blocking short timeout)
try:
    with socket.create_connection(('127.0.0.1', dbg_port), timeout=1) as s:
        result['connectable'] = True
except Exception as e:
    result['connectable'] = False
    result['connect_error'] = repr(e)
print(json.dumps(result, indent=2))
