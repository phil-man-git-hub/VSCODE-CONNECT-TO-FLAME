# Goal: Project Structure Refactoring

## Vision
To evolve the `flame-utilities` directory into a professional, scalable, and robust architecture that respects Autodesk Flame's unique constraints (no `__init__.py` files) while providing a cleaner developer experience. This refactor aims to eliminate "root clutter" and standardize how the toolkit "ignites" itself within the Flame environment.

---

## 1. Architectural Pivot: The Bootstrap Pattern
Since Flame prohibits traditional Python packages, we will implement a **Bootstrap Pattern**. A single, authoritative `fu_bootstrap.py` will be responsible for resolving the toolkit's root and injecting all necessary subdirectories into `sys.path`. 

### The Reasoning: Why Bootstrap?
Currently, every major script (e.g., `fu_logger.py`, `fu_eavesdrop.py`) contains redundant, fragile boilerplate to find the toolkit root and manipulate `sys.path`. This has several drawbacks:
*   **Maintenance Overhead**: Moving a file requires updating the path logic in multiple places.
*   **Import Fragility**: If a script is executed from a different working directory, imports often fail.
*   **Context Bloat**: Scripts are cluttered with 10-15 lines of path math before the actual logic begins.

**`fu_bootstrap.py`** centralizes this "infrastructure" logic. By importing bootstrap first, any script in the toolkit gains immediate access to `src/`, `lib/`, and `service/` without needing to know where they are relative to itself.

---

## 2. Proposed Structural Changes

| Directory / File | Action | Purpose |
| :--- | :--- | :--- |
| `flame-utilities/fu_bootstrap.py` | **NEW** | Central path discovery and environment setup. |
| `flame-utilities/service/` | **NEW** | Move `fu_eavesdrop.py`, `fu_activate.py`, and `fu_eavesdrop_init.py` here. |
| `flame-utilities/lib/` | **RETAIN** | Keep high-level SDKs (e.g., `fu_pybox_v3_13.py`) and AI technical bridges. |
| `flame-utilities/src/` | **FLATTEN** | Consolidate `src/utils` and `src/core` into a flatter structure to reduce import depth. |
| `flame-utilities/*.json` | **MOVE** | Ensure all JSON configs remain in `config/` to keep the root pristine. |

### Targeted Root Cleanup
The root of `flame-utilities/` should ideally only contain:
- `fu_bootstrap.py` (The entry point)
- `README.md`
- `config/`, `lib/`, `service/`, `src/`, `scripts/`, `tests/`

---

## 3. Initiative Task List

| Task ID | Action | Affected Files |
| :--- | :--- | :--- |
| **REF-01** | Create `fu_bootstrap.py` | `flame-utilities/fu_bootstrap.py` (NEW) |
| **REF-02** | Migrate Services | `fu_eavesdrop.py`, `fu_eavesdrop_init.py` $\rightarrow$ `flame-utilities/service/` |
| **REF-03** | Flatten Source | `src/core/*`, `src/utils/*` $\rightarrow$ `flame-utilities/src/` |
| **REF-04** | Refactor `fu_activate` | `flame-utilities/fu_activate.py` (Use bootstrap to trigger init) |
| **REF-05** | Update Imports | All `.py` files in `src/`, `lib/`, and `service/` (Remove path boilerplate) |
| **REF-06** | Update Automation | `scripts/deploy_to_flame_project.py`, `.github/workflows/ci.yml` |

---

## 4. Consequences & Benefits

### Strengths Gained
*   **Import Reliability**: By using `fu_bootstrap`, we ensure that `import fu_logger` always works, regardless of which subdirectory the parent script is running from.
*   **Deployment Simplicity**: The project becomes a "drop-in" folder where only the bootstrap needs to be referenced by external hooks.
*   **Reduced Complexity**: Flat internal structures make it easier for AI agents (and humans) to locate utilities without navigating deep nested hierarchies that aren't true Python packages.

### Weaknesses Addressed
*   **Eliminates Root Clutter**: Service-level logic is no longer mixed with documentation and metadata.
*   **Solves Path Fragility**: Removes the need for every script to contain `os.path.dirname(os.path.dirname(__file__))` boilerplate.

---
*Proposed by Gemini on 2026-02-02.*
