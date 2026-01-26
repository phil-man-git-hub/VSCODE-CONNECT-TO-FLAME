
# Class: PyVersion

**Module**: `flame`

## Inheritance & Hierarchy
* **Base Class:** PyFlameObject
* **Contained By:** PySequence, PyClip

## Functional Role & Context
* **Functional Role:** Represents a version of a sequence or clip, providing access to tracks, stereo state, and version management operations.
* **Context:** Used for programmatic management of versions, including track creation and Dolby Vision XML import in Flame.

## Description
The PyVersion class provides access to versions in a sequence or clip, enabling automation of version management, track operations, and HDR/Dolby Vision workflows in Flame.


Object representing a Version.

## API Insight
### Autodesk Flame API Insight (2026)

`PyVersion` is an organizational container used to group related cuts or iterations (clips/sequences) for version management and review in the Media Panel. It is conceptually distinct from an editorial "version" track layer or the `attributes.version` metadata found on Open Clip imports.

**Core attributes:**
- `tracks` (list of `PyTrack`) — Read-only; returns tracks contained in the Version.
- `stereo` (bool) — Read-only; whether the version contains stereo media.
- `attributes` (`PyAttribute`) — Read-only metadata for the Version object.

**Key methods:**
- `create_track(track_index=-1, hdr=False)` — Add a new track to the Version (use `hdr=True` to create an HDR track).
- `copy_to_media_panel(destination, duplicate_action='add')` — Duplicate the Version's media to a destination.
- `import_DolbyVision_xml(file_name, mode='Include Frame Based Transitions Trims', track_index=-1)` — Import Dolby Vision XML data into the Version.

**Note on "version" terminology:**
- `PyVersion` (the object) is the Media Panel organizer. 
- Track-based versions are `PyTrack` layers within sequences. 
- The `attributes.version` string on clips/sequences (from Open Clip/OC/AAF imports) is metadata identifying the editorial version.

**Example:**

```python
# Create an HDR track in a Version and import Dolby Vision data
version = flame.project.desktop.reels[0].children[0]
new_track = version.create_track(track_index=-1, hdr=True)
print('Created track:', new_track)
version.import_DolbyVision_xml('/tmp/shot01_dv.xml', track_index=new_track.attributes.name)
```

## Attributes
| Attribute         | Type   | Description |
|-------------------|--------|-------------|
| expanded          | bool   | The expanded status of the Version or Audio Track. True or False. |
| selected_segments | list   | Return a list of PySegment currently selected. |

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


