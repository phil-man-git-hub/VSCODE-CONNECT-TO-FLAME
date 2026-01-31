"""
Clip Inspector. Retrieves Identity, Format, Resolution, and Colour via Python and Wiretap XML.
"""

import flame
import json
import subprocess
import xml.etree.ElementTree as ET

def safe_val(val):
    if val is None: return None
    return str(val).strip("'")

selection = [o for o in flame.media_panel.selected_objects if str(type(o)).count('Clip')]
c = selection[0] if selection else None

if not c:
    print(json.dumps({"error": "No Clip selected"}, indent=2))
else:
    node_id = safe_val(c.get_wiretap_node_id()) if hasattr(c, 'get_wiretap_node_id') else None
    data = {
        'name': safe_val(c.name),
        'duration': c.duration.frame if hasattr(c.duration, 'frame') else str(c.duration),
        'width': c.width,
        'height': c.height,
        'bit_depth': c.bit_depth,
        'wiretap_node_id': node_id,
        'xml': {}
    }

    if node_id:
        tool = '/opt/Autodesk/wiretap/tools/current/wiretap_get_metadata'
        try:
            res = subprocess.run([tool, '-n', node_id, '-m', 'XML'], capture_output=True, text=True, timeout=5)
            if res.returncode == 0:
                root = ET.fromstring(res.stdout)
                for child in root:
                    if child.text:
                        data['xml'][child.tag] = child.text
        except: pass

    print(json.dumps(data, indent=2))
