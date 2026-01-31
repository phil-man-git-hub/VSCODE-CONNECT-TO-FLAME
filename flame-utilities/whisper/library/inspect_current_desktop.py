"""
Desktop Inspector. Retrieves Desktop identity, Reel Groups, Batch Groups, and Libraries.
"""

import flame
import json

def safe_val(val):
    if val is None: return None
    return str(val).strip("'")

ws = flame.project.current_project.current_workspace
d = ws.desktop if ws else None

if not d:
    print(json.dumps({"error": "No Desktop active"}, indent=2))
else:
    data = {
        'name': safe_val(d.name),
        'reel_groups': [safe_val(rg.name) for rg in d.reel_groups] if d.reel_groups else [],
        'batch_groups': [safe_val(bg.name) for bg in d.batch_groups] if d.batch_groups else [],
        'libraries': [safe_val(lib.name) for lib in d.libraries] if d.libraries else [],
        'wiretap_node_id': safe_val(d.get_wiretap_node_id()) if hasattr(d, 'get_wiretap_node_id') else None
    }
    print(json.dumps(data, indent=2))
