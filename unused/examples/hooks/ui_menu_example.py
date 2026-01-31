"""Example UI Menu Hook

This module demonstrates how to declare a menu structure and register it with
Flame if the Flame UI API is present. All operations are guarded so importing
or running these functions outside Flame is safe for testing.
"""

MENU_DEF = [
    {"name": "Examples", "items": [
        {"name": "List Clips", "action": "list_clips"},
        {"name": "Show Timeline Ranges", "action": "show_ranges"},
    ]}
]


def register_menu():
    """Attempt to register the menu in Flame's UI if possible.

    Returns a dict describing what it did. Does not raise if Flame is unavailable.
    """
    try:
        import flame
        ui = getattr(flame, 'ui', None)
        # Many Flame installations expose UI functions differently. Take a best-effort approach.
        if ui and hasattr(ui, 'register_menu'):
            ui.register_menu(MENU_DEF)
            return {'ok': True, 'registered': True}
        else:
            # No registration API: return the menu description so the caller can display it
            return {'ok': True, 'registered': False, 'menu': MENU_DEF}
    except Exception as e:
        return {'ok': False, 'error': repr(e)}


def menu_action(action_name, *, confirm=False):
    """Perform a menu action. If `confirm` is True we attempt to show a confirmation dialog.

    This is a thin wrapper intended for examples; real hooks should implement
    user-facing dialogs inside Flame's main thread.
    """
    try:
        # confirmation simulation
        if confirm:
            try:
                import flame
                ui = getattr(flame, 'ui', None)
                if ui and hasattr(ui, 'confirm'):
                    ok = ui.confirm(f"Run {action_name}?")
                    if not ok:
                        return {'ok': False, 'confirmed': False}
            except Exception:
                # if we can't show dialog, treat confirm=True as a veto unless overridden
                return {'ok': False, 'error': 'confirm-unavailable'}

        # dispatch to safe snippets
        if action_name == 'list_clips':
            from examples.snippets.clip_snippet import list_clips_in_current_timeline
            return {'ok': True, 'result': list_clips_in_current_timeline()}
        if action_name == 'show_ranges':
            from examples.snippets.timeline_snippet import timeline_frame_ranges
            return {'ok': True, 'result': timeline_frame_ranges()}
        return {'ok': False, 'error': 'unknown-action'}
    except Exception as e:
        return {'ok': False, 'error': repr(e)}
