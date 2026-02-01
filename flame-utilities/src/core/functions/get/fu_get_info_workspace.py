"""
fu_get_info_workspace.py - Part of the FLAME-UTILITIES suite.
Workspace Inspector. Retrieves Workspace identity, Desktop list, and Library count.
"""

import flame

def workspace(selection=None):
    """Gathers and returns Workspace metadata."""
    def safe_val(val):
        if val is None: return None
        return str(val).strip("'")

    ws = flame.project.current_project.current_workspace

    if not ws:
        data = {"error": "No Workspace active"}
    else:
        data = {
            'name': safe_val(ws.name),
            'desktops': [safe_val(d.name) for d in ws.desktops] if ws.desktops else [],
            'libraries': len(ws.libraries) if ws.libraries else 0,
            'is_current': True
        }
    
    return data
