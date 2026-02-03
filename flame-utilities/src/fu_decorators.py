import fu_bootstrap
from fu_menu_registry import FuMenuRegistry

def fu_action(menu="media_panel", path="Flame Utilities", is_visible=None, is_enabled=None, min_version=None, max_version=None, wait_cursor=None):
    """
    Decorator to register a Python function as a Flame Contextual Menu action.

    Args:
        menu (str): The target menu. One of: 
                    'media_panel', 'main_menu', 'timeline', 'batch', 
                    'mediahub_files', 'mediahub_projects', 'mediahub_archives', 'action'.
        path (str): The menu path (e.g., "Flame Utilities / My Tool").
                    The first segment is the Menu Group.
        is_visible (func): Optional scoping function returning Bool.
        is_enabled (func): Optional scoping function returning Bool.
        min_version (str): Minimum Flame version (e.g. "2023.1").
        max_version (str): Maximum Flame version.
        wait_cursor (bool): Whether to show the wait cursor during execution.
    """
    def decorator(func):
        registry = FuMenuRegistry()
        
        # Build definition object
        action_def = {
            "name": func.__name__, # Default name, can be overridden if we added a 'name' arg
            "execute": func,
            "path": path
        }
        
        # We might want to allow the function name to be pretty-printed or explicit
        # For this V1, we use the function name, but replacing underscores could be nice.
        # Let's clean it up slightly:
        action_def["name"] = func.__name__.replace('_', ' ').title()

        if is_visible:
            action_def["isVisible"] = is_visible
        if is_enabled:
            action_def["isEnabled"] = is_enabled
        if min_version:
            action_def["minimumVersion"] = min_version
        if max_version:
            action_def["maximumVersion"] = max_version
        if wait_cursor is not None:
            action_def["waitCursor"] = wait_cursor

        # Register
        registry.register(menu, action_def)

        return func
    return decorator
