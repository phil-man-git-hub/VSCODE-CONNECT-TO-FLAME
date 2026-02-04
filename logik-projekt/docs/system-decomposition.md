# System Decomposition: Logik-Projekt

This document provides a definitive, file-by-file manifest of the `logik-projekt` toolset, categorized by logical layer and functional purpose.

## 1. Trigger Layer (Hooks)
Entry points executed by Autodesk Flame.

| File | Purpose |
| :--- | :--- |
| `hooks/create_projekt_layout.py` | Main script for building Flame project structures. |
| `hooks/create_after_effects_script.py` | Triggers AE script generation. |
| `hooks/create_nuke_script.py` | Triggers Nuke script generation. |
| `hooks/create_dated_objects.py` | Logic for auto-timestamped objects. |
| `hooks/sync_assets.py` | Asset synchronization logic. |
| `hooks/logik_projekt_openclip_*.py` | Specialized OpenClip hooks (comp, mattes, neat_video, precomp, multichannel). |

## 2. Logic Layer (Core Engine)
The modularized Python engine located in `src/core/`.

### Functional Modules (`src/core/functions/`)
- **`browse/`**: Qt-based file browsers (`pyside6_qt_file_browser.py`).
- **`create/`**: The construction engine (e.g., `create_or_validate_object.py`, `create_shot_bookmarks.py`).
- **`define/`**: Structure definitions (`define_job_structure.py`, `define_shot_structure.py`).
- **`get/`**: Information retrieval and path discovery (`pathfinder_abs.py`, `pathfinder_rel.py`).
- **`io/`**: Data persistence and importing (`flame_importer.py`, `bookmark_manager.py`).
- **`list/`**: Directory listing and discovery utilities.
- **`log/`**: The unified `debugging_and_logging.py` system.
- **`process/`**: Computation and parsing for external apps (`process_shot_info_nuke.py`).
- **`ui/`**: A deep hierarchy of PySide6/Qt components for Flame integration.
  - `orchestrators/`: Master UI controllers (e.g., `pyside6_qt_flame_ui.py`).
  - `widgets/`: Custom UI elements (buttons, labels, tree widgets, sliders).
  - `dialog/`: Predefined dialog windows (message, password, progress).

### Master Logic (`src/core/logik/`)
- `logik_projekt_openclip.py`: High-level orchestration for complex OpenClip creation.

## 3. Data Layer (Configuration & Blueprints)
Located primarily in `cfg/`, this layer drives the execution logic.

### Global Configuration
- `LOGIK-PROJEKT-default-config.xml`: Repository-wide settings.
- `filesystem-tree.json`: The standard project directory layout.
- `object_colors.json`: Color mapping for Flame project objects.

### Project Templates
- `library_template_01.json` through `06.json`: Blueprints for various project phases.
- `flame-workspace.json`: Environment-level setup.

### External App Templates (`cfg/templates/`)
- **Adobe AE**: `.jsx.template` files for after-effects scripts.
- **Foundry Nuke**: `.nk` and `menu.py` templates for pipeline integration.

### Specialized Configs
- `cfg/logik_projekt_openclip_*/`: Subdirectories containing `config.xml` for specific OpenClip workflows.

## 4. Infrastructure & Maintenance
| Component | Purpose |
| :--- | :--- |
| `lp_bootstrap.py` | **Master Bootstrapper**. Handles `sys.path` and environment setup. |
| `version/version.json` | Global versioning for the toolset. |
| `scripts/` | Maintenance scripts like `update_changelist_comments.sh`. |
| `logs/session.log` | Persistent runtime logging. |
| `docs/` | Comprehensive technical documentation hub. |
| `help/` | Premium visual guides (`systems-architecture-guide.html`). |

---
*Exhaustive Manifest Update: 2026-02-03 (102 Files, 56 Directories)*
