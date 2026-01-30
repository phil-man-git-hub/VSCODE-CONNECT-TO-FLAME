import logging
import logging.handlers
import os
import sys

"""
fu_logger.py

A centralized logging utility for Flame Utilities.
Ensures logs are written to both the file system and the console (stdout).

Feature:
    - Creates a separate log file for each module that requests a logger.
    - Example: 'fu_export' -> logs/fu_export.log

Usage:
    from fu_logger import get_logger
    log = get_logger(__name__)
    log.info("Something happened")
"""

# ------------------------------------------------------------------------------
# CONFIGURATION
# ------------------------------------------------------------------------------

# Calculate paths relative to this file location
# This file is in flame-utilities/src/utils/
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
FLAME_UTILS_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, '..', '..'))
LOG_DIR = os.path.join(FLAME_UTILS_ROOT, 'logs')

# Ensure log directory exists
if not os.path.exists(LOG_DIR):
    try:
        os.makedirs(LOG_DIR)
    except OSError as e:
        print(f"Flame Utilities Error: Could not create log directory {LOG_DIR}: {e}")

# ------------------------------------------------------------------------------
# CUSTOM HANDLER (Optional Flame GUI integration)
# ------------------------------------------------------------------------------
class FlameMessageConsoleHandler(logging.Handler):
    """
    A custom logging handler that sends logs to the Flame GUI Console
    (the message bar at the bottom/top of the screen).
    
    Only typically useful for Warnings/Errors or high-level Info to avoid spam.
    """
    def __init__(self):
        super(FlameMessageConsoleHandler, self).__init__()
        
    def emit(self, record):
        try:
            import flame
            msg = self.format(record)
            
            # Map Python logging levels to Flame message types
            if record.levelno >= logging.ERROR:
                msg_type = "error"
                duration = 5
            elif record.levelno >= logging.WARNING:
                msg_type = "warning"
                duration = 3
            else:
                msg_type = "info"
                duration = 2

            flame.messages.show_in_console(msg, msg_type, duration)
        except (ImportError, AttributeError):
            # Flame module not available (e.g. testing outside Flame)
            pass

# ------------------------------------------------------------------------------
# FACTORY
# ------------------------------------------------------------------------------

def get_logger(name):
    """
    Returns a configured logger instance.
    
    Args:
        name (str): The name of the module (usually __name__).
                    If the name starts with 'fu_', the log file will be named accordingly.
                    e.g. 'fu_export' -> logs/fu_export.log
    """
    # Clean up the name for the file system
    # If passed 'src.utils.fu_something', we just want 'fu_something'
    short_name = name.split('.')[-1]
    
    logger = logging.getLogger(f"fu.{short_name}")
    
    # If logger already has handlers, assume it's configured to prevent duplicates
    if logger.handlers:
        return logger
    
    logger.setLevel(logging.DEBUG)
    
    # 1. File Handler (Rotating) - PER SCRIPT
    # 1MB per file, keep last 3
    log_file_path = os.path.join(LOG_DIR, f"{short_name}.log")
    
    try:
        file_handler = logging.handlers.RotatingFileHandler(
            log_file_path, maxBytes=1024*1024, backupCount=3
        )
        file_formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(file_formatter)
        file_handler.setLevel(logging.DEBUG) # Log everything to file
        logger.addHandler(file_handler)
    except Exception as e:
        print(f"Flame Utilities Warning: Could not setup file logging for {short_name}: {e}")

    # 2. Console/Stream Handler (Stdout)
    # This shows up in the terminal where Flame started, or the Python Console tab.
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_formatter = logging.Formatter(
        f'[FlameUtils:{short_name}] %(levelname)s: %(message)s'
    )
    stream_handler.setFormatter(stream_formatter)
    stream_handler.setLevel(logging.INFO) # Only INFO and above to console by default
    logger.addHandler(stream_handler)
    
    # 3. Flame GUI Handler (Optional - Uncomment to enable)
    # gui_handler = FlameMessageConsoleHandler()
    # gui_handler.setFormatter(logging.Formatter('%(message)s'))
    # gui_handler.setLevel(logging.WARNING) # Only warn/error in the UI overlay
    # logger.addHandler(gui_handler)

    return logger
