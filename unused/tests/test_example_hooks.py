import socket
import json
import pytest

HOST = '127.0.0.1'
PORT = 5555


def call_execute(code, timeout=5):
    msg = {'command': 'execute', 'id': 't', 'code': code}
    try:
        with socket.create_connection((HOST, PORT), timeout=2) as s:
            s.settimeout(timeout)
            s.sendall(json.dumps(msg).encode('utf-8'))
            data = b''
            while True:
                chunk = s.recv(4096)
                if not chunk:
                    break
                data += chunk
            return json.loads(data.decode('utf-8'))
    except Exception as e:
        pytest.skip(f'Listener not available: {e}')


def test_startup_example():
    code = "import examples.hooks.startup_example as se; print('OUT:'+str(se.sample_startup()))"
    resp = call_execute(code)
    assert 'OUT:' in resp.get('stdout','')


def test_menu_example():
    code = "import examples.hooks.menu_example as me; print('OUT:'+str(me.get_menu_items()))"
    resp = call_execute(code)
    assert 'OUT:' in resp.get('stdout','')


def test_asset_sync_example():
    code = "import examples.hooks.asset_sync_example as ae; print('OUT:'+str(ae.sync_preview()))"
    resp = call_execute(code)
    assert 'OUT:' in resp.get('stdout','')
