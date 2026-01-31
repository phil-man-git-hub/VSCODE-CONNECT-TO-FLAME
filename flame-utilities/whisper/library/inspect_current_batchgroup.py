"""
Batch Group Inspector. Retrieves Batch Group identity, iteration, and setup data.
"""

import flame
import json

def safe_val(val):
    if val is None: return None
    return str(val).strip("'")

# Target first selected Batch Group or active one
selection = [o for o in flame.media_panel.selected_objects if str(type(o)).count('BatchGroup')]
bg = selection[0] if selection else flame.batch.current_group if hasattr(flame, 'batch') else None

if not bg:
    print(json.dumps({"error": "No Batch Group found"}, indent=2))
else:
    data = {
        'name': safe_val(bg.name),
        'iteration': safe_val(bg.iteration) if hasattr(bg, 'iteration') else None,
        'start_frame': bg.start_frame if hasattr(bg, 'start_frame') else None,
        'duration': bg.duration.frame if hasattr(bg, 'duration') and hasattr(bg.duration, 'frame') else None,
        'wiretap_node_id': safe_val(bg.get_wiretap_node_id()) if hasattr(bg, 'get_wiretap_node_id') else None
    }
    print(json.dumps(data, indent=2))
