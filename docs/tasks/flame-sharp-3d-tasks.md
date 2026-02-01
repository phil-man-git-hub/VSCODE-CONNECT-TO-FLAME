# Tasks: FU_ML_Sharp Development

This list tracks the implementation of the `fu_ml_sharp.py` PyBox handler and its underlying AI worker.

## 1. Environment & Research
- [x] **Dependency Audit:** Verify requirements for the `apple/ml-sharp` repository (Torch 2.3.1).
- [x] **SDK Indexing:** Index SHARP documentation into `docs/research/understanding-SHARP.md` for RAG support.
- [ ] **Virtual Env Setup:** Create a specialized `.venv_sharp` to isolate AI dependencies.

## 2. Technical Bridge (Worker)
- [x] **`fu_ml_sharp_client.py`:** Implement the class that loads the SHARP model and weights.
- [x] **Inference Logic:** Create a function that takes a single EXR and returns a 3D Splat/Cloud.
- [x] **Rasterization Pass:** Implement a lightweight renderer to output Depth and Multiview frames.

## 3. PyBox Handler (`fu_ml_sharp.py`)
- [x] **Initial Foundation:** Inherit from `fu_pybox_v3_13.BaseClass`.
- [x] **Socket Setup:** Configure Front (Input) and Result (Output) sockets for EXR/PLY data.
- [x] **Dynamic UI:**
    - [x] `Output Type`: Popup (Depth Map, PLY Cloud, Turntable Render).
    - [x] `Resolution`: Popup (512, 1024, 2048).
    - [x] `Generate 3D`: Trigger button.
- [x] **Lifecycle Execution:** Implement the logic to hand off the EXR path to the SHARP worker and wait for the result.

## 4. Image & Data Pipeline
- [ ] **EXR Handling:** Ensure the 16-bit Float dynamic range is preserved during the Torch tensor conversion.
- [x] **PLY Export:** Write logic to convert Gaussian Splat points into a PLY format readable by Flame's Action node.

## 5. Verification
- [x] **Standalone Test:** Run inference on an EXR via the terminal (Verified via dry_run_sharp_bridge.py).
- [ ] **Flame Integration:** Load the handler in Batch and verify the 3D-to-2D depth alignment.

## 6. Secure Splat Viewer Integration
- [ ] **`fu_splat_viewer.py`:** Implement a specialized visualization handler.
- [ ] **Local Hosting:** Add logic to serve splat data via a temporary local HTTP server for SuperSplat.
- [ ] **Browser Orchestration:** Use `webbrowser` to launch the sandboxed viewer.
- [ ] **Blender Pathway:** Architect the tool to support launching Blender with the KIRI add-on via CLI.
