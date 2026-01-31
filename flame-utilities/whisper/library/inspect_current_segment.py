"""
Segment Inspector. Retrieves Timeline Segment data: range, source, and track.
"""

import flame
import json

def safe_val(val):
    if val is None: return None
    return str(val).strip("'")

# Segments are usually only accessible via timeline selection or iteration
selection = [o for o in flame.media_panel.selected_objects if str(type(o)).count('Segment')]
seg = selection[0] if selection else None

if not seg:
    print(json.dumps({"error": "No Segment selected"}, indent=2))
else:
    data = {
        'name': safe_val(seg.name),
        'shot_name': safe_val(seg.shot_name),
        'comment': safe_val(seg.comment),
        'record_in': seg.record_in.frame if hasattr(seg.record_in, 'frame') else str(seg.record_in),
        'record_out': seg.record_out.frame if hasattr(seg.record_out, 'frame') else str(seg.record_out),
        'source_name': safe_val(seg.source_name),
        'track': safe_val(seg.parent.name) if hasattr(seg, 'parent') else "Unknown"
    }
    print(json.dumps(data, indent=2))
