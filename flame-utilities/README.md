# Flame Utilities

**Goal:** Create hooks and scripts that will help to automate Flame and improve Flame connectivity with other software.

## Naming Conventions
- **Scripts:** All scripts in `flame-utilities/scripts` must be prefixed with `fu_` (e.g., `fu_export_clips.py`). This ensures easy identification and avoids collisions.

## Directory Structure

- **`fu_bootstrap.py`**:
  The central infrastructure component. Resolves local paths to allow importing from `src/` and `lib/` without standard package installation.

- **`service/`**:
  Contains the `fu_eavesdrop.py` listener and initialization hooks (`fu_eavesdrop_init.py`). This is the backend service that runs inside Flame.

- **`scripts/`**:
  Standalone scripts intended to be run manually via the Flame Python "Run Script" menu or CLI. **Must be prefixed with `fu_`.**

- **`src/`**:
  Source code for internal libraries and shared logic.
  - **`core/`**: Core functionality and base classes.
  - **`utils/`**: General utility functions.

- **`lib/`**:
  External or third-party libraries required by the utilities (e.g., specific PyBox implementations).

- **`config/`**:
  Configuration files (JSON, YAML, XML) used by the scripts and hooks.

- **`examples/`**:
  Example scripts and snippets for reference.

- **`bin/`**:
  Shell scripts or binaries for deployment, setup, or external tools.

- **`api/`**:
  API wrapper definitions or interface documentation.

- **`tools/`**:
  Maintenance tools, build scripts, or dev-ops utilities.

- **`logs/`**:
  Runtime logs for the listener and utilities.

## Constraints (Autodesk Flame)

1.  **Unique Filenames:** All Python files loaded by Flame must have unique names, even if they are in different folders.
2.  **No `__init__.py`:** Do not use `__init__.py` files to define packages. Flame's loader does not support them in the standard way.
