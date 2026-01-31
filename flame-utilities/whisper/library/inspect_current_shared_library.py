"""
Shared Library Inspector. Retrieves metadata and lock status for Shared Libraries.
"""

import flame
import json

def safe_val(val):
    if val is None: return None
    return str(val).strip("'")

# Target first selected Shared Library
sel = flame.media_panel.get_selected_objects() if hasattr(flame.media_panel, 'get_selected_objects') else []
selection = [o for o in sel if str(type(o)).count('Library') and getattr(o, 'is_shared', False)]
lib = selection[0] if selection else None

if not lib:
    print(json.dumps({"error": "No Shared Library selected"}, indent=2))
else:
    data = {
        'name': safe_val(lib.name),
        'is_shared': True,
        'lock_status': getattr(lib, 'lock_status', 'Unknown'),
        'wiretap_node_id': safe_val(lib.get_wiretap_node_id()) if hasattr(lib, 'get_wiretap_node_id') else None
    }
    print(json.dumps(data, indent=2))
