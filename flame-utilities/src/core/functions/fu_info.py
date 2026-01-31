"""
fu_info.py - Part of the FLAME-UTILITIES suite.
Gathers high-level environment and project information from Autodesk Flame.
"""

import flame
from fu_decorators import fu_action

@fu_action(menu="main_menu", path="FU / get")
@fu_action(menu="media_panel", path="FU / get")
def info(selection):
    """Returns a dictionary containing version and project information."""
    import json
    info_data = {
        "version": flame.get_version(),
        "project": flame.project.current_project.name,
        "user": flame.users.current_user.name,
        "home": flame.get_home_directory()
    }
    print("--- FLAME INFO ---")
    print(json.dumps(info_data, indent=4))
    return info_data
