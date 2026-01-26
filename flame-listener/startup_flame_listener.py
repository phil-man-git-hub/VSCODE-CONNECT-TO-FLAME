"""Startup hook to be placed inside Flame project `setups/python/`.

This file is intended to be copied into Flame's `setups/python/` directory and
will be executed by Flame on startup. It spawns the listener in a background
thread so it doesn't block Flame's UI thread.
"""

import threading
try:
    import flame  # type: ignore
except Exception:
    flame = None

# Import the local flame_listener module (assumes it's copied alongside this file)
try:
    from flame_listener import start_server
except Exception:
    # If we can't import the full listener, abort gracefully
    print('Failed to import flame_listener; remote execution bridge not started')
else:
    # Run the TCP listener in a daemon thread so it won't block Flame shutdown
    t = threading.Thread(target=start_server, kwargs={}, daemon=True)
    t.start()
    print('Flame listener startup hook started in background thread')
