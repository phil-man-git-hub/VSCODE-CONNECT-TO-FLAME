"""Example Safe Toggle Hook

Provides a simple toggled feature flag that can be read or set. Persists the
flag under /tmp so it's safe without flame-specific storage.
"""

import os

_FLAG_FILE = os.path.join('/tmp', 'flame_example_toggle.flag')


def get_toggle():
    try:
        if os.path.exists(_FLAG_FILE):
            return {'ok': True, 'enabled': True}
        return {'ok': True, 'enabled': False}
    except Exception as e:
        return {'ok': False, 'error': repr(e)}


def set_toggle(enabled: bool):
    try:
        if enabled:
            open(_FLAG_FILE, 'w').write('1')
            return {'ok': True, 'enabled': True}
        else:
            try:
                os.remove(_FLAG_FILE)
            except FileNotFoundError:
                pass
            return {'ok': True, 'enabled': False}
    except Exception as e:
        return {'ok': False, 'error': repr(e)}
