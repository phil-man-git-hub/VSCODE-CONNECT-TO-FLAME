"""
fu_get_tags.py - Part of the FLAME-UTILITIES suite.
Gathers and manages tags and markers within Autodesk Flame.
"""

import flame

def tags(selection):
    """Lists all markers on the selected objects."""
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
        
    return all_markers
