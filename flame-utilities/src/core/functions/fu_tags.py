"""
fu_tags.py - Part of the FLAME-UTILITIES suite.
Gathers and manages tags and markers within Autodesk Flame.
"""

import flame
from fu_decorators import fu_action

@fu_action(menu="media_panel", path="FU / get")
@fu_action(menu="timeline", path="FU / get")
def tags(selection):
    """Lists all markers on the selected objects."""
    import json
    all_markers = {}
    for item in selection:
        item_name = getattr(item, 'name', str(item))
        markers = []
        if hasattr(item, 'markers'):
            for marker in item.markers:
                markers.append({
                    "name": marker.name,
                    "comment": marker.comment,
                    "location": marker.location,
                    "colour": marker.colour
                })
        all_markers[item_name] = markers
        
    print("--- TAGS/MARKERS ---")
    print(json.dumps(all_markers, indent=4))
    return all_markers
