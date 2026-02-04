"""
LOGIK-PROJEKT Bootstrap
-----------------------
Provides standalone path resolution and logging infrastructure for Logik-Projekt.
Ensures valid sys.path injection and standardizes configuration updates.
"""

import os
import sys
import logging
import importlib
from pathlib import Path

# -------------------------------------------------------------------------- #
# Path Resolution
# -------------------------------------------------------------------------- #

def get_root():
    """Returns the absolute path to the logik-projekt root directory."""
    return Path(__file__).parent.absolute()

def get_paths():
    """Returns a dictionary of critical paths."""
    root = get_root()
    return {
        "root": root,
        "hooks": root / "hooks",
        "src": root / "src",
        "cfg": root / "cfg",
        "logs": root / "logs",
        "docs": root / "docs"
    }

# -------------------------------------------------------------------------- #
# Logging Setup
# -------------------------------------------------------------------------- #

def setup_logging(name="logik-projekt", level=logging.INFO):
    """Configures a standardized logger."""
    paths = get_paths()
    log_dir = paths["logs"]
    log_dir.mkdir(exist_ok=True)
    
    log_file = log_dir / "session.log"
    
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Avoid adding duplicate handlers if setup runs multiple times
    if not logger.handlers:
        # File Handler
        fh = logging.FileHandler(log_file)
        fh.setLevel(level)
        fh_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        fh.setFormatter(fh_formatter)
        logger.addHandler(fh)
        
        # Console Handler (for Flame console visibility)
        ch = logging.StreamHandler()
        ch.setLevel(level)
        ch_formatter = logging.Formatter(
            '[LP] %(levelname)s: %(message)s'
        )
        ch.setFormatter(ch_formatter)
        logger.addHandler(ch)
        
    return logger

# -------------------------------------------------------------------------- #
# Initialization
# -------------------------------------------------------------------------- #

def bootstrap():
    """Injects core paths into sys.path."""
    paths = get_paths()
    root_str = str(paths["root"])
    
    if root_str not in sys.path:
        print(f"[LP] Bootstrapping: {root_str}")
        sys.path.insert(0, root_str)
        
    return paths

def refresh():
    """Forces a reload of all logik-projekt modules."""
    for mod_name in list(sys.modules.keys()):
        if mod_name.startswith("src.core.logik") or mod_name.startswith("src.core.functions"):
            print(f"[LP] UNLOADING: {mod_name}")
            del sys.modules[mod_name]
    
    # Reload the openclip module specifically if it was already imported
    if "src.core.logik.logik_projekt_openclip" in sys.modules:
         importlib.reload(sys.modules["src.core.logik.logik_projekt_openclip"])

# -------------------------------------------------------------------------- #
# Module Exports
# -------------------------------------------------------------------------- #

# Run bootstrap on import to ensure availability
paths = bootstrap()
logger = setup_logging()

if __name__ == "__main__":
    print(f"Logik-Projekt Root: {get_root()}")
    print("Paths:")
    for k, v in paths.items():
        print(f"  {k}: {v}")
    logger.info("Bootstrap check complete.")
