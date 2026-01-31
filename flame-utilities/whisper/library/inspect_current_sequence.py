"""
Sequence Inspector. Retrieves Tracks, Versions, and duration.
"""

import flame
import json

def safe_val(val):
    if val is None: return None
    return str(val).strip("'")

selection = [o for o in flame.media_panel.selected_objects if str(type(o)).count('Sequence')]
s = selection[0] if selection else None

if not s:
    print(json.dumps({"error": "No Sequence selected"}, indent=2))
else:
    data = {
        'name': safe_val(s.name),
        'duration': s.duration.frame if hasattr(s.duration, 'frame') else str(s.duration),
        'versions': [safe_val(v.name) for v in s.versions] if hasattr(s, 'versions') else [],
        'video_tracks': len(s.video_tracks) if hasattr(s, 'video_tracks') else 0,
        'audio_tracks': len(s.audio_tracks) if hasattr(s, 'audio_tracks') else 0,
        'wiretap_node_id': safe_val(s.get_wiretap_node_id()) if hasattr(s, 'get_wiretap_node_id') else None
    }
    print(json.dumps(data, indent=2))
