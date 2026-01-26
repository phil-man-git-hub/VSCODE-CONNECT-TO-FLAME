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


def test_run_list_clips():
    code = "import examples.hooks.list_clips_hook as h; print('OUT:'+str(h.run_list_clips()))"
    resp = call_execute(code)
    assert 'OUT:' in resp.get('stdout','')


def test_show_timeline_ranges():
    code = "import examples.hooks.show_timeline_ranges_hook as h; print('OUT:'+str(h.run_show_ranges()))"
    resp = call_execute(code)
    assert 'OUT:' in resp.get('stdout','')


def test_preview_marker():
    code = "import examples.hooks.marker_preview_hook as h; print('OUT:'+str(h.preview_marker(100,'t','red')))"
    resp = call_execute(code)
    assert 'OUT:' in resp.get('stdout','')
