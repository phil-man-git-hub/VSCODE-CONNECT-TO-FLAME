"""
Workspace Inspector. Retrieves Workspace identity, Desktop list, and Library count.
"""

import flame
import json

def safe_val(val):
    if val is None: return None
    return str(val).strip("'")

w = flame.project.current_project.current_workspace

data = {
    'name': safe_val(w.name),
    'desktops': [safe_val(d.name) for d in w.desktops],
    'libraries': len(w.libraries),
    'is_current': True
}

print(json.dumps(data, indent=2))
