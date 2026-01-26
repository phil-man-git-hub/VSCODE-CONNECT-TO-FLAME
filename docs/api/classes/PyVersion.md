# Class: PyVersion

**Module**: `flame`

**Inherits from**: [PyFlameObject](PyFlameObject.md), instance, object

## Description
Object representing a Version.


## Properties
| Name | Description |
| --- | --- |
| `attributes` | The attributes of a python object. |
| `parent` | The parent object of this object. |
| `stereo` | Return whether or not the Version is stereo. |
| `tracks` | Return a list of the Version's Tracks. |


## Methods
### `copy_to_media_panel`
```python
copy_to_media_panel
```


copy_to_media_panel( (PyVersion)arg1, (PyArchiveEntry)destination [, (str)duplicate_action='add']) -> object :

    Create a new clip with a copy of the PyObject.

    

---

### `create_track`
```python
create_track
```


create_track( (PyVersion)arg1 [, (int)track_index=-1 [, (bool)hdr=False]]) -> object :

    Add a track to the Version.Keywords arguments:

    track_index -- Index to insert the new track at, -1 to append at the top.

    hdr -- Set to True to create an HDR track.

    

---

### `import_DolbyVision_xml`
```python
import_DolbyVision_xml
```


import_DolbyVision_xml( (PyVersion)arg1, (str)file_name [, (str)mode='Include Frame Based Transitions Trims' [, (int)track_index=-1]]) -> object :

    Add a track to the Version.Keywords arguments:

    track_index -- Index to insert the new track at, -1 to append at the top.

    hdr -- Set to True to create an HDR track.

    

---
