"""
fu_metadata.py - Part of the FLAME-UTILITIES suite.
Gathers technical metadata and XML data for Flame objects.
"""

import flame
import subprocess
from fu_decorators import fu_action

@fu_action(menu="media_panel", path="FU / get")
def metadata(selection):
    """Gathers technical metadata for the selected objects."""
    import json
    results = []
    for item in selection:
        # Basic metadata for now
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
        
    print("--- METADATA ---")
    print(json.dumps(results, indent=4))
    return results
