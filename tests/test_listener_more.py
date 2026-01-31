import os
import time
import socket
import json
import importlib.util
import threading

import pytest

# Local copies of helpers (kept local to avoid import/package issues in pytest collection)

def start_listener_module(port):
    repo_root = os.path.dirname(os.path.dirname(__file__))
    listener_path = os.path.join(repo_root, 'flame-utilities', 'fu_eavesdrop.py')
    spec = importlib.util.spec_from_file_location('fu_eavesdrop', listener_path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    t = threading.Thread(target=m.initialize_eavesdrop, kwargs={'host': '127.0.0.1', 'port': port}, daemon=True)
    t.start()
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


def test_long_running_exec_and_thread_tracking():
    port = find_free_port()
    m, t = start_listener_module(port)
    # make sure threads list gets populated for long-running exec
    payload = {'command': 'execute', 'id': 'long1', 'code': "import time\ntime.sleep(0.5)\nprint('done')", 'timeout': 0.1}
    resp = send_request('127.0.0.1', port, payload, timeout=2)
    assert resp is not None
    assert resp.get('exception') == 'TimeoutError'
    # the listener module should have a threads list with at least one exec thread
    assert hasattr(m, 'threads')
    assert any(getattr(th, 'name', '').startswith('exec-') for th in m.threads)


def test_concurrent_execs_complete():
    port = find_free_port()
    m, t = start_listener_module(port)
    payload1 = {'command': 'execute', 'id': 'c1', 'code': "print('c1')", 'timeout': 1}
    payload2 = {'command': 'execute', 'id': 'c2', 'code': "print('c2')", 'timeout': 1}
    r1 = r2 = None

    def req(p, out_holder):
        out_holder.append(send_request('127.0.0.1', port, p, timeout=2))

    o1 = []
    o2 = []
    th1 = threading.Thread(target=req, args=(payload1, o1), daemon=True)
    th2 = threading.Thread(target=req, args=(payload2, o2), daemon=True)
    th1.start(); th2.start()
    th1.join(); th2.join()
    assert o1 and o2
    assert o1[0].get('stdout').strip() == 'c1'
    assert o2[0].get('stdout').strip() == 'c2'


class FakeDebugpy:
    _evt = threading.Event()

    def listen(self, ep, in_process_debug_adapter=True):
        return ep

    def wait_for_client(self, timeout=None):
        # wait until test sets the event to simulate an attach
        return FakeDebugpy._evt.wait(timeout=timeout)


def test_debug_attach_logs_when_client_simulates(monkeypatch, tmp_path):
    port = find_free_port()
    m, t = start_listener_module(port)
    log = os.environ.get('FLAME_LISTENER_LOG', '/tmp/fu_eavesdrop.log')
    try:
        os.remove(log)
    except Exception:
        pass

    # inject fake debugpy
    fake = FakeDebugpy()
    monkeypatch.setitem(__import__('sys').modules, 'debugpy', fake)

    resp = send_request('127.0.0.1', port, {'command': 'start_debug_server', 'id': 'dbg', 'port': 5679})
    assert resp is not None
    assert 'Starting debug server' in resp.get('stdout', '')

    # after a short delay, simulate the client attaching
    time.sleep(0.05)
    FakeDebugpy._evt.set()

    assert tail_log_until_contains(log, 'debug client attached', timeout=2.0)
