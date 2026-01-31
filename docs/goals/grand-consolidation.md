# Goal: The Grand Consolidation

## Vision
To transform `FLAME-UTILITIES` into a self-contained, portable toolkit that can be archived and restored alongside Autodesk Flame projects. By moving all listener and AI bridge logic into a single directory hierarchy, we ensure that project-specific automation never breaks due to workstation-level changes.

---

## 1. Architectural Pivot: Project-Centric Deployment
Instead of global workstation hooks, the entire `flame-utilities/` folder is copied into:
`<Flame_Project_Path>/setups/python/flame-utilities/`

A lightweight loader (`fu_loader.py`) in the parent directory ensures that Flame "ignites" the tools from within the archived folder.

---

## 2. Structural Consolidation

| Old Location | New Location | Purpose |
| :--- | :--- | :--- |
| `flame-listener/fu_eavesdrop.py` | `flame-utilities/fu_eavesdrop.py` | The Listener Logic |
| `flame-listener/fu_eavesdrop_init.py` | `flame-utilities/fu_eavesdrop_init.py` | The Hook Entry Point |
| `flame-listener/generate_stubs.py` | `flame-utilities/scripts/fu_generate_stubs.py` | Maintenance |
| `flame-mcp/` | `flame-utilities/whisper/` | The AI Bridge Hierarchy |

---

## 3. Impact & Reference Updates
This move requires a coordinated update of:
*   **Imports**: MCP tools and relay must find each other in the new hierarchy.
*   **Deployment Scripts**: `deploy_to_flame_project.py` must be updated to copy the entire folder.
*   **CI/CD**: Task runners and tests must look in the new paths.
*   **Documentation**: All "Getting Started" guides must reflect the new structure.
*   **AI Handlers**: Configuration for Claude/Cursor must be updated to the new `whisper/` paths.

---

## 4. Key Deliverables
1.  **Consolidated Directory**: All logic under `flame-utilities/`.
2.  **Portable Loader**: `fu_loader.py` for easy activation.
3.  **Updated Automation**: Fully functional deployment and versioning scripts.
