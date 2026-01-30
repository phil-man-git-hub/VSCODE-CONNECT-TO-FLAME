import os
import sys
import glob

def load_fu_plugins():
    """
    Scans the 'src/utils' directory for python files starting with 'fu_' 
    and imports them. This triggers the execution of any @fu_action decorators
    contained within them.
    """
    # Calculate the path to src/utils based on this file's location
    # This file is in src/utils/fu_loader.py
    current_dir = os.path.dirname(os.path.realpath(__file__))
    
    # We are already in src/utils, so we scan this directory
    # If we wanted to scan a sibling 'plugins' dir, we would adjust path.
    
    # Add src/core and src/utils to sys.path if not present, to ensure imports work
    src_core = os.path.join(os.path.dirname(current_dir), 'core')
    if src_core not in sys.path:
        sys.path.append(src_core)
    
    if current_dir not in sys.path:
        sys.path.append(current_dir)

    # Find all fu_*.py files
    plugin_files = glob.glob(os.path.join(current_dir, "fu_*.py"))
    
    for plugin_path in plugin_files:
        filename = os.path.basename(plugin_path)
        if filename == "__init__.py" or filename == "fu_loader.py":
            continue
            
        module_name = os.path.splitext(filename)[0]
        
        # Import the module
        try:
            if module_name in sys.modules:
                 # Reload if already loaded (useful for dev)
                 # Note: Python 3 requires importlib for reload
                 # but Flame's python environment is standard.
                 pass 
            else:
                __import__(module_name)
        except Exception as e:
            print(f"Flame Utilities: Failed to load plugin '{module_name}': {e}")
