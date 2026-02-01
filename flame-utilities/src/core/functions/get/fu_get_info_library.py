"""
fu_get_info_library.py - Part of the FLAME-UTILITIES suite.
Library Inspector. Retrieves Library identity and child counts.
"""

import flame

def library(selection=None):
    """Gathers and returns Library metadata."""
    def safe_val(val):
        if val is None: return None
        return str(val).strip("'")

    sel = flame.media_panel.get_selected_objects() if hasattr(flame.media_panel, 'get_selected_objects') else []
    selection_lib = [o for o in sel if str(type(o)).count('Library')]
    lib = selection_lib[0] if selection_lib else None

    if not lib:
        data = {"error": "No Library selected"}
    else:
        data = {
            'name': safe_val(lib.name),
            'is_shared': getattr(lib, 'is_shared', False),
            'item_count': (len(lib.clips) if lib.clips else 0) + (len(lib.sequences) if lib.sequences else 0),
            'wiretap_node_id': safe_val(lib.get_wiretap_node_id()) if hasattr(lib, 'get_wiretap_node_id') else None
        }
    
    return data

if __name__ == "__main__":
    import json
    print(json.dumps(library(), indent=4))
