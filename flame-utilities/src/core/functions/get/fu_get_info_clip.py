"""
fu_get_info_clip.py - Part of the FLAME-UTILITIES suite.
Clip Inspector. Retrieves Identity, Format, Resolution, and Colour via Python and Wiretap XML.
"""

import flame
import subprocess
import os
import xml.etree.ElementTree as ET

def clip(selection=None):
    """Gathers and returns Clip metadata."""
    def safe_val(val):
        if val is None: return None
        return str(val).strip("'")

    sel = flame.media_panel.get_selected_objects() if hasattr(flame.media_panel, 'get_selected_objects') else []
    selection_c = [o for o in sel if str(type(o)).count('Clip')]
    c = selection_c[0] if selection_c else None

    if not c:
        data = {"error": "No Clip selected"}
    else:
        node_id = safe_val(c.get_wiretap_node_id()) if hasattr(c, 'get_wiretap_node_id') else None
        data = {
            'name': safe_val(c.name),
            'duration': c.duration.frame if hasattr(c.duration, 'frame') else str(c.duration),
            'width': getattr(c, 'width', 0),
            'height': getattr(c, 'height', 0),
            'bit_depth': getattr(c, 'bit_depth', 0),
            'wiretap_node_id': node_id,
            'xml': {}
        }

        if node_id:
            tool = '/opt/Autodesk/wiretap/tools/current/wiretap_get_metadata'
            if os.path.exists(tool):
                try:
                    res = subprocess.run([tool, '-n', node_id, '-m', 'XML'], capture_output=True, text=True, timeout=5)
                    if res.returncode == 0:
                        root = ET.fromstring(res.stdout)
                        for child in root:
                            if child.text:
                                data['xml'][child.tag] = child.text
                except: pass
    
    return data

if __name__ == "__main__":
    import json
    print(json.dumps(clip(), indent=4))
