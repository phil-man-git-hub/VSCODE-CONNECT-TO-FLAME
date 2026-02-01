"""
fu_get_tags.py - Part of the FLAME-UTILITIES suite.
Gathers and manages tags and markers within Autodesk Flame.
"""

import flame

def tags(selection):
    """Lists all markers on the selected objects."""
    all_markers = {}
    
    def safe_str(val):
        return str(val) if val is not None else ""

    for item in selection:
        # Use name or string representation as key
        item_key = getattr(item, 'name', str(item))
        markers_data = []
        
        # Check if object has markers (Clips, Sequences, Segments)
        if hasattr(item, 'markers'):
            for m in item.markers:
                # Extract frame location (handle PyTime or int)
                loc = m.location
                frame_idx = loc.frame if hasattr(loc, 'frame') else int(loc)
                
                markers_data.append({
                    "name": safe_str(m.name),
                    "comment": safe_str(m.comment),
                    "location_frame": frame_idx,
                    "colour": safe_str(m.colour)
                })
        
        all_markers[item_key] = markers_data
        
    return all_markers