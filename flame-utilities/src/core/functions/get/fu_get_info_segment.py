"""
fu_get_info_segment.py - Part of the FLAME-UTILITIES suite.
Segment Inspector. Retrieves Timeline Segment data: range, source, and track.
"""

import flame

def segment(selection=None):
    """Gathers and returns Segment metadata."""
    def safe_val(val):
        if val is None: return None
        return str(val).strip("'")

    sel = flame.media_panel.get_selected_objects() if hasattr(flame.media_panel, 'get_selected_objects') else []
    selection_seg = [o for o in sel if str(type(o)).count('Segment')]
    seg = selection_seg[0] if selection_seg else None

    if not seg:
        data = {"error": "No Segment selected"}
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
    
    return data

if __name__ == "__main__":
    import json
    print(json.dumps(segment(), indent=4))
