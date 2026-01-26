#!/usr/bin/env python3
"""Collect a mini debug bundle from a running Flame and the listener.

Saves outputs into a timestamped directory under /tmp for easy attachment.
"""
import socket
import json
import subprocess
import time
import os
from datetime import datetime

OUTDIR = f"/tmp/flame_debug_bundle_{int(time.time())}"
os.makedirs(OUTDIR, exist_ok=True)

def run(cmd):
    try:
        out = subprocess.getoutput(cmd)
    except Exception as e:
        out = f"ERROR: {e}"
    with open(os.path.join(OUTDIR, 'cmd_' + cmd.replace('/', '_').replace(' ', '_') + '.txt'), 'w') as fh:
        fh.write(out)
    return out

print('Collecting logs to', OUTDIR)
run('date')
run('uname -a')
run('ps aux | grep flame | grep -v grep')
run('lsof -nP -iTCP -sTCP:LISTEN | grep 5555 || true')
run('lsof -nP -iTCP -sTCP:LISTEN | grep 5678 || true')

# Attempt to ping the listener
HOST='127.0.0.1'; PORT=5555
try:
    s = socket.create_connection((HOST, PORT), timeout=3)
    payload = {'command': 'ping', 'id': 'collect-ping'}
    s.sendall(json.dumps(payload).encode())
    s.shutdown(1)
    data = b''
    while True:
        chunk = s.recv(4096)
        if not chunk: break
        data += chunk
    s.close()
    with open(os.path.join(OUTDIR, 'ping_resp.json'), 'wb') as fh:
        fh.write(data)
    print('Ping ok')
except Exception as e:
    with open(os.path.join(OUTDIR, 'ping_error.txt'), 'w') as fh:
        fh.write(str(e))
    print('Ping failed:', e)

# Fire the background breakpoint test (does not block)
code = '''import threading, traceback

def bp_test():
    try:
        import debugpy
        print('bp_test: waiting for client (5s)')
        try:
            debugpy.wait_for_client(timeout=5)
            print('bp_test: client attached')
        except Exception:
            print('bp_test: client did not attach within timeout')
        print('bp_test: invoking breakpoint')
        try:
            debugpy.breakpoint()
            print('bp_test: resumed after breakpoint')
        except Exception:
            traceback.print_exc()
    except Exception:
        traceback.print_exc()

threading.Thread(target=bp_test, daemon=True).start()
print('bp_test: started')'''
try:
    s = socket.create_connection((HOST, PORT), timeout=3)
    s.sendall(json.dumps({'command': 'execute', 'id': 'collect-bp3', 'code': code}).encode())
    s.shutdown(1)
    data = b''
    while True:
        chunk = s.recv(4096)
        if not chunk: break
        data += chunk
    with open(os.path.join(OUTDIR, 'bp_start_resp.json'), 'wb') as fh:
        fh.write(data)
    s.close()
    print('bp test started')
except Exception as e:
    with open(os.path.join(OUTDIR, 'bp_start_error.txt'), 'w') as fh:
        fh.write(str(e))
    print('bp test failed to start:', e)

# Wait a bit and collect the local flame_listener log if present
time.sleep(2)
log_file = os.environ.get('FLAME_LISTENER_LOG', '/tmp/flame_listener.log')
if os.path.exists(log_file):
    run(f'head -n 200 {log_file} > {os.path.join(OUTDIR, "listener_log_head.txt")}')
    run(f'tail -n 200 {log_file} > {os.path.join(OUTDIR, "listener_log_tail.txt")}')
else:
    with open(os.path.join(OUTDIR, 'listener_log_missing.txt'), 'w') as fh:
        fh.write('listener log not found: ' + log_file)

print('Bundle collected:', OUTDIR)
