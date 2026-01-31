"""
Batch Group Inspector. Retrieves Batch Group identity, iteration, and setup data.
"""

import flame
import json

def safe_val(val):
    if val is None: return None
    return str(val).strip("'")

# Target first selected Batch Group or active one
sel = flame.media_panel.get_selected_objects() if hasattr(flame.media_panel, 'get_selected_objects') else []
selection = [o for o in sel if str(type(o)).count('BatchGroup')]

bg = None
if selection:
    bg = selection[0]
elif hasattr(flame, 'batch') and flame.batch.current_group:
    bg = flame.batch.current_group

if not bg:
    print(json.dumps({"error": "No Batch Group found"}, indent=2))
else:
    data = {
        'name': safe_val(bg.name),
        'iteration': safe_val(getattr(bg, 'iteration', None)),
        'start_frame': getattr(bg, 'start_frame', None),
        'duration': bg.duration.frame if hasattr(bg, 'duration') and hasattr(bg.duration, 'frame') else str(getattr(bg, 'duration', 'Unknown')),
        'wiretap_node_id': safe_val(bg.get_wiretap_node_id()) if hasattr(bg, 'get_wiretap_node_id') else None
    }
    print(json.dumps(data, indent=2))
