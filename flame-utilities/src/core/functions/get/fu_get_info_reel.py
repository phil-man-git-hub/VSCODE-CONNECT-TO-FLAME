"""
fu_get_info_reel.py - Part of the FLAME-UTILITIES suite.
Reel Inspector. Targets the first selected Reel in the Media Panel.
"""

import flame

def reel(selection=None):
    """Gathers and returns Reel metadata."""
    def safe_val(val):
        if val is None: return None
        return str(val).strip("'")

    sel = flame.media_panel.get_selected_objects() if hasattr(flame.media_panel, 'get_selected_objects') else []
    selection_r = [o for o in sel if str(type(o)).count('Reel')]
    r = selection_r[0] if selection_r else None

    if not r:
        data = {"error": "No Reel selected"}
    else:
        data = {
            'name': safe_val(r.name),
            'clip_count': len(r.clips) if r.clips else 0,
            'parent': safe_val(r.parent.name) if hasattr(r, 'parent') and r.parent else None,
            'wiretap_node_id': safe_val(r.get_wiretap_node_id()) if hasattr(r, 'get_wiretap_node_id') else None
        }
    
    return data

