# Goal: PyBox Modernization (Python 3.13 Migration)

## Objective
Establish the **`pybox_v3.13`** SDK—a modern, clean-room implementation of the PyBox protocol natively written for **Python 3.13**. This migration moves away from the legacy `pybox_v1` (Python 2.7) architecture to enable high-performance, AI-compatible, and type-safe workflows within Autodesk Flame.

## Rationale
- **End of Life:** Python 2.7 reached end-of-life in 2020; the VFX industry has moved to the VFX Reference Platform CY2024+ standards.
- **AI-Native Ready:** Modern generative AI frameworks (ComfyUI, PyTorch) require Python 3.10+.
- **Clean-Room Compliance:** By implementing the established JSON protocol from scratch as `pybox_v3.13`, we ensure modernization without contravening Autodesk's proprietary source copyright.
- **Future-Proofing:** Leverages Python 3.13 features like advanced typing, Pathlib integration, and improved error reporting.

## Migration Tasks

### 1. New SDK Development (`pybox_v3.13.py`)
- [x] **Clean-Room Implementation:** Developed `flame-utilities/lib/fu_pybox_v3_13.py` from scratch, based on the documented JSON communication schema.
- [x] **Unicode & Pathlib:** Implemented native UTF-8 handling and use `pathlib.Path` for all image sequence and temporary file operations.
- [x] **Modern Class Structure:** Refactored the `BaseClass` to use native Python 3 features (e.g., `@property`, `super()`).
- [x] **PEP 484 Type Hinting:** Provided full type stubs and inline hints to enable robust AI introspection via `fu_whisper`.

### 2. Handler Migration (v1 to v3.13)
- [ ] **Migration Tool:** Create a utility script (`fu_pybox_converter.py`) that uses AST analysis to port legacy 2.7 handlers to 3.13 syntax.
- [x] **Logic Conversion:** Updated initial production handler (`fu_pybox_no_op_v3.py`) to use `pybox_v3.13` imports and logic.
- [ ] **I/O Refactoring:** Ensure handlers correctly distinguish between Unicode JSON metadata and binary image data.

### 3. Execution Infrastructure
- [ ] **Universal Wrapper:** Implement a wrapper logic that detects the available Python 3.13 binary and sets up an isolated environment for the handler.
- [ ] **Environment Isolation:** Standardize the use of `.venv` for PyBox handlers to manage dependencies (OpenCV, ComfyUI-Client) safely.

### 4. FLAME-UTILITIES Integration
- [ ] **MCP Version Detection:** Update `fu_whisper` to detect if a PyBox node is running a `v1` or `v3.13` handler and suggest migrations.
- [ ] **Semantic Discovery:** Integrate `pybox_v3.13` symbols into `fu_encyclopedia` for RAG-assisted handler development.

## Success Metrics
- Successful execution of a 3.13-native `no_op.py` handler using `pybox_v3.13` inside Flame.
- Successful integration of `fu_comfyui` calls directly within a PyBox execution loop.
- Full verification that no proprietary `pybox_v1` source code is redistributed within the `flame-utilities/` directory.