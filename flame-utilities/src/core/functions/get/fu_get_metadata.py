"""
fu_get_metadata.py - Part of the FLAME-UTILITIES suite.
Gathers technical metadata and XML data for Flame objects via Python and Wiretap.
"""

import flame
import subprocess
import xml.etree.ElementTree as ET
import os

def metadata(selection):
    """Gathers technical metadata for the selected objects."""
    results = []
    
    # Path to Wiretap metadata tool
    tool_path = '/opt/Autodesk/wiretap/tools/current/wiretap_get_metadata'
    
    for item in selection:
        # 1. Basic Python API metadata
        data = {
            "name": getattr(item, 'name', 'Unknown'),
            "type": str(type(item))
        }
        
        # If it's a clip-like object, get basic resolution/depth
        if hasattr(item, 'width'):
            data.update({
                "width": getattr(item, 'width', 0),
                "height": getattr(item, 'height', 0),
                "aspect_ratio": getattr(item, 'aspect_ratio', 'N/A'),
                "bit_depth": getattr(item, 'bit_depth', 'Unknown'),
                "duration": item.duration.frame if hasattr(item, 'duration') and hasattr(item.duration, 'frame') else str(getattr(item, 'duration', 'N/A'))
            })
            
        # 2. Wiretap XML metadata (Deep Inspection)
        if hasattr(item, 'get_wiretap_node_id'):
            node_id = item.get_wiretap_node_id()
            if node_id and os.path.exists(tool_path):
                try:
                    cmd = [tool_path, '-n', str(node_id), '-m', 'XML']
                    res = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
                    if res.returncode == 0 and res.stdout.strip():
                        root = ET.fromstring(res.stdout)
                        xml_data = {}
                        for child in root:
                            if child.text:
                                xml_data[child.tag] = child.text
                        data['wiretap_xml'] = xml_data
                except Exception as e:
                    data['wiretap_error'] = str(e)
            
        results.append(data)
        
    return results