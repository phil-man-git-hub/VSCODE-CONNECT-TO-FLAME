# Flame Utilities

A collection of Python utilities, hooks, and scripts for Autodesk Flame.

## Naming Conventions
- **Scripts:** All scripts in `flame-utilities/scripts` must be prefixed with `fu_` (e.g., `fu_export_clips.py`). This ensures easy identification and avoids collisions.

## Directory Structure

- **`hooks/`**:  
  Contains Python hook files (e.g., `app_initialized.py`, `batch_hook.py`) that listen for Flame events.  
  *Configuration:* Add this path to the `hook_path` in `init.cfg`.

- **`scripts/`**:  
  Standalone scripts intended to be run manually via the Flame Python "Run Script" menu or CLI. **Must be prefixed with `fu_`.**

- **`src/`**:  
  Source code for internal libraries and shared logic.
  - **`core/`**: Core functionality and base classes.
  - **`utils/`**: General utility functions (logging, string manipulation, file I/O).
  *Important:* Since Flame does not support standard packages with `__init__.py`, files here must have **unique filenames** globally. You may need to add specific subdirectories to the `python_path` or use a deployment script to flatten them.

- **`lib/`**:  
  External or third-party libraries required by the utilities.

- **`config/`**:  
  Configuration files (JSON, YAML, XML) used by the scripts and hooks.

- **`examples/`**:  
  Example scripts and snippets (including those analyzing Autodesk patterns) for reference.

- **`bin/`**:  
  Shell scripts or binaries for deployment, setup, or external tools.

- **`api/`**:  
  API wrapper definitions or interface documentation.

- **`tools/`**:  
  Maintenance tools, build scripts, or dev-ops utilities.

## Constraints (Autodesk Flame)

1.  **Unique Filenames:** All Python files loaded by Flame must have unique names, even if they are in different folders.
2.  **No `__init__.py`:** Do not use `__init__.py` files to define packages. Flame's loader does not support them in the standard way.
