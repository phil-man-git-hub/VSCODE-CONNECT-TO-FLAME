"""
Library Inspector. Retrieves Library identity and child counts.
"""

import flame
import json

def safe_val(val):
    if val is None: return None
    return str(val).strip("'")

# Target first selected Library
sel = flame.media_panel.get_selected_objects() if hasattr(flame.media_panel, 'get_selected_objects') else []
selection = [o for o in sel if str(type(o)).count('Library')]
lib = selection[0] if selection else None

if not lib:
    print(json.dumps({"error": "No Library selected"}, indent=2))
else:
    data = {
        'name': safe_val(lib.name),
        'is_shared': getattr(lib, 'is_shared', False),
        'item_count': (len(lib.clips) if lib.clips else 0) + (len(lib.sequences) if lib.sequences else 0),
        'wiretap_node_id': safe_val(lib.get_wiretap_node_id()) if hasattr(lib, 'get_wiretap_node_id') else None
    }
    print(json.dumps(data, indent=2))
