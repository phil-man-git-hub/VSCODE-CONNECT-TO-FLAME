# Tasks: FU_Bridge_ComfyUI Development

This list tracks the implementation of the `fu_bridge_comfyui.py` PyBox handler, which serves as the bridge between Autodesk Flame and ComfyUI.

## 1. Core Handler Foundation
- [x] **SDK Setup:** Import `fu_pybox_v3_13` and initialize the `ComfyUIBridge` class.
- [x] **Socket Definition:** Configure `Front`, `Matte`, and `Result` sockets using 16-bit Float EXR format.
- [x] **Lifecycle Hooks:** Implement `initialize()`, `setup_ui()`, and `execute()` methods.

## 2. Dynamic UI Implementation
- [x] **Workflow Selector:** Create a popup menu to choose from available ComfyUI workflow templates (.json).
- [x] **Server Config:** Add a text field for the ComfyUI server address (defaults to 127.0.0.1:8188).
- [x] **Trigger Button:** Implement a "Generate" toggle button (Global Element) to initiate the AI pass.
- [x] **Status Bar:** Use a read-only text field or `set_notice_msg` to display execution status (Queueing, Executing, Done).

## 3. Communication Logic (Backend)
- [x] **Client Integration:** Integrate `fu-comfyui/fu_comfyui.py` logic within the handler.
- [x] **Workflow Mapping:** Write logic to read a workflow JSON and inject the Flame frame paths into the correct nodes.
- [x] **WebSocket Monitoring:** Implement a non-blocking check (during `execute`) to monitor the ComfyUI progress.

## 4. Image Pipeline (Data Exchange)
- [x] **Path Handling:** Ensure `pathlib` is used to manage the "Drop Zone" directory between Flame and ComfyUI.
- [x] **Result Verification:** Verify that the output image exists and is valid before returning control to Flame.

## 5. Metadata & Error Handling
- [x] **Metadata Tagging:** Pass Flame's `shot_name` and `frame` number to the ComfyUI result filename for better tracking.
- [x] **Graceful Failure:** Implement detailed error messages if the server is unreachable or the workflow fails.

## 6. Verification
- [x] **Dry Run:** Test the handler using a simulated JSON payload from the terminal.
- [ ] **Flame Integration:** Load the handler into a live PyBox node and verify the 16-bit EXR round-trip.

