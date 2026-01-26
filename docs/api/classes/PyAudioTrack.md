
# Class: PyAudioTrack

**Module**: `flame`

## Inheritance & Hierarchy
* **Base class:** `PyFlameObject`
* **Functional Role:** Represents a specific audio track in a timeline, containing audio segments.
* **Contained by:** `PyTimeline`
* **Contains:** `PySegment`


## Description
Represents an Audio Track in a timeline, used for organizing and editing audio segments in Flame.

---

## Attributes
| Attribute         | Type  | Description |
|-------------------|-------|-------------|
| expanded          | bool  | The expanded status of the Version or Audio Track. Values: True/False |
| selected_segments | list  | List of PySegment currently selected. |
| solo              | bool  | The solo status of the Track. Values: True/False |
| mute              | bool  | The mute status of the Track. Values: True/False |

---


## Methods
### Properties
- `channels(...)` — None( (flame.PyAudioTrack)arg1) -> list 
None( (flame.PyAudioTrack)arg1) -> list

- `stereo(...)` — None( (flame.PyAudioTrack)arg1) -> bool 
None( (flame.PyAudioTrack)arg1) -> bool


### Built-in methods
- `copy_to_media_panel(...)` — copy_to_media_panel( (PyAudioTrack)arg1, (PyArchiveEntry)destination [, (str)duplicate_action='add']) -> object : 
copy_to_media_panel( (PyAudioTrack)arg1, (PyArchiveEntry)destination [, (str)duplicate_action='add']) -> object :
    Create a new clip with a copy of the PyObject.


### Example
```python
# Mute/solo an audio track and list selected segments
# Assume 'track' is a PyAudioTrack object
track.mute = True
track.solo = False
print('Track muted:', track.mute, 'solo:', track.solo)
for seg in track.selected_segments:
    print('Selected audio segment:', seg.attributes.name)
```
