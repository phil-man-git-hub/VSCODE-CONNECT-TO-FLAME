"""
fu_get.py - Orchestrator for all 'get' functions.
Registers the sub-menu hierarchy and delegates to individual logic scripts.
"""

import flame
import json
from fu_decorators import fu_action

def _display(title, data):
    """Utility to print and return formatted data."""
    print(f"--- {title} ---")
    print(json.dumps(data, indent=4))
    return data

# --- Top Level Get Actions ---

@fu_action(menu="media_panel", path="FU / get")
def metadata(selection):
    """Gathers technical metadata for the selected objects."""
    from get.fu_get_metadata import metadata as logic
    return _display("METADATA", logic(selection))

@fu_action(menu="media_panel", path="FU / get")
@fu_action(menu="timeline", path="FU / get")
def tags(selection):
    """Lists all markers on the selected objects."""
    from get.fu_get_tags import tags as logic
    return _display("TAGS/MARKERS", logic(selection))

# --- Info Sub-Menu Actions ---

@fu_action(menu="main_menu", path="FU / get / info")
@fu_action(menu="media_panel", path="FU / get / info")
def summary(selection=None):
    """Basic project/version summary."""
    info_data = {
        "version": flame.get_version(),
        "project": flame.project.current_project.name,
        "user": flame.users.current_user.name,
        "home": flame.get_home_directory()
    }
    return _display("FLAME INFO SUMMARY", info_data)

@fu_action(menu="main_menu", path="FU / get / info")
@fu_action(menu="media_panel", path="FU / get / info")
def project(selection=None):
    """Comprehensive project metadata via Wiretap XML."""
    from get.fu_get_info_project import project as logic
    return _display("PROJECT METADATA", logic())

@fu_action(menu="main_menu", path="FU / get / info")
@fu_action(menu="media_panel", path="FU / get / info")
def workspace(selection=None):
    """Active Workspace and Desktop inventory."""
    from get.fu_get_info_workspace import workspace as logic
    return _display("WORKSPACE INFO", logic())

@fu_action(menu="main_menu", path="FU / get / info")
@fu_action(menu="media_panel", path="FU / get / info")
def desktop(selection=None):
    """Desktop content inventory (Reels, Batches)."""
    from get.fu_get_info_desktop import desktop as logic
    return _display("DESKTOP INFO", logic())

@fu_action(menu="main_menu", path="FU / get / info")
@fu_action(menu="media_panel", path="FU / get / info")
def reel_group(selection=None):
    """Selected or current Reel Group details."""
    from get.fu_get_info_reel_group import reel_group as logic
    return _display("REEL GROUP INFO", logic())

@fu_action(menu="media_panel", path="FU / get / info")
def reel(selection=None):
    """Selected Reel details."""
    from get.fu_get_info_reel import reel as logic
    return _display("REEL INFO", logic())

@fu_action(menu="media_panel", path="FU / get / info")
@fu_action(menu="timeline", path="FU / get / info")
def clip(selection=None):
    """Selected Clip technical metadata."""
    from get.fu_get_info_clip import clip as logic
    return _display("CLIP INFO", logic())

@fu_action(menu="media_panel", path="FU / get / info")
@fu_action(menu="timeline", path="FU / get / info")
def sequence(selection=None):
    """Selected Sequence track and version inventory."""
    from get.fu_get_info_sequence import sequence as logic
    return _display("SEQUENCE INFO", logic())

@fu_action(menu="timeline", path="FU / get / info")
def segment(selection=None):
    """Selected Timeline Segment range and source metadata."""
    from get.fu_get_info_segment import segment as logic
    return _display("SEGMENT INFO", logic())

@fu_action(menu="media_panel", path="FU / get / info")
def library(selection=None):
    """Selected Library inventory."""
    from get.fu_get_info_library import library as logic
    return _display("LIBRARY INFO", logic())

@fu_action(menu="media_panel", path="FU / get / info")
def shared_library(selection=None):
    """Selected Shared Library status and locks."""
    from get.fu_get_info_shared_library import shared_library as logic
    return _display("SHARED LIBRARY INFO", logic())

@fu_action(menu="media_panel", path="FU / get / info")
@fu_action(menu="batch", path="FU / get / info")
def batch_group(selection=None):
    """Selected or active Batch Group iteration details."""
    from get.fu_get_info_batchgroup import batchgroup as logic
    return _display("BATCH GROUP INFO", logic())
