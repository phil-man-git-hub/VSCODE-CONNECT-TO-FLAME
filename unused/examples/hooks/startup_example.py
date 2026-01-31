"""Example startup hook that exercises basic Flame APIs.

This module is safe to import and contains a small function `sample_startup` that
returns a simple dict so it can be used by smoke tests executed via the listener.
"""

def sample_startup():
    # Minimal, non-destructive operation
    return {'hook': 'startup', 'status': 'ok'}


def get_version_info():
    try:
        import flame
        v = flame.get_version()
        return {'version': v}
    except Exception:
        return {'version': None}
