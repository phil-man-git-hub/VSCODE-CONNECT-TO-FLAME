# Pybox API Reference (`pybox_v1`)

This document provides a technical reference for the `pybox_v1` module, which is used to create handlers for Autodesk Flame's Pybox nodes.

**Module:** `pybox_v1`  
**Location:** `/opt/Autodesk/presets/<version>/shared/pybox/pybox_v1.py`

## UI Creation Functions

These functions are used to define the user interface of the Pybox node. Elements created with these functions must be added to the node using `BaseClass.add_render_elements()` or `BaseClass.add_global_elements()`.

### `create_page(name, *cols)`
Creates a new page definition for the node UI.
- **name** (str): Display name of the tab.
- **cols** (str, optional): Names of the columns in the page.
- **Returns:** A page definition dictionary.

### `create_float_numeric(name, value=0.0, default=0.0, min=0.0, max=100.0, inc=1.0, row=0, col=0, page=0, channel_name=None, tooltip="")`
Creates a floating-point numeric field.
- **name** (str): Label displayed in the UI.
- **value** (float): Current value.
- **default** (float): Default value on load.
- **min** (float): Minimum allowed value.
- **max** (float): Maximum allowed value.
- **inc** (float): Increment step when dragging.
- **row** (int): Y position (0-4).
- **col** (int): X position (0-3).
- **page** (int): Page index (0-5).
- **channel_name** (str, optional): Animation channel name. Defaults to `name + "_chn"`.
- **tooltip** (str): Tooltip text.

### `create_vector_numeric(name, size=3, values=None, numeric_info=None, default=0.0, min=0.0, max=100.0, inc=1.0, row=0, col=0, page=0, channel_name=None, tooltip="")`
Creates a 2D or 3D vector numeric field.
- **name** (str): Label displayed in the UI.
- **size** (int): Vector dimension (2 or 3).
- **values** (list[float]): Initial values.
- **numeric_info** (list): Optional list of per-component info (see `create_numeric_info`).
- **default** (float): Default value for all components.
- **min**, **max**, **inc**: Constraints for all components.

### `create_popup(name, items, value=0, default=0, row=0, col=0, page=0, tooltip="")`
Creates a dropdown menu.
- **name** (str): Label.
- **items** (list[str]): List of menu options.
- **value** (int): Index of current selection.
- **default** (int): Index of default selection.

### `create_color(name, default=None, values=None, row=0, col=0, page=0, channel_name=0, tooltip="")`
Creates a color pot.
- **name** (str): Label.
- **default** (list[float]): Default RGB values [0.0-1.0].
- **values** (list[float]): Current RGB values.

### `create_toggle_button(name, value, default=False, row=0, col=0, page=0, tooltip="")`
Creates a toggle button.
- **name** (str): Label.
- **value** (bool): Current state (True/False).
- **default** (bool): Default state.

### `create_file_browser(name, value, extension, home, row=0, col=0, page=0, tooltip="", isFileSelector=True)`
Creates a file browser widget.
- **name** (str): Label.
- **value** (str): Current path.
- **extension** (str): File extension filter (e.g., "jpg", "exr").
- **home** (str): Default "Home" directory path.
- **isFileSelector** (bool): True for file selection, False for directory.

### `create_text_field(name, value="", row=0, col=0, page=0, tooltip="", isField=True)`
Creates a string input field.
- **name** (str): Label.
- **value** (str): Current text.

---

## BaseClass

The `BaseClass` is the parent class for all Pybox handlers. Your handler must inherit from this class and override specific lifecycle methods.

### Lifecycle Methods (Override these)

#### `initialize(self)`
Called when the Pybox is first loaded. Use this to:
- Set image format (`set_img_format`).
- Define input/output sockets (`set_in_socket`, `set_out_socket`).
- Transition state: `self.set_state_id("setup_ui")` followed by `self.setup_ui()`.

#### `setup_ui(self)`
Called to define the UI. Use this to:
- Create UI elements using the `create_*` functions.
- Add elements to pools: `add_global_elements()`, `add_render_elements()`.
- Set pages: `set_ui_pages()`.
- Transition state: `self.set_state_id("execute")` followed by `self.execute()`.

#### `execute(self)`
Called when processing is required. Use this to:
- Read input sockets/parameters.
- Run external processes (e.g., call Nuke, Maya, ImageMagick).
- Write to output sockets.
- Transition state: `self.set_state_id("teardown")` followed by `self.teardown()`.

#### `teardown(self)`
Called when the Pybox is destroyed or the handler is changed. Clean up resources here.

### State Management

#### `set_state_id(self, state_id)`
Sets the next state for the Pybox.
- **state_id** (str): One of `"initialize"`, `"setup_ui"`, `"execute"`, `"teardown"`.

#### `dispatch(self)`
Executes the method corresponding to the current `state_id`.

### Socket Management

#### `set_in_socket(self, idx, socket_type, path)`
Defines an input socket at a specific index.
- **idx** (int): 0-based index.
- **socket_type** (str): "Front", "Matte", "Back", "3DMotion", "Background", "MotionVector", "Normal", "Position", "Uv", "ZDepth", "undefined".
- **path** (str): File path where Flame writes the input image.

#### `set_out_socket(self, idx, socket_type, path)`
Defines an output socket at a specific index.
- **socket_type** (str): "Result", "OutMatte", "Out3DMotion", etc.
- **path** (str): File path where Flame expects the result image.

#### `add_in_socket(self, socket_type, path)`
Appends a new input socket.

#### `add_out_socket(self, socket_type, path)`
Appends a new output socket.

### UI Management

#### `add_global_elements(self, *elements)`
Adds UI elements that trigger an immediate Python callback when changed (e.g., browsers, setup buttons).

#### `add_render_elements(self, *elements)`
Adds UI elements that only update parameters for the render pass (e.g., blur amount, color correction).

#### `set_ui_pages(self, *pages)`
Sets the visible pages (tabs) in the node UI.

#### `get_global_element_value(self, name)` / `set_global_element_value(self, name, value)`
Get/Set values for global elements.

#### `get_render_element_value(self, name)` / `set_render_element_value(self, name, value)`
Get/Set values for render elements.

### Metadata Access (Getters)

- `get_bit_depth()`
- `get_colour_space()`
- `get_date()`, `get_date_day()`, `get_date_month()`, `get_date_year()`
- `get_frame()` (Current Batch frame)
- `get_frame_ratio()`
- `get_framerate()`
- `get_height()`, `get_width()` (Resolution)
- `get_img_format()`
- `get_nickname()`, `get_user()`
- `get_node_name()`
- `get_project()`, `get_project_nickname()`
- `get_record_time_code()`, `get_source_time_code()`
- `get_shot_name()`, `get_tape_name()`
- `get_workstation()`

### Messaging / Logging

- `set_error_msg(msg)`
- `set_warning_msg(msg)`
- `set_notice_msg(msg)`
- `set_debug_msg(msg)`
