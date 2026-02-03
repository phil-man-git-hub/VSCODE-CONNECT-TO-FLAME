"""Startup hook to be placed inside Flame project `setups/python/`.

This file is intended to be executed by fu_activate. 
It spawns the listener in a background thread and registers UI hooks.
"""

# Version metadata
__version__ = '0.1.0'

import threading
import sys
import os

# 1. Bootstrap
try:
    import fu_bootstrap
except ImportError:
    # Fallback discovery
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    import fu_bootstrap

# 2. Initialization
def initialize():
    # Announce our presence & version
    print(f"fu_eavesdrop_init.py version {__version__} (Ignited)")

    try:
        from fu_eavesdrop import initialize_eavesdrop
        import fu_menu_hook
        
        # Run the TCP listener in a daemon thread
        t = threading.Thread(target=initialize_eavesdrop, kwargs={}, daemon=True)
        t.start()
        print(f'FU_Eavesdrop service started in background (v{__version__})')
    except Exception as e:
        print(f'Failed to initialize toolkit services: {e}')

if __name__ == "fu_init" or __name__ == "__main__":
    initialize()
