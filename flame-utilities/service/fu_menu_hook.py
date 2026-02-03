"""
FU_Menu_Hook: Contextual Menu Registration
------------------------------------------
Registers toolkit actions into Flame's UI menus (Media Panel, Timeline, Batch, etc.)
Leverages the FuMenuRegistry singleton and auto-loads plugins from src/.
"""

import sys
import os
import fu_bootstrap

# ------------------------------------------------------------------------------
# IMPORTS & INITIALIZATION
# ------------------------------------------------------------------------------
try:
    from fu_menu_registry import FuMenuRegistry
    import fu_plugin_loader as fu_loader
    
    # Trigger the loading of all utility scripts/plugins to register their actions
    fu_loader.load_fu_plugins()
    registry = FuMenuRegistry()
    
except ImportError as e:
    print(f"Flame Utilities Error: Could not initialize menu registry. {e}")
    registry = None

# ------------------------------------------------------------------------------
# FLAME HOOKS
# ------------------------------------------------------------------------------

def get_media_panel_custom_ui_actions():
    if registry:
        return registry.get_actions_for_hook("media_panel")
    return []

def get_main_menu_custom_ui_actions():
    if registry:
        return registry.get_actions_for_hook("main_menu")
    return []

def get_timeline_custom_ui_actions():
    if registry:
        return registry.get_actions_for_hook("timeline")
    return []

def get_batch_custom_ui_actions():
    if registry:
        return registry.get_actions_for_hook("batch")
    return []

def get_mediahub_files_custom_ui_actions():
    if registry:
        return registry.get_actions_for_hook("mediahub_files")
    return []

def get_mediahub_projects_custom_ui_actions():
    if registry:
        return registry.get_actions_for_hook("mediahub_projects")
    return []

def get_mediahub_archives_custom_ui_actions():
    if registry:
        return registry.get_actions_for_hook("mediahub_archives")
    return []

def get_action_custom_ui_actions():
    if registry:
        return registry.get_actions_for_hook("action")
    return []
