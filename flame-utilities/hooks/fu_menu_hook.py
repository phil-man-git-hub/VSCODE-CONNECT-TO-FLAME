import sys
import os

# ------------------------------------------------------------------------------
# BOOTSTRAP
# ------------------------------------------------------------------------------
# We need to ensure flame-utilities/src/core and src/utils are in sys.path
# because this hook file is in flame-utilities/hooks/

HOOK_DIR = os.path.dirname(os.path.realpath(__file__))
FLAME_UTILS_ROOT = os.path.dirname(HOOK_DIR)
SRC_CORE = os.path.join(FLAME_UTILS_ROOT, 'src', 'core')
SRC_UTILS = os.path.join(FLAME_UTILS_ROOT, 'src', 'utils')

if SRC_CORE not in sys.path:
    sys.path.append(SRC_CORE)

if SRC_UTILS not in sys.path:
    sys.path.append(SRC_UTILS)

# ------------------------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------------------------
try:
    from fu_menu_registry import FuMenuRegistry
    import fu_loader
except ImportError as e:
    print(f"Flame Utilities Error: Could not import core modules. {e}")
    FuMenuRegistry = None

# ------------------------------------------------------------------------------
# INITIALIZATION
# ------------------------------------------------------------------------------
# Trigger the loading of all utility scripts/plugins to register their actions
if FuMenuRegistry:
    fu_loader.load_fu_plugins()
    registry = FuMenuRegistry()
else:
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
