"""
Segment Inspector. Retrieves Timeline Segment data: range, source, and track.
"""

import flame
import json

def safe_val(val):
    if val is None: return None
    return str(val).strip("'")

# Segments are usually only accessible via timeline selection or iteration
sel = flame.media_panel.get_selected_objects() if hasattr(flame.media_panel, 'get_selected_objects') else []
selection = [o for o in sel if str(type(o)).count('Segment')]
seg = selection[0] if selection else None

if not seg:
    print(json.dumps({"error": "No Segment selected"}, indent=2))
else:
    data = {
        'name': safe_val(seg.name),
        'shot_name': safe_val(getattr(seg, 'shot_name', None)),
        'comment': safe_val(getattr(seg, 'comment', None)),
        'record_in': seg.record_in.frame if hasattr(seg.record_in, 'frame') else str(seg.record_in),
        'record_out': seg.record_out.frame if hasattr(seg.record_out, 'frame') else str(seg.record_out),
        'source_name': safe_val(getattr(seg, 'source_name', None)),
        'track': safe_val(seg.parent.name) if hasattr(seg, 'parent') and seg.parent else "Unknown"
    }
    print(json.dumps(data, indent=2))
