"""
FU_Bootstrap: Central Path Infrastructure
-----------------------------------------
This utility resolves the FLAME-UTILITIES root directory and ensures 
all core subdirectories (src, lib, service) are in sys.path.

Usage:
    import fu_bootstrap
    # all fu_* modules are now importable
"""

import os
import sys

def setup():
    """
    Initializes the toolkit environment by injecting paths into sys.path.
    This function is idempotent and can be called safely multiple times.
    """
    if getattr(sys, '_fu_bootstrap_done', False):
        return
    
    # 1. Resolve Root (The folder containing this file)
    root = os.path.dirname(os.path.realpath(__file__))
    print(f"[fu_bootstrap] Setting up toolkit root: {root}")
    
    # 2. Define Subdirectories to inject
    subdirs = [
        root,
        os.path.join(root, 'src'),
        os.path.join(root, 'lib'),
        os.path.join(root, 'service'),
        os.path.join(root, 'lib', 'ai'),
    ]
    
    # 3. Inject into sys.path
    for d in subdirs:
        if os.path.exists(d) and d not in sys.path:
            sys.path.insert(0, d)
            
    # 4. Set a persistent flag to avoid redundant path math
    sys._fu_bootstrap_done = True
    sys._fu_root = root
    print("[fu_bootstrap] Path injection complete.")

# Execute setup on import
setup()

def get_root():
    """Returns the absolute path to the flame-utilities root."""
    return getattr(sys, '_fu_root', None)

def get_config_path(filename):
    """Utility to find a JSON config file in the config/ directory."""
    root = get_root()
    if root:
        path = os.path.join(root, 'config', filename)
        if os.path.exists(path):
            return path
    return None
