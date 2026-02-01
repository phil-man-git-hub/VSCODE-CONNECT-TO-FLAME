"""
fu_get_info_shared_library.py - Part of the FLAME-UTILITIES suite.
Shared Library Inspector. Retrieves metadata and lock status for Shared Libraries.
"""

import flame

def shared_library(selection=None):
    """Gathers and returns Shared Library metadata."""
    def safe_val(val):
        if val is None: return None
        return str(val).strip("'")

    # Target first selected Shared Library
    sel = flame.media_panel.get_selected_objects() if hasattr(flame.media_panel, 'get_selected_objects') else []
    selection_lib = [o for o in sel if str(type(o)).count('Library') and getattr(o, 'is_shared', False)]
    lib = selection_lib[0] if selection_lib else None

    if not lib:
        data = {"error": "No Shared Library selected"}
    else:
        data = {
            'name': safe_val(lib.name),
            'is_shared': True,
            'lock_status': getattr(lib, 'lock_status', 'Unknown'),
            'wiretap_node_id': safe_val(lib.get_wiretap_node_id()) if hasattr(lib, 'get_wiretap_node_id') else None
        }
    
    return data

if __name__ == "__main__":
    import json
    print(json.dumps(shared_library(), indent=4))
