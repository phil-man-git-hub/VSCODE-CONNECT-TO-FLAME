"""FU_Ignite: Project-Level Toolkit Activator

This script is the single entry point for the FLAME-UTILITIES suite.
It should be placed in '<project>/setups/python/'. 
It adds the toolkit (located in '<project>/setups/flame-utilities/') 
to the Python path and initializes the listener and menus.
"""

import os
import sys
import importlib.util

# 1. Identify the toolkit location (one level up, then into flame-utilities)
# Assuming this script is in /setups/python/
here = os.path.dirname(__file__)
setups_dir = os.path.dirname(here)
utilities_path = os.path.join(setups_dir, 'flame-utilities')

if os.path.exists(utilities_path):
    # 2. Add the toolkit folder to sys.path
    if utilities_path not in sys.path:
        sys.path.append(utilities_path)
    
    # 3. Import and execute the init logic
    # We use fu_eavesdrop_init.py as the secondary loader
    init_script = os.path.join(utilities_path, 'fu_eavesdrop_init.py')
    if os.path.exists(init_script):
        try:
            print(f"[fu_ignite] Activating toolkit at: {utilities_path}")
            spec = importlib.util.spec_from_file_location("fu_init", init_script)
            fu_init = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(fu_init)
        except Exception as e:
            print(f"[fu_ignite] Error igniting toolkit: {str(e)}")
    else:
        print(f"[fu_ignite] Error: fu_eavesdrop_init.py not found in {utilities_path}")
else:
    print(f"[fu_ignite] Error: flame-utilities folder not found at {utilities_path}")
