# Comprehensive Insight: Autodesk Flame Pybox

**Source:** Autodesk Flame Family 2026 Help | Pybox
**Context:** This document synthesizes knowledge from the official Pybox documentation and analysis of shipping handler scripts.

## What is Pybox?

Pybox is a specialized node type in Autodesk Flame's Batch and Timeline environments. It acts as a bridge, allowing third-party applications (typically renderers) or custom Python scripts to integrate directly into the compositing pipeline.

Unlike standard Batch nodes which are hardcoded C++ operators, a Pybox node is driven by a **Python Handler**. This handler defines the node's UI, manages its sockets (inputs/outputs), and orchestrates the execution of external processes.

### Key Capabilities
-   **External Rendering:** Use Maya, Nuke, or command-line tools (like ImageMagick) to process images within a Batch tree.
-   **Custom UI:** Build dynamic user interfaces with tabs, sliders, color pots, and file browsers directly in the Flame node menu.
-   **Pipeline Integration:** Inject metadata, manage assets, or "radio-control" other software from within Flame.

### Core Architecture: Stateless & Synchronous

Pybox operates on a **stateless, synchronous** model.

1.  **JSON Payload:** Communication between Flame and the Python handler is exclusively through a JSON payload.
    -   Flame writes the current state (metadata, UI values, socket paths) to a JSON file.
    -   The Python handler reads this JSON, performs actions, updates the JSON structure, and writes it back.
    -   Flame reads the updated JSON to update its UI or get the status of a render.
2.  **State Machine:** The handler is responsible for managing its own state transitions. Flame does not drive the handler; it only reacts to the state set by the handler (`initialize`, `setup_ui`, `execute`, `teardown`).
3.  **Disk I/O:** Image exchange is done via the filesystem. Flame writes input frames to disk, the external process reads them, renders, and writes output frames to disk, which Flame then reads back. *Performance Tip: Use fast storage (NVMe) or RAM disks for these intermediate paths.*

## The `pybox_v1` Module

All Pybox handlers rely on the `pybox_v1` Python module.
-   **Location:** `/opt/Autodesk/presets/<version>/shared/pybox/pybox_v1.py`
-   **Availability:** This module is automatically added to the Python path by Flame when a Pybox node is loaded. You do not need to manually configure `sys.path` for it.

## Handler Lifecycle

A standard Pybox handler inherits from `pybox_v1.BaseClass` and overrides four key methods:

### 1. `initialize(self)`
-   **Trigger:** Called when the node is first loaded or reset.
-   **Tasks:**
    -   Set the image format (`self.set_img_format("exr")`).
    -   Define Input sockets (`self.set_in_socket(...)`) - where Flame writes source images.
    -   Define Output sockets (`self.set_out_socket(...)`) - where Flame expects results.
    -   Set next state: `self.set_state_id("setup_ui")`.

### 2. `setup_ui(self)`
-   **Trigger:** Called after initialization.
-   **Tasks:**
    -   Create UI widgets (`pybox.create_float_numeric`, `pybox.create_toggle_button`, etc.).
    -   Categorize widgets:
        -   **Global Elements:** Trigger Python execution immediately (e.g., "Load Setup").
        -   **Render Elements:** Only read during processing (e.g., "Blur Amount").
    -   Define layout (`pybox.create_page`, `self.set_ui_pages`).
    -   Set next state: `self.set_state_id("execute")`.

### 3. `execute(self)`
-   **Trigger:** Called when Flame needs a frame (rendering) or a Global UI element is changed.
-   **Tasks:**
    -   Read UI values (`self.get_render_element_value`).
    -   Check if processing is needed (`self.is_processing()`).
    -   Build command lines for external apps (e.g., `nuke -x ...`).
    -   Execute the external process.
    -   Set next state: `self.set_state_id("teardown")`.

### 4. `teardown(self)`
-   **Trigger:** Called when the node is deleted or the handler is changed.
-   **Tasks:** Cleanup temporary files or close connections.

## Examples and Use Cases

### Minimalist Handler ("Hello World")
The simplest handler just moves through the states without doing real work.
```python
import sys
import pybox_v1 as pybox

class HelloWorld(pybox.BaseClass):
    def initialize(self):
        self.set_state_id("setup_ui")
        self.setup_ui()
    def setup_ui(self):
        self.set_state_id("execute")
        self.execute()
    def execute(self):
        self.set_state_id("teardown")
        self.teardown()
    def teardown(self):
        pass

def _main(argv):
    p = HelloWorld(argv[0])
    p.dispatch()
    p.write_to_disk(argv[0])

if __name__ == '__main__':
    _main(sys.argv[1:])
```

### ImageMagick Integration
Common use case: Use ImageMagick to process frames.
-   **Inputs:** Flame writes `Front` to `/tmp/in.exr`.
-   **Process:** Handler calls `convert /tmp/in.exr -blur 0x8 /tmp/out.exr`.
-   **Outputs:** Flame reads `Result` from `/tmp/out.exr`.

### Nuke Integration
Allows controlling a Nuke script from Flame.
-   **Knob Exposure:** Nuke knobs named `adsk_*` can be auto-exposed in the Pybox UI.
-   **Execution:** The handler typically launches Nuke in command-line mode (`-x`) to render the specific frame requested by Flame.

## Best Practices

1.  **Error Handling:** Use `self.set_error_msg("Message")` to print errors to the Flame console. Wrap execution logic in `try...except` blocks.
2.  **Performance:**
    -   Minimize startup time for external processes (e.g., keep a daemon running if possible, though Pybox is naturally stateless/one-shot).
    -   Use fast SSDs for the socket paths.
3.  **Debugging:**
    -   Use `self.set_debug_msg()` to log info.
    -   Remember that `Change Handler` reloads the code from disk, allowing for rapid iteration without restarting Flame.
4.  **Distribution:** Distribute the `.py` file. If you have dependencies, they must be standard libraries or co-located in the Pybox presets folder.

## File Locations

-   **Handlers:** `/opt/Autodesk/presets/<version>/pybox/` (or any user path).
-   **Shared Modules:** `/opt/Autodesk/shared/presets/pybox/` (Place custom libraries here).
