"""
fu_info.py - Part of the FLAME-UTILITIES suite.
Gathers high-level environment and project information from Autodesk Flame.
"""

import flame

def get_flame_info():
    """Returns a dictionary containing version and project information."""
    return {
        "version": flame.get_version(),
        "project": flame.project.current_project.name,
        "user": flame.users.current_user.name,
        "home": flame.get_home_directory()
    }
