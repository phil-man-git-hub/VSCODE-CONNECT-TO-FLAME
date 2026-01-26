# Class: PyTrack

**Module**: `flame`

Object representing a Track.

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


