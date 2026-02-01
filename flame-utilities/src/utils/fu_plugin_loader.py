import os
import sys
import glob

def load_fu_plugins():
    """
    Scans the 'src/utils' and 'src/core/functions' directories for python files 
    starting with 'fu_' and imports them. This triggers the execution of any 
    @fu_action decorators contained within them.
    """
    current_dir = os.path.dirname(os.path.realpath(__file__)) # src/utils
    src_root = os.path.dirname(current_dir) # src
    
    functions_dir = os.path.join(src_root, 'core', 'functions')
    get_dir = os.path.join(functions_dir, 'get')
    
    # Locations to scan
    scan_paths = [current_dir, functions_dir, get_dir]
    
    # Ensure they are in sys.path
    for p in scan_paths:
        if p not in sys.path:
            sys.path.append(p)
    
    # Also ensure src/core is in path for decorators
    src_core = os.path.join(src_root, 'core')
    if src_core not in sys.path:
        sys.path.append(src_core)

    for scan_path in scan_paths:
        if not os.path.exists(scan_path):
            continue
            
        plugin_files = glob.glob(os.path.join(scan_path, "fu_*.py"))
        
        for plugin_path in plugin_files:
            filename = os.path.basename(plugin_path)
            if filename == "__init__.py" or filename == "fu_plugin_loader.py":
                continue
                
            module_name = os.path.splitext(filename)[0]
            
            # Import the module
            try:
                # Use importlib for cleaner dynamic imports if needed, 
                # but __import__ is fine for triggering decorators.
                __import__(module_name)
            except Exception as e:
                print(f"Flame Utilities: Failed to load plugin '{module_name}' from {scan_path}: {e}")
