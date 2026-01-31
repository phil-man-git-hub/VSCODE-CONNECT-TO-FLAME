"""FU_Loader: Project-Level Toolkit Activator

This script is intended to be placed in the root of a Flame project's 
'setups/python/' directory. It adds the 'flame-utilities' subfolder 
to the Python path and ignites the eavesdrop listener.
"""

import os
import sys
import importlib.util

# 1. Identify the absolute path to the archived flame-utilities folder
here = os.path.dirname(__file__)
utilities_path = os.path.join(here, 'flame-utilities')

if os.path.exists(utilities_path):
    # 2. Add the folder to sys.path so its modules can be imported
    if utilities_path not in sys.path:
        sys.path.append(utilities_path)
    
    # 3. Manually trigger the fu_eavesdrop_init logic
    init_script = os.path.join(utilities_path, 'fu_eavesdrop_init.py')
    if os.path.exists(init_script):
        try:
            print(f"[fu_loader] Activating archived toolkit at: {utilities_path}")
            # We import it as a module to trigger its execution
            spec = importlib.util.spec_from_file_location("fu_init", init_script)
            fu_init = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(fu_init)
        except Exception as e:
            print(f"[fu_loader] Error igniting toolkit: {str(e)}")
    else:
        print(f"[fu_loader] Error: fu_eavesdrop_init.py not found in {utilities_path}")
else:
    print(f"[fu_loader] Error: flame-utilities folder not found at {utilities_path}")
