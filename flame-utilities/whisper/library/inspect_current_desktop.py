"""
Desktop Inspector. Retrieves Desktop identity, Reel Groups, Batch Groups, and Libraries.
"""

import flame
import json

def safe_val(val):
    if val is None: return None
    return str(val).strip("'")

d = flame.project.current_project.current_workspace.desktop

data = {
    'name': safe_val(d.name),
    'reel_groups': [safe_val(rg.name) for rg in d.reel_groups],
    'batch_groups': [safe_val(bg.name) for bg in d.batch_groups],
    'libraries': [safe_val(lib.name) for lib in d.libraries],
    'wiretap_node_id': safe_val(d.get_wiretap_node_id()) if hasattr(d, 'get_wiretap_node_id') else None
}

print(json.dumps(data, indent=2))
