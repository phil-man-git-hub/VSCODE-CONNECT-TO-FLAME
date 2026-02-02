#!/usr/bin/env python3
import sys
sys.path.append('fu-whisper')
import json
from fu_relay import FlameRelay

relay = FlameRelay()
code = """
import flame
proj = flame.project.current_project
print(json.dumps({
    'name': proj.name,
    'nickname': getattr(proj, 'nickname', 'N/A'),
    'code': getattr(proj, 'code', 'N/A'),
    'path': getattr(proj, 'path', 'N/A')
}))
"""
resp = relay.execute(code)
print(resp)