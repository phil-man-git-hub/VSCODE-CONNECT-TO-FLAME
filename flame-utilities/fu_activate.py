"""FU_Activate: Project-Level Toolkit Activator

This script is the single entry point for the FLAME-UTILITIES suite.
It leverages fu_bootstrap to setup the environment and then ignites
the background services and UI hooks.
"""

import sys
import os
import importlib.util

# 1. Bootstrapping
# We assume fu_bootstrap is in the same directory as this script
try:
    import fu_bootstrap
except ImportError:
    # If not in path, try relative discovery
    here = os.path.dirname(os.path.realpath(__file__))
    if here not in sys.path:
        sys.path.append(here)
    import fu_bootstrap

# 2. Initialization
def ignite():
    if getattr(sys, '_fu_initialized', False):
        return
    
    sys._fu_initialized = True
    root = fu_bootstrap.get_root()
    
    init_script = os.path.join(root, 'service', 'fu_eavesdrop_init.py')
    if os.path.exists(init_script):
        try:
            print(f"[fu_activate] Igniting toolkit from: {init_script}")
            spec = importlib.util.spec_from_file_location("fu_init", init_script)
            fu_init = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(fu_init)
        except Exception as e:
            print(f"[fu_activate] Critical Error during ignition: {e}")
    else:
        print(f"[fu_activate] Error: service/fu_eavesdrop_init.py not found in {root}")

if __name__ == "__main__":
    ignite()
