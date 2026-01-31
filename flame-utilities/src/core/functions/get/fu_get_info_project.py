"""
fu_get_info_project.py - Part of the FLAME-UTILITIES suite.
Comprehensive project inspector. Retrieves Identity, Paths, IDs, Resolution, Config, Proxy, HDR, and Colour settings via Python API and Wiretap XML.
"""

import flame
import subprocess
import xml.etree.ElementTree as ET
import json
from fu_decorators import fu_action

@fu_action(menu="main_menu", path="FU / get / info")
@fu_action(menu="media_panel", path="FU / get / info")
def project(selection=None):
    """Gathers and returns comprehensive project metadata."""
    # 1. Gather Basic Python Info
    p = flame.project.current_project
    w = p.current_workspace

    def safe_val(val):
        if val is None: return None
        return str(val).strip("'")

    data = {
        'name': safe_val(p.name),
        'nickname': safe_val(p.nickname),
        'description': safe_val(p.description),
        'ids': {
            'wiretap_node_id': safe_val(p.get_wiretap_node_id()) if hasattr(p, 'get_wiretap_node_id') else None,
            'wiretap_storage_id': safe_val(p.get_wiretap_storage_id()) if hasattr(p, 'get_wiretap_storage_id') else None,
        },
        'paths': {
            'project_folder': safe_val(p.project_folder),
            'setups_folder': safe_val(p.setups_folder),
            'media_folder': safe_val(p.media_folder),
        },
        'workspace': {
            'name': safe_val(w.name),
            'desktop_name': safe_val(w.desktop.name) if hasattr(w, 'desktop') else None
        },
        'parameters': {
            'resolution': 'Unknown',
            'frame_rate': 'Unknown',
            'bit_depth': 'Unknown',
            'start_frame': 'Unknown',
            'aspect_ratio': 'Unknown',
            'field_dominance': 'Unknown'
        },
        'extended_metadata': {
            'version': 'Unknown',
            'creation_date': 'Unknown',
            'proxy': {},
            'hdr': {},
            'intermediates_profile': 'Unknown'
        }
    }

    # 2. Extract Wiretap XML
    tool_path = '/opt/Autodesk/wiretap/tools/current/wiretap_get_metadata'
    node_id = data['ids']['wiretap_node_id']

    if node_id:
        cmd = [tool_path, '-n', node_id, '-m', 'XML']
        try:
            res = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
            if res.returncode == 0 and res.stdout.strip():
                if res.stdout.strip().startswith('<'):
                    try:
                        root = ET.fromstring(res.stdout)
                        
                        def get_xml(element, tag):
                            found = element.find(tag)
                            return found.text if found is not None else None

                        # Core Params
                        width = get_xml(root, 'FrameWidth')
                        height = get_xml(root, 'FrameHeight')
                        if width and height:
                            data['parameters']['resolution'] = f'{width}x{height}'
                        
                        data['parameters']['frame_rate'] = get_xml(root, 'FrameRate')
                        data['parameters']['bit_depth'] = get_xml(root, 'FrameDepth')
                        data['parameters']['start_frame'] = get_xml(root, 'DefaultStartFrame')
                        data['parameters']['aspect_ratio'] = get_xml(root, 'AspectRatio')
                        data['parameters']['field_dominance'] = get_xml(root, 'FieldDominance')
                        
                        # Colour
                        cp = get_xml(root, 'ColourPolicyName')
                        cf = get_xml(root, 'OCIOConfigFile')
                        if cp: data['colour_policy'] = cp
                        if cf: data['colour_config_file'] = cf
                        
                        # Extended Metadata
                        data['extended_metadata']['version'] = get_xml(root, 'Version')
                        data['extended_metadata']['creation_date'] = get_xml(root, 'CreationDate')
                        data['extended_metadata']['intermediates_profile'] = get_xml(root, 'IntermediatesProfile')
                        
                        # Proxy
                        data['extended_metadata']['proxy'] = {
                            'width': get_xml(root, 'ProxyWidth'),
                            'depth': get_xml(root, 'ProxyDepth'),
                            'quality': get_xml(root, 'ProxyQuality'),
                            'min_size': get_xml(root, 'ProxyMinFrameSize')
                        }
                        
                        # HDR
                        data['extended_metadata']['hdr'] = {
                            'mode': get_xml(root, 'HdrMode'),
                            'cmu_type': get_xml(root, 'HdrCmuType'),
                            'mastering_id': get_xml(root, 'HdrMasteringId')
                        }

                    except Exception as xml_err:
                        data['xml_error'] = str(xml_err)
                
        except Exception as e:
            data['wiretap_error'] = str(e)

    return data
