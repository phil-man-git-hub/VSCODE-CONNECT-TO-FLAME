"""
Workspace Inspector. Retrieves Workspace identity, Desktop list, and Library count.
"""

import flame
import json

def safe_val(val):
    if val is None: return None
    return str(val).strip("'")

w = flame.project.current_project.current_workspace

if not w:
    print(json.dumps({"error": "No Workspace active"}, indent=2))
else:
    data = {
        'name': safe_val(w.name),
        'desktops': [safe_val(d.name) for d in w.desktops] if w.desktops else [],
        'libraries': len(w.libraries) if w.libraries else 0,
        'is_current': True
    }
    print(json.dumps(data, indent=2))
