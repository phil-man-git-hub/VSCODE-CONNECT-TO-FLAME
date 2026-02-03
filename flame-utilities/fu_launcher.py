"""FU_Launcher: Project-Level Toolkit Activator
-------------------------------------------
This script is the single entry point for the FLAME-UTILITIES suite.
It is typically deployed as 'fu_activate.py' in the parent directory.
"""

import sys
import os
import importlib.util

def ignite():
    # 1. Identify Toolkit Root
    # This script might be in setups/python/ OR setups/python/flame-utilities/
    here = os.path.dirname(os.path.realpath(__file__))
    
    if os.path.exists(os.path.join(here, 'fu_bootstrap.py')):
        # We are inside the toolkit
        toolkit_root = here
    else:
        # We are likely in the parent directory
        toolkit_root = os.path.join(here, 'flame-utilities')

    if not os.path.exists(toolkit_root):
        print(f"[fu_launcher] Error: Toolkit root not found at {toolkit_root}")
        return

    # 2. Setup Path
    if toolkit_root not in sys.path:
        sys.path.insert(0, toolkit_root)

    # 3. Bootstrap
    try:
        import fu_bootstrap
        fu_bootstrap.setup()
    except Exception as e:
        print(f"[fu_launcher] Error during bootstrap: {e}")
        return

    # 4. Initialize Services (Idempotent)
    if getattr(sys, '_fu_initialized', False):
        return
    
    sys._fu_initialized = True
    
    init_script = os.path.join(toolkit_root, 'service', 'fu_eavesdrop_init.py')
    if os.path.exists(init_script):
        try:
            print(f"[fu_launcher] Igniting toolkit from: {init_script}")
            spec = importlib.util.spec_from_file_location("fu_init", init_script)
            fu_init = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(fu_init)
        except Exception as e:
            print(f"[fu_launcher] Critical Error during ignition: {e}")
    else:
        print(f"[fu_launcher] Error: service/fu_eavesdrop_init.py not found")

# Trigger ignition immediately on load (Standard Flame Hook behavior)
ignite()