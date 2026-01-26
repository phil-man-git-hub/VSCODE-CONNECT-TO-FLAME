
# Class: PyTrack

**Module**: `flame`

## Inheritance & Hierarchy
* **Base Class:** PyFlameObject
* **Contained By:** PySequence, PyTimeline

## Functional Role & Context
* **Functional Role:** Represents a track in a sequence or timeline, providing access to segments, transitions, and editing operations.
* **Context:** Used for programmatic editing, cutting, and transition management in the timeline or sequence.

## Description
The PyTrack class provides access to tracks in a sequence or timeline, enabling automation of segment management, transitions, and editing operations in Flame.


Object representing a Track.

## API Insight
### Autodesk Flame API Insight (2026)

`PyTrack` represents a video track in a `PySequence` and is the container for `PySegment` objects and `PyTransition`s. Use it to query or mutate per-layer state (mute/solo/lock), iterate segments, and insert transitions or gaps.

**Core attributes:** `segments`, `transitions`, `is_muted`, `is_solo`, `is_locked`, `attributes`, `parent`.

**Common methods:** `add_gap(start_frame, length, ripple=False)`, `set_muted(muted)`, `set_solo(solo)`, `set_locked(locked)`, `insert_transition(record_time, type, duration=10, alignment='Centred')`.

**Example:**

```python
# Mute the third track and list its segments
track = seq.tracks[2]
track.set_muted(True)
for seg in track.segments:
    print(seg.attributes.name, seg.record_in)
```

## Attributes
| Attribute         | Type   | Description |
|-------------------|--------|-------------|
| name              | str    | The name of the Track. |
| hidden            | bool   | The hidden status of the Track. True or False. |
| locked            | bool   | The locked status of the Track. True or False. |
| stereo_linked     | bool   | The stereo link status of the Track. True or False. |
| selected_segments | list   | Return a list of PySegment currently selected. |

## Methods
### Properties
- `segments(...)` — None( (flame.PyTrack)arg1) -> list 
None( (flame.PyTrack)arg1) -> list

- `transitions(...)` — None( (flame.PyTrack)arg1) -> list 
None( (flame.PyTrack)arg1) -> list


### Built-in methods
- `copy_to_media_panel(...)` — copy_to_media_panel( (PyTrack)arg1, (PyArchiveEntry)destination [, (str)duplicate_action='add']) -> object : 
copy_to_media_panel( (PyTrack)arg1, (PyArchiveEntry)destination [, (str)duplicate_action='add']) -> object :
    Create a new clip with a copy of the PyObject.

- `cut(...)` — cut( (PyTrack)arg1, (PyTime)cut_time [, (bool)sync=False]) -> None : 
cut( (PyTrack)arg1, (PyTime)cut_time [, (bool)sync=False]) -> None :
    Cut the Track.

- `insert_transition(...)` — insert_transition( (PyTrack)arg1, (PyTime)record_time, (str)type [, (int)duration=10 [, (str)alignment='Centred' [, (int)in_offset=0 [, (bool)sync=False]]]]) -> object : 
insert_transition( (PyTrack)arg1, (PyTime)record_time, (str)type [, (int)duration=10 [, (str)alignment='Centred' [, (int)in_offset=0 [, (bool)sync=False]]]]) -> object :
    Insert a Transition on the Track.
    Returns the new PyTransition if successful.
    Keywords argument:
    record_time -- Time at which the Transition is inserted.
    type -- Type of the new Transition.
    duration -- Duration of the new Transition in frames.
    alignment -- Alignment of the new Transition.
    in_offset -- Number of frames on left side of the cut in custom alignment.
    sync -- Perform the operation on all Tracks part of the sync group.


