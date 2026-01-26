
# Class: PyBrowser

**Module**: `flame`

## Functional Role & Context
* **Functional Role:** Represents the file browser interface for selecting and importing files in Flame.

## Description
Provides access to the file browser UI, allowing users to select files, directories, and set import options.


## API Insight: Definition, Methods, and Usage
The **PyBrowser** class represents the file browser object, used to interact with the file system and retrieve user-selected paths.

### Definition and Hierarchy
| Property      | Value         | Description |
|-------------- |-------------- |-------------|
| Class Name    | PyBrowser     | System file browser dialog. |
| Parent Class  | None          | Standalone utility class. |
| Access Point  | flame.browser | Accessed as a static object from the flame module. |

### Core Methods
| Method              | Arguments                        | Returns   | Description |
|---------------------|----------------------------------|-----------|-------------|
| open_file()         | title, directory                 | str/None  | Open single file selection dialog. |
| open_files()        | title, directory                 | list/None | Open multiple file selection dialog. |
| open_directory()    | title, directory                 | str/None  | Open directory selection dialog. |
| save_file()         | title, directory                 | str/None  | Open file saving dialog. |

### Usage Context
PyBrowser is essential for scripts that need to reference external media, setups, or files, providing a programmatic interface to the OS file selection dialogs.

**Examples:**

```python
import flame

# Open a single file selection dialog
file_path = flame.browser.open_file('Select source', '/mnt/assets')

# Open multiple file selection dialog
files = flame.browser.open_files('Select frames', '/mnt/assets')

# Open a directory selection
dir_path = flame.browser.open_directory('Choose folder', '/mnt/assets')

# Or use the generic show() for more options
flame.browser.show('/mnt/assets', extension='exr', multi_selection=True, title='Import Files')
```



## Methods
### Properties
- `selection(...)` — None( (flame.PyBrowser)arg1) -> object 
None( (flame.PyBrowser)arg1) -> object

- `sequence_mode(...)` — None( (flame.PyBrowser)arg1) -> bool 
None( (flame.PyBrowser)arg1) -> bool

- `width(...)` — None( (flame.PyBrowser)arg1) -> object 
None( (flame.PyBrowser)arg1) -> object

- `height(...)` — None( (flame.PyBrowser)arg1) -> object 
None( (flame.PyBrowser)arg1) -> object

- `scaling_presets_value(...)` — None( (flame.PyBrowser)arg1) -> object 
None( (flame.PyBrowser)arg1) -> object

- `bit_depth(...)` — None( (flame.PyBrowser)arg1) -> object 
None( (flame.PyBrowser)arg1) -> object

- `frame_ratio(...)` — None( (flame.PyBrowser)arg1) -> object 
None( (flame.PyBrowser)arg1) -> object

- `scan_mode(...)` — None( (flame.PyBrowser)arg1) -> str 
None( (flame.PyBrowser)arg1) -> str

- `colour_space(...)` — None( (flame.PyBrowser)arg1) -> str 
None( (flame.PyBrowser)arg1) -> str

- `resize_mode(...)` — None( (flame.PyBrowser)arg1) -> str 
None( (flame.PyBrowser)arg1) -> str

- `resize_filter(...)` — None( (flame.PyBrowser)arg1) -> str 
None( (flame.PyBrowser)arg1) -> str

- `resolution(...)` — None( (flame.PyBrowser)arg1) -> str 
None( (flame.PyBrowser)arg1) -> str


### Built-in methods
- `show(...)` — show( (PyBrowser)arg1, (str)default_path [, (object)extension='' [, (bool)select_directory=False [, (bool)multi_selection=False [, (object)include_resolution=False [, (str)title='Load']]]]]) -> None : 
show( (PyBrowser)arg1, (str)default_path [, (object)extension='' [, (bool)select_directory=False [, (bool)multi_selection=False [, (object)include_resolution=False [, (str)title='Load']]]]]) -> None :
    Show the file browser.Keyword arguments:
    default_path -- Set the path.
    extension -- Set the extension filter. Can be a single extension or a list of extensions.Leave empty to see all files.
    select_directory -- Only show directories.
    multi_selection -- Allow the user to select multiple files.
    include_resolution -- Display the resolution controls. Possible values are False, True, or "Full". The Full mode includes the new adaptive and scaling presets modes.
    title -- Set the window title.


