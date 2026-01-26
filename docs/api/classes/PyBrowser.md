# Class: PyBrowser

**Module**: `flame`

**Inherits from**: instance, object

## Description
This class represents the file browser.


## Properties
| Name | Description |
| --- | --- |
| `bit_depth` | Return the bit depth. |
| `colour_space` | Return the colour space. |
| `frame_ratio` | Return the frame ratio. Returns None when resolution is set to Same As Source. |
| `height` | Return the height. Returns None when resolution is set to Same As Source. |
| `resize_filter` | Return the resize filter. |
| `resize_mode` | Return the resize mode. |
| `resolution` | Return the name of the resolution preset. |
| `scaling_presets_value` | Return the scaling presets value. Returns None when resolution is not set to Scaling Presets. |
| `scan_mode` | Return the scan mode. |
| `selection` | Get the selected files/directories. |
| `sequence_mode` | Return the sequence mode. |
| `width` | Return the width. Returns None when resolution is set to Same As Source. |


## Methods
### `show`
```python
show
```


show( (PyBrowser)arg1, (str)default_path [, (object)extension='' [, (bool)select_directory=False [, (bool)multi_selection=False [, (object)include_resolution=False [, (str)title='Load']]]]]) -> None :

    Show the file browser.Keyword arguments:

    default_path -- Set the path.

    extension -- Set the extension filter. Can be a single extension or a list of extensions.Leave empty to see all files.

    select_directory -- Only show directories.

    multi_selection -- Allow the user to select multiple files.

    include_resolution -- Display the resolution controls. Possible values are False, True, or "Full". The Full mode includes the new adaptive and scaling presets modes.

    title -- Set the window title.

    

---
