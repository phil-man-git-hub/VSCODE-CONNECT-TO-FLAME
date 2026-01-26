"""Example: Confirmation Action Hook

Shows how to implement an action that requires explicit user confirmation
before committing a potentially-destructive operation.
"""


def preview_delete_selection():
    # Non-destructive preview
    return {'ok': True, 'preview': 'Will delete selected items (dry-run)'}


def delete_selection(confirm=False):
    if not confirm:
        return {'ok': False, 'error': 'confirm required'}
    try:
        import flame
        # Example: attempt to call a safe deletion API if present (this is illustrative)
        p = getattr(flame, 'project', None)
        if p and hasattr(p, 'delete_selected'):
            p.delete_selected()
            return {'ok': True, 'deleted': True}
        return {'ok': False, 'error': 'no-delete-api'}
    except Exception as e:
        return {'ok': False, 'error': repr(e)}
