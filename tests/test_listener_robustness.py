import os
import time
import socket
import json
import subprocess
import sys
import importlib.util
import tempfile

import pytest

# Helpers to start listener module in background on ephemeral port

def start_listener_module(port):
    # Resolve path relative to this tests file so it works from any cwd
    repo_root = os.path.dirname(os.path.dirname(__file__))
    listener_path = os.path.join(repo_root, 'flame-listener', 'flame_listener.py')
    spec = importlib.util.spec_from_file_location('flame_listener', listener_path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    import threading
    t = threading.Thread(target=m.start_server, kwargs={'host': '127.0.0.1', 'port': port}, daemon=True)
    t.start()
    # Give server time to bind
    time.sleep(0.1)
    return m, t


def send_request(host, port, payload, timeout=5):
    with socket.create_connection((host, port), timeout=timeout) as s:
        s.sendall(json.dumps(payload).encode())
        s.shutdown(socket.SHUT_WR)
        data = b''
        s.settimeout(timeout)
        while True:
            try:
                chunk = s.recv(4096)
            except socket.timeout:
                break
            if not chunk:
                break
            data += chunk
    if not data:
        return None
    return json.loads(data.decode())


def tail_log_until_contains(logfile, substr, timeout=2.0):
    start = time.time()
    while time.time() - start < timeout:
        if os.path.exists(logfile):
            with open(logfile, 'r') as fh:
                txt = fh.read()
            if substr in txt:
                return True
        time.sleep(0.05)
    return False


def find_free_port():
    s = socket.socket()
    s.bind(('127.0.0.1', 0))
    p = s.getsockname()[1]
    s.close()
    return p


def test_execute_timeout():
    port = find_free_port()
    m, t = start_listener_module(port)
    # ensure log file is fresh
    log = os.environ.get('FLAME_LISTENER_LOG', '/tmp/flame_listener.log')
    try:
        os.remove(log)
    except Exception:
        pass
    # request a short timeout and sleep longer than that
    payload = {'command': 'execute', 'id': 't1', 'code': "import time\ntime.sleep(0.5)\nprint('done')", 'timeout': 0.1}
    resp = send_request('127.0.0.1', port, payload, timeout=2)
    assert resp is not None
    assert resp.get('exception') == 'TimeoutError'
    assert 'timed out' in resp.get('stderr', '')


def test_thread_exception_reports():
    port = find_free_port()
    m, t = start_listener_module(port)
    log = os.environ.get('FLAME_LISTENER_LOG', '/tmp/flame_listener.log')
    try:
        os.remove(log)
    except Exception:
        pass
    payload = {'command': 'execute', 'id': 't2', 'code': "import threading\ndef f():\n    raise RuntimeError('boom')\nthreading.Thread(target=f, daemon=True).start()\nprint('started')"}
    resp = send_request('127.0.0.1', port, payload)
    assert resp is not None
    assert resp.get('stdout', '').strip().endswith('started')
    # wait for thread death to be logged
    assert tail_log_until_contains(log, 'thread-exc', timeout=2.0)


def test_start_debug_server_ack_and_background(monkeypatch):
    port = find_free_port()
    m, t = start_listener_module(port)
    log = os.environ.get('FLAME_LISTENER_LOG', '/tmp/flame_listener.log')
    try:
        os.remove(log)
    except Exception:
        pass

    # monkeypatch a fake debugpy module so we don't actually open sockets
    class FakeDebugpy:
        def listen(self, ep, in_process_debug_adapter=True):
            return ep
        def wait_for_client(self, timeout=None):
            return None
        def breakpoint(self):
            return None
    import sys as _sys
    _sys.modules['debugpy'] = FakeDebugpy()

    payload = {'command': 'start_debug_server', 'id': 't3', 'port': 5678}
    resp = send_request('127.0.0.1', port, payload)
    assert resp is not None
    assert 'Starting debug server' in resp.get('stdout', '')
    # background thread should log adapter listening
    assert tail_log_until_contains(log, 'debug adapter listening', timeout=2.0)


def test_recv_timeout_on_partial_payload():
    port = find_free_port()
    m, t = start_listener_module(port)
    log = os.environ.get('FLAME_LISTENER_LOG', '/tmp/flame_listener.log')
    try:
        os.remove(log)
    except Exception:
        pass
    # reduce server recv timeout for the test
    os.environ['FLAME_LISTENER_RECV_TIMEOUT'] = '0.2'
    # connect and send partial JSON then pause
    s = socket.create_connection(('127.0.0.1', port))
    s.sendall(b'{"command": "ping", "id": "p')
    # wait longer than handler socket timeout
    time.sleep(0.5)
    # try to close
    s.close()
    # handler should have logged a recv timeout
    assert tail_log_until_contains(log, 'recv timeout', timeout=2.0)
