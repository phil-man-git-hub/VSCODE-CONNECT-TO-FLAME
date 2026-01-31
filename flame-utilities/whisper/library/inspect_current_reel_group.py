"""
Reel Group Inspector. Targets the first selected Reel Group in the Media Panel.
"""

import flame
import json

def safe_val(val):
    if val is None: return None
    return str(val).strip("'")

# Target selection or first available on desktop
selection = [o for o in flame.media_panel.selected_objects if str(type(o)).count('ReelGroup')]
rg = selection[0] if selection else flame.project.current_project.current_workspace.desktop.reel_groups[0]

data = {
    'name': safe_val(rg.name),
    'reels': [safe_val(r.name) for r in rg.reels],
    'wiretap_node_id': safe_val(rg.get_wiretap_node_id()) if hasattr(rg, 'get_wiretap_node_id') else None
}

print(json.dumps(data, indent=2))
