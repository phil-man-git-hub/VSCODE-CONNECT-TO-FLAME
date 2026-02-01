"""
fu_get_info_sequence.py - Part of the FLAME-UTILITIES suite.
Sequence Inspector. Retrieves Tracks, Versions, and duration.
"""

import flame

def sequence(selection=None):
    """Gathers and returns Sequence metadata."""
    def safe_val(val):
        if val is None: return None
        return str(val).strip("'")

    sel = flame.media_panel.get_selected_objects() if hasattr(flame.media_panel, 'get_selected_objects') else []
    selection_s = [o for o in sel if str(type(o)).count('Sequence')]
    s = selection_s[0] if selection_s else None

    if not s:
        data = {"error": "No Sequence selected"}
    else:
        data = {
            'name': safe_val(s.name),
            'duration': s.duration.frame if hasattr(s.duration, 'frame') else str(s.duration),
            'versions': [safe_val(v.name) for v in s.versions] if hasattr(s, 'versions') and s.versions else [],
            'video_tracks': len(s.video_tracks) if hasattr(s, 'video_tracks') and s.video_tracks else 0,
            'audio_tracks': len(s.audio_tracks) if hasattr(s, 'audio_tracks') and s.audio_tracks else 0,
            'wiretap_node_id': safe_val(s.get_wiretap_node_id()) if hasattr(s, 'get_wiretap_node_id') else None
        }
    
    return data
