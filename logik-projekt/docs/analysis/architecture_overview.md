# Logik-Projekt Architecture Analysis

**Date:** 2026-02-03
**Scope:** `logik-projekt` directory
**Analyst:** Gemini

## 1. High-Level Architecture

The `logik-projekt` directory follows a "Decoupled Logic" pattern, separating entry points (Hooks), business logic (Source), and data (Configuration).

### directory Map
```
logik-projekt/
├── hooks/       # FLAME ENTRY POINTS. Python scripts executed by Flame.
├── src/         # BUSINESS LOGIC. Reusable Python modules.
│   └── core/    # Core functionality (functions, UI, specific logic).
└── cfg/         # DATA LAYER. XML and JSON configuration templates.
```

### The Execution Flow
1.  **Trigger:** User interacts with a specific context (Main Menu, Media Panel) in Flame.
2.  **Hook (`hooks/*.py`):** Flame executes a script from the `hooks/` directory (e.g., `create_projekt_layout.py`).
3.  **Bootstrap:** The hook manually injects the project root into `sys.path` to locate `src`.
4.  **Logic (`src/`):** The hook imports and calls functions from `src/core` (e.g., `create_or_validate_object`).
5.  **Configuration (`cfg/`):** The logic reads JSON/XML templates from `cfg/` to drive creation of objects (Libraries, Reels, Folders).

## 2. Hook & Configuration Interaction

The core design philosophy is **Data-Driven Execution**. Instead of hardcoding project structures, the python logic iterates over definition files.

### Mechanism
- **Path Resolution:** `src/core/functions/get/pathfinder_abs.py` is responsible for locating the `cfg/` directory relative to the executing script.
- **Template Loading:**
    - **Format:** Attributes are stored in JSON files (e.g., `library_template_04.json`).
    - **Parsing:** `create_projekt_layout.py` reads these files and uses `json.load()`.
    - **Execution (Risk):** The current implementation uses `exec()` to dynamically construct and execute Flame Python API commands based on strings in the JSON.
    - **Example Flow:**
        ```python
        # simplified
        data = json.load(open("cfg/library_template_04.json"))
        command = f"create_{data['object_type']}(name='{data['object_name']}')"
        exec(command)
        ```

## 3. Integration Points with `flame-utilities`

The `flame-utilities` suite offers robust infrastructure that `logik-projekt` is currently re-implementing manually.

### A. Path Management & Bootstrapping
- **Current State:** `hooks/create_projekt_layout.py` manually calculates `project_root` and modifies `sys.path`. It also uses a custom class `pathfinder_abs` to find its own directories.
- **Improved Integration:**
    - Use `fu_bootstrap.py`: Rely on the standardized bootstrapper to handle `sys.path` injection.
    - Use `pathlib`: Replace string manipulation in `pathfinder_abs` with standard `pathlib` (which `flame-utilities` prefers).

### B. Configuration Loading
- **Current State:** Manual `json` and `xml` parsing scattered across scripts.
- **Improved Integration:** Centralize configuration loading. If `flame-utilities` introduces a `ConfigManager`, `logik-projekt` should consume it.

### C. Logging vs Print
- **Current State:** Elaborate `print()` statements with manual formatting (`separator_hash`).
- **Improved Integration:** Switch to standard Python `logging`. This creates structured logs that `flame-utilities` can capture (e.g., in `fu_eavesdrop` or `scripts/logs/`), keeping the Flame console clean.

### D. Security (`exec`)
- **Current State:** Heavy reliance on `exec()` to turn JSON strings into API calls. This is brittle and potentially unsafe.
- **Improved Integration:** Refactor to use a factory pattern or direct API calls.
    - *Instead of:* `exec("library.create_folder(name='foo')")`
    - *Use:* `getattr(library, "create_folder")(name="foo")` (The code already does this partially, but `create_and_validate_from_template` falls back to `exec`).

## 4. Immediate Recommendations

1.  **Adopt `fu_bootstrap`:** Remove the manual `sys.path` insertion block from all `hooks/*.py` files and import `fu_bootstrap` instead (if feasible within the Flame Python environment).
2.  **Refactor `pathfinder_abs.py`:** It is a complex class for a simple task. Simplify using `pathlib` and `__file__`.
3.  **Standardize Logging:** Replace `print(separator)` blocks with a standardized logger.
