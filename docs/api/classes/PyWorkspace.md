
# Class: PyWorkspace

**Module**: `flame`

## Inheritance & Hierarchy
* **Base Class:** PyFlameObject
* **Contained By:** PyProject
* **Contains:** PyDesktop, PyLibrary

## Functional Role & Context
* **Functional Role:** Represents a workspace, providing access to desktop, libraries, and workspace management operations.
* **Context:** Used for automating workspace management, desktop replacement, and library creation in the Flame environment.

## Description
The PyWorkspace class provides programmatic access to workspaces, supporting automation of desktop and library management in the Flame environment.


Object representing a Workspace.

## API Insight
### Autodesk Flame API Insight (2026)

`PyWorkspace` encapsulates the project's technical configuration (frame rate, OCIO config, audio sample rate and defaults). It is a structural object contained by `PyProject` and is commonly used during automated project setup and validation.

**Core attributes:**
- `frame_rate` (str) — Read/Write; working frame rate (e.g., '23.976 fps').
- `audio_sample_rate` (str) — Read/Write; audio sample rate (e.g., '48000 Hz').
- `ocio_config_name` (str) — Read/Write; name of the OCIO configuration loaded for the workspace.
- `colour_space` (str) — Read/Write; primary working color space for the workspace.
- `default_bit_depth` (str) — Read/Write; default bit depth setting.

**Common methods (inherited):**
- `duplicate()` — Create a copy of the workspace.
- `move(destination)` — Move the workspace within the project hierarchy.
- `delete([confirm=True])` — Delete the workspace.

**Example:**

```python
# Inspect the project's primary workspace and update the OCIO name
ws = flame.project.workspaces[0]
print('Workspace frame rate:', ws.frame_rate)
ws.ocio_config_name = 'Company_OCIO_v2'
ws.default_bit_depth = '16'
```
## Attributes
| Attribute   | Type   | Description |
|-------------|--------|-------------|
| name        | str    | The name of an object in the Media Panel, resolving tokens if any are present. |
| uid         | str    | The unique identifier of an object in the Media Panel. |
| token_name  | str    | The tokenized name of an object in the Media Panel. |
| expanded    | bool   | The expanded state of an object in the Media Panel. True or False. |
| colour      | tuple  | The colour of an object in the Media Panel. |

## Methods
### Properties
- `desktop(...)` — None( (flame.PyWorkspace)arg1) -> object 
None( (flame.PyWorkspace)arg1) -> object

- `libraries(...)` — None( (flame.PyWorkspace)arg1) -> list 
None( (flame.PyWorkspace)arg1) -> list


### Built-in methods
- `create_library(...)` — create_library( (PyWorkspace)arg1, (str)name) -> object : 
create_library( (PyWorkspace)arg1, (str)name) -> object :
    Create a new Library in a Workspace.

- `replace_desktop(...)` — replace_desktop( (PyWorkspace)arg1, (PyDesktop)desktop) -> bool : 
replace_desktop( (PyWorkspace)arg1, (PyDesktop)desktop) -> bool :
    Replace the Workspace active Desktop with another one.

- `set_desktop_reels(...)` — set_desktop_reels( (PyWorkspace)arg1 [, (object)group=None]) -> bool : 
set_desktop_reels( (PyWorkspace)arg1 [, (object)group=None]) -> bool :
    Set the Desktop Reels view mode.

- `set_freeform(...)` — set_freeform( (PyWorkspace)arg1 [, (object)reel=None]) -> bool : 
set_freeform( (PyWorkspace)arg1 [, (object)reel=None]) -> bool :
    Set the Freeform view mode.


