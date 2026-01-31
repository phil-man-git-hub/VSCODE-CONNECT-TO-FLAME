"""
fu_info.py - Part of the FLAME-UTILITIES suite.
Gathers high-level environment and project information from Autodesk Flame.
"""

import flame
import json
from fu_decorators import fu_action

@fu_action(menu="main_menu", path="FU / get / info")
@fu_action(menu="media_panel", path="FU / get / info")
def summary(selection=None):
    """Returns a basic summary of version and project names."""
    info_data = {
        "version": flame.get_version(),
        "project": flame.project.current_project.name,
        "user": flame.users.current_user.name,
        "home": flame.get_home_directory()
    }
    print("--- FLAME INFO SUMMARY ---")
    print(json.dumps(info_data, indent=4))
    return info_data
