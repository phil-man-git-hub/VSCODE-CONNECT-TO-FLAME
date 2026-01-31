"""
fu_tags.py - Part of the FLAME-UTILITIES suite.
Gathers and manages tags and markers within Autodesk Flame.
"""

import flame

def list_markers(clip):
    """Lists all markers on a given PyClip or PySequence."""
    markers = []
    for marker in clip.markers:
        markers.append({
            "name": marker.name,
            "comment": marker.comment,
            "location": marker.location,
            "colour": marker.colour
        })
    return markers
