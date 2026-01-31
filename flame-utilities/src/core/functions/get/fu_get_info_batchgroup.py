"""
fu_get_info_batchgroup.py - Part of the FLAME-UTILITIES suite.
Batch Group Inspector. Retrieves Batch Group identity, iteration, and setup data.
"""

import flame
import json
from fu_decorators import fu_action

@fu_action(menu="media_panel", path="FU / get / info")
@fu_action(menu="batch", path="FU / get / info")
def batchgroup(selection=None):
    """Gathers and returns Batch Group metadata."""
    def safe_val(val):
        if val is None: return None
        return str(val).strip("'")

    # Target first selected Batch Group or active one
    sel = flame.media_panel.get_selected_objects() if hasattr(flame.media_panel, 'get_selected_objects') else []
    selection_bg = [o for o in sel if str(type(o)).count('BatchGroup')]

    bg = None
    if selection_bg:
        bg = selection_bg[0]
    elif hasattr(flame, 'batch') and flame.batch.current_group:
        bg = flame.batch.current_group

    if not bg:
        data = {"error": "No Batch Group found"}
    else:
        data = {
            'name': safe_val(bg.name),
            'iteration': safe_val(getattr(bg, 'iteration', None)),
            'start_frame': getattr(bg, 'start_frame', None),
            'duration': bg.duration.frame if hasattr(bg, 'duration') and hasattr(bg.duration, 'frame') else str(getattr(bg, 'duration', 'Unknown')),
            'wiretap_node_id': safe_val(bg.get_wiretap_node_id()) if hasattr(bg, 'get_wiretap_node_id') else None
        }
    
    print("--- BATCH GROUP INFO ---")
    print(json.dumps(data, indent=4))
    return data
