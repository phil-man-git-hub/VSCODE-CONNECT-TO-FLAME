#!/usr/bin/env python3
import socket, json, textwrap, time
HOST='127.0.0.1'; PORT=5555
code = textwrap.dedent('''
print('IDENT-START')
import sys, importlib
mods=','.join([k for k in sys.modules if 'flame_listener' in k])
print('MODS:'+mods)
try:
    m= importlib.import_module('flame_listener')
    print('FILE:'+str(getattr(m,'__file__','<no-file>')))
    print('HAS_WAIT:'+str(hasattr(m,'wait_for_threads_at_exit')))
    print('HAS_RECV_TIMEOUT:'+str(hasattr(m,'RECV_TIMEOUT') or hasattr(m,'DEFAULT_RECV_TIMEOUT')))
except Exception as e:
    print('ERR:'+repr(e))
print('IDENT-END')
''')
msg = {'command':'execute','id':'inspect','code':code}
for attempt in range(6):
    try:
        print('attempt', attempt)
        with socket.create_connection((HOST, PORT), timeout=5) as s:
            s.settimeout(5)
            s.sendall(json.dumps(msg).encode('utf-8'))
            data = b''
            while True:
                chunk = s.recv(4096)
                if not chunk:
                    break
                data += chunk
            print('raw reply:', data)
            try:
                obj = json.loads(data.decode('utf-8'))
                print('json reply:', obj)
            except Exception as e:
                print('parse failed', e)
            break
    except Exception as e:
        print('attempt failed:', repr(e))
        time.sleep(0.5)
