import socket
import json
import pytest

HOST = '127.0.0.1'
PORT = 5555


def call_execute(code, timeout=10):
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


def test_project_snippet():
    code = "import examples.snippets.project_snippet as ps; print('OUT:'+str(ps.get_current_project_info()))"
    resp = call_execute(code)
    assert 'OUT:' in resp.get('stdout','')


def test_marker_make_payload():
    code = "import examples.snippets.marker_snippet as ms; print('OUT:'+str(ms.make_marker_payload(100,'t','red')))"
    resp = call_execute(code)
    assert 'OUT:' in resp.get('stdout','')


def test_timeline_snippet():
    code = "import examples.snippets.timeline_snippet as ts; print('OUT:'+str(ts.list_timelines()))"
    resp = call_execute(code)
    assert 'OUT:' in resp.get('stdout','')


def test_timeline_frame_ranges():
    code = "import examples.snippets.timeline_snippet as ts; print('OUT:'+str(ts.timeline_frame_ranges()))"
    resp = call_execute(code)
    assert 'OUT:' in resp.get('stdout','')


def test_clip_snippet():
    code = "import examples.snippets.clip_snippet as cs; print('OUT:'+str(cs.list_clips_in_current_timeline()))"
    resp = call_execute(code)
    assert 'OUT:' in resp.get('stdout','')


def test_find_clip_by_name():
    code = "import examples.snippets.clip_snippet as cs; print('OUT:'+str(cs.find_clip_by_name('nonexistent')) )"
    resp = call_execute(code)
    assert 'OUT:' in resp.get('stdout','')
