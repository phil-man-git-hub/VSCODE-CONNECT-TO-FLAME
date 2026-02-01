"""Startup hook to be placed inside Flame project `setups/python/`.

This file is intended to be copied into Flame's `setups/python/` directory and
will be executed by Flame on startup. It spawns the listener in a background
thread so it doesn't block Flame's UI thread.
"""

# Version metadata for easier diagnosis of which startup hook is active
__version__ = '0.0.1'

import threading
import os
import sys

# Ensure the utilities directory is in path
utilities_dir = os.path.dirname(__file__)
if utilities_dir not in sys.path:
    sys.path.append(utilities_dir)

try:
    import flame  # type: ignore
except Exception:
    flame = None

# Announce our presence & version so deployed startup hooks are easy to identify
try:
    print(f"fu_eavesdrop_init.py version {__version__}")
except Exception:
    pass

# Import the local fu_eavesdrop module (now in same directory)
try:
    from fu_eavesdrop import initialize_eavesdrop
    import hooks.fu_menu_hook
except Exception as e:
    # If we can't import the full listener, abort gracefully
    print(f'Failed to initialize toolkit: {e}')
else:
    # Run the TCP listener in a daemon thread so it won't block Flame shutdown
    t = threading.Thread(target=initialize_eavesdrop, kwargs={}, daemon=True)
    t.start()
    print(f'FU_Eavesdrop startup hook started in background thread (version {__version__})')
