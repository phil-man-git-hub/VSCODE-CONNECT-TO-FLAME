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


def test_register_menu():
    code = "import examples.hooks.ui_menu_example as u; print('OUT:'+str(u.register_menu()))"
    resp = call_execute(code)
    assert 'OUT:' in resp.get('stdout','')


def test_menu_actions():
    code = "import examples.hooks.ui_menu_example as u; print('OUT:'+str(u.menu_action('list_clips')))"
    resp = call_execute(code)
    assert 'OUT:' in resp.get('stdout','')


def test_toggle_feature():
    code = "import examples.hooks.toggle_feature_hook as t; print('OUT:'+str(t.set_toggle(True))); print('OUT:'+str(t.get_toggle()))"
    resp = call_execute(code)
    assert 'OUT:' in resp.get('stdout','')


def test_confirm_preview():
    code = "import examples.hooks.confirm_action_hook as c; print('OUT:'+str(c.preview_delete_selection()))"
    resp = call_execute(code)
    assert 'OUT:' in resp.get('stdout','')
