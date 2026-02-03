import os
import sys
import glob
import fu_bootstrap

def load_fu_plugins():
    """
    Scans the flat 'src' directory for python files starting with 'fu_' 
    and imports them. This triggers the execution of any @fu_action 
    decorators contained within them.
    """
    root = fu_bootstrap.get_root()
    src_path = os.path.join(root, 'src')
    
    if not os.path.exists(src_path):
        print(f"Flame Utilities: src directory not found at {src_path}")
        return

    # Ensure src is in sys.path (Bootstrap should have done this, but we double check)
    if src_path not in sys.path:
        sys.path.insert(0, src_path)

    # Scan for fu_*.py files
    plugin_files = glob.glob(os.path.join(src_path, "fu_*.py"))
    
    for plugin_path in plugin_files:
        filename = os.path.basename(plugin_path)
        
        # Skip init files and this loader itself
        if filename == "__init__.py" or filename == "fu_plugin_loader.py":
            continue
            
        module_name = os.path.splitext(filename)[0]
        
        # Import the module to trigger registration
        try:
            if module_name in sys.modules:
                import importlib
                importlib.reload(sys.modules[module_name])
            else:
                __import__(module_name)
        except Exception as e:
            print(f"Flame Utilities: Failed to load plugin '{module_name}': {e}")
