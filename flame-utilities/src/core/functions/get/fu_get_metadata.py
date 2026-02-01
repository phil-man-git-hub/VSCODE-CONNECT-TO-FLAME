"""
fu_get_metadata.py - Part of the FLAME-UTILITIES suite.
Gathers technical metadata and XML data for Flame objects.
"""

import flame

def metadata(selection):
    """Gathers technical metadata for the selected objects."""
    results = []
    for item in selection:
        # Basic metadata
        data = {
            "name": getattr(item, 'name', 'Unknown'),
            "type": str(type(item))
        }
        
        # If it's a clip-like object
        if hasattr(item, 'width'):
            data.update({
                "width": item.width,
                "height": item.height,
                "aspect_ratio": getattr(item, 'aspect_ratio', 'N/A')
            })
            
        results.append(data)
        
    return results
