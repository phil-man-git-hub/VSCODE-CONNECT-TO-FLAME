# Class: PySequence

**Module**: `flame`

Object representing a Sequence.

## Methods
### `open(...)`

open( (PySequence)arg1) -> bool :
    Open the Sequence.

### `create_container(...)`

create_container( (PySequence)arg1) -> object :
    Create a container with the selected segments or between the in and out marks.

### `create_version(...)`

create_version( (PySequence)arg1 [, (bool)stereo=False]) -> object :
    Add a Version to the Sequence.

### `create_audio(...)`

create_audio( (PySequence)arg1 [, (bool)stereo=False]) -> object :
    Add an Audio Track to the Sequence.

### `create_subtitle(...)`

create_subtitle( (PySequence)arg1) -> object :
    Add a Subtitle Track to the Sequence.

### `import_subtitles_file(...)`

import_subtitles_file( (PySequence)arg1, (str)file_name [, (object)file_type=None [, (bool)align_first_event_to_clip_start=False [, (object)convert_from_frame_rate=None]]]) -> object :
    Import a subtitles file into a new Subtitles Track.
    Return the new PySubtitleTrack.
    Keyword arguments:
    file_name -- The path and name of the file to import.
    file_type -- The type of subtitle if it is not the file extension (srt or txt).
    align_first_event_to_clip_start -- Force the first event to be aligned with the clip start.
    convert_from_frame_rate -- frame rate of the imported file (for txt files only).
    

### `create_group(...)`

create_group( (PySequence)arg1, (str)name) -> object :
    Creates a new PySequenceGroup.
    The group name must be supplied as argument.

### `insert(...)`

insert( (PySequence)arg1, (PyClip)source_clip [, (PyTime)insert_time=None [, (PyTrack)destination_track=None]]) -> bool :
    Creates a new PySequenceGroup.
    The group name must be supplied as argument.

### `overwrite(...)`

overwrite( (PySequence)arg1, (PyClip)source_clip [, (PyTime)overwrite_time=None [, (PyTrack)destination_track=None]]) -> bool :
    Creates a new PySequenceGroup.
    The group name must be supplied as argument.

### `copy_selection_to_media_panel(...)`

copy_selection_to_media_panel( (PySequence)arg1, (PyArchiveEntry)destination [, (str)duplicate_action='add']) -> object :
    Create a new clip by copying the currently selected segments.
    Return the new PyClip.
    Keyword arguments:
    destination -- The PyObject that acts as the destination.
    duplicate_action -- Action to take when an object with the same name already exists (add or replace).
    

### `extract_selection_to_media_panel(...)`

extract_selection_to_media_panel( (PySequence)arg1 [, (PyArchiveEntry)destination=None [, (str)duplicate_action='add']]) -> object :
    Extract the selection from the sequence.
    Return the new PyClip created from the selection when a destination is supplied.
    Keyword arguments:
    destination -- The PyObject that acts as the destination.
    duplicate_action -- Action to take when an object with the same name already exists (add or replace).
    

### `lift_selection_to_media_panel(...)`

lift_selection_to_media_panel( (PySequence)arg1 [, (PyArchiveEntry)destination=None [, (str)duplicate_action='add']]) -> object :
    Lift the selection from the sequence.
    Return the new PyClip created from the selection when a destination is supplied.
    Keyword arguments:
    destination -- The PyObject that acts as the destination.
    duplicate_action -- Action to take when an object with the same name already exists (add or replace).

### `groups(...)`

None( (flame.PySequence)arg1) -> list

