# Class: PyWorkspace

**Module**: `flame`

Object representing a Workspace.

## Methods
### `desktop(...)`

None( (flame.PyWorkspace)arg1) -> object

### `libraries(...)`

None( (flame.PyWorkspace)arg1) -> list

### `create_library(...)`

create_library( (PyWorkspace)arg1, (str)name) -> object :
    Create a new Library in a Workspace.

### `replace_desktop(...)`

replace_desktop( (PyWorkspace)arg1, (PyDesktop)desktop) -> bool :
    Replace the Workspace active Desktop with another one.

### `set_desktop_reels(...)`

set_desktop_reels( (PyWorkspace)arg1 [, (object)group=None]) -> bool :
    Set the Desktop Reels view mode.

### `set_freeform(...)`

set_freeform( (PyWorkspace)arg1 [, (object)reel=None]) -> bool :
    Set the Freeform view mode.

