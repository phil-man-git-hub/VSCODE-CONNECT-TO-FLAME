"""
fu_get_info_reel_group.py - Part of the FLAME-UTILITIES suite.
Reel Group Inspector. Targets the first selected Reel Group in the Media Panel.
"""

import flame

def reel_group(selection=None):
    """Gathers and returns Reel Group metadata."""
    def safe_val(val):
        if val is None: return None
        return str(val).strip("'")

    # Target selection or first available on desktop
    sel = flame.media_panel.get_selected_objects() if hasattr(flame.media_panel, 'get_selected_objects') else []
    selection_rg = [o for o in sel if str(type(o)).count('ReelGroup')]

    ws = flame.project.current_project.current_workspace
    desktop = ws.desktop if ws else None

    rg = None
    if selection_rg:
        rg = selection_rg[0]
    elif desktop and desktop.reel_groups:
        rg = desktop.reel_groups[0]

    if not rg:
        data = {"error": "No Reel Group found"}
    else:
        data = {
            'name': safe_val(rg.name),
            'reels': [safe_val(r.name) for r in rg.reels] if rg.reels else [],
            'wiretap_node_id': safe_val(rg.get_wiretap_node_id()) if hasattr(rg, 'get_wiretap_node_id') else None
        }
    
    return data
