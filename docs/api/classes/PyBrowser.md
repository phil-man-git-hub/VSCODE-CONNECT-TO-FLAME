# Class: PyBrowser

**Module**: `flame`

This class represents the file browser.

## Methods
### `show(...)`

show( (PyBrowser)arg1, (str)default_path [, (object)extension='' [, (bool)select_directory=False [, (bool)multi_selection=False [, (object)include_resolution=False [, (str)title='Load']]]]]) -> None :
    Show the file browser.Keyword arguments:
    default_path -- Set the path.
    extension -- Set the extension filter. Can be a single extension or a list of extensions.Leave empty to see all files.
    select_directory -- Only show directories.
    multi_selection -- Allow the user to select multiple files.
    include_resolution -- Display the resolution controls. Possible values are False, True, or "Full". The Full mode includes the new adaptive and scaling presets modes.
    title -- Set the window title.
    

### `selection(...)`

None( (flame.PyBrowser)arg1) -> object

### `sequence_mode(...)`

None( (flame.PyBrowser)arg1) -> bool

### `width(...)`

None( (flame.PyBrowser)arg1) -> object

### `height(...)`

None( (flame.PyBrowser)arg1) -> object

### `scaling_presets_value(...)`

None( (flame.PyBrowser)arg1) -> object

### `bit_depth(...)`

None( (flame.PyBrowser)arg1) -> object

### `frame_ratio(...)`

None( (flame.PyBrowser)arg1) -> object

### `scan_mode(...)`

None( (flame.PyBrowser)arg1) -> str

### `colour_space(...)`

None( (flame.PyBrowser)arg1) -> str

### `resize_mode(...)`

None( (flame.PyBrowser)arg1) -> str

### `resize_filter(...)`

None( (flame.PyBrowser)arg1) -> str

### `resolution(...)`

None( (flame.PyBrowser)arg1) -> str

