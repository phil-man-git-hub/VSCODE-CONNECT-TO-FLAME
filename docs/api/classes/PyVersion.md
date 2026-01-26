# Class: PyVersion

**Module**: `flame`

Object representing a Version.

## Methods
### Properties
- `tracks(...)` — None( (flame.PyVersion)arg1) -> list 
None( (flame.PyVersion)arg1) -> list

- `stereo(...)` — None( (flame.PyVersion)arg1) -> bool 
None( (flame.PyVersion)arg1) -> bool


### Built-in methods
- `copy_to_media_panel(...)` — copy_to_media_panel( (PyVersion)arg1, (PyArchiveEntry)destination [, (str)duplicate_action='add']) -> object : 
copy_to_media_panel( (PyVersion)arg1, (PyArchiveEntry)destination [, (str)duplicate_action='add']) -> object :
    Create a new clip with a copy of the PyObject.

- `create_track(...)` — create_track( (PyVersion)arg1 [, (int)track_index=-1 [, (bool)hdr=False]]) -> object : 
create_track( (PyVersion)arg1 [, (int)track_index=-1 [, (bool)hdr=False]]) -> object :
    Add a track to the Version.Keywords arguments:
    track_index -- Index to insert the new track at, -1 to append at the top.
    hdr -- Set to True to create an HDR track.

- `import_DolbyVision_xml(...)` — import_DolbyVision_xml( (PyVersion)arg1, (str)file_name [, (str)mode='Include Frame Based Transitions Trims' [, (int)track_index=-1]]) -> object : 
import_DolbyVision_xml( (PyVersion)arg1, (str)file_name [, (str)mode='Include Frame Based Transitions Trims' [, (int)track_index=-1]]) -> object :
    Add a track to the Version.Keywords arguments:
    track_index -- Index to insert the new track at, -1 to append at the top.
    hdr -- Set to True to create an HDR track.


