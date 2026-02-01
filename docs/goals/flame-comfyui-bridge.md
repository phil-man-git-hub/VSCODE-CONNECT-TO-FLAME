# Goal: Flame-to-ComfyUI Bridge (PyBox v3.13)

## Objective
Develop a production-grade bridge that enables Autodesk Flame to utilize ComfyUI as a generative AI processing engine. This bridge will use the **`fu_pybox_v3.13`** SDK as the primary interface, allowing Flame artists to trigger AI workflows (e.g., automated in-painting, texture generation, upscaling) directly from the Batch or Timeline environments.

## Rationale
- **Native Integration:** PyBox is Flame's established method for integrating external processors into the compositing pipeline.
- **High Fidelity:** By using the Python 3.13 SDK, we can maintain 16-bit Float OpenEXR data paths, essential for professional VFX.
- **Stateless Synergy:** Both PyBox and the ComfyUI API operate on a stateless, JSON-driven model, making them architecturally compatible.
- **Automation:** Leveraging `fu_whisper` and `fu_comfyui.py` allows for automated AI workflows that feel like native Flame nodes.

## Implementation Tasks

### 1. PyBox Handler Development
- [ ] **`fu_comfyui_handler.py`:** Create a modern PyBox v3.13 handler that:
    - Sets up EXR input/output sockets.
    - Provides a UI for selecting ComfyUI workflow templates.
    - Includes a "Trigger" button (Global Element) to submit the prompt to ComfyUI.
    - Monitors execution status and notifies Flame upon completion.

### 2. ComfyUI Side Integration
- [ ] **Flame-Aware Nodes:** Identify or create custom ComfyUI nodes that:
    - Read OpenEXR files from specific paths (preserving HDR range).
    - Auto-save results to the "Result" paths defined by the PyBox JSON payload.
- [ ] **Metadata Passthrough:** Ensure Flame metadata (Shot Name, Project Name) is passed to ComfyUI for organizational purposes.

### 3. Orchestration & Communication
- [ ] **Backend Relay:** Use `fu-comfyui/fu_comfyui.py` to handle the HTTP/WebSocket handshake between the PyBox handler and the ComfyUI server.
- [ ] **Shared Storage Setup:** Standardize the use of a shared NVMe/RAM disk "Drop Zone" for frame exchange between the Flame workstation and the AI worker.

### 4. Workflow Library
- [ ] **Templates:** Create a set of base `.json` workflows for ComfyUI specifically tuned for Flame:
    - **AI Clean Plate:** Automated removal of objects using masks.
    - **Background Extender:** Out-painting for ratio changes.
    - **Texture Synthesizer:** Generating tileable textures from selection.

## Success Metrics
- A Flame artist can add a PyBox node, select "fu_comfyui_handler.py", and see a generated AI result in the Result View (F4).
- Preservation of full dynamic range (no clipping) from Flame -> ComfyUI -> Flame.
- Successful round-trip execution in under 10 seconds for a 2K frame (hardware permitting).
