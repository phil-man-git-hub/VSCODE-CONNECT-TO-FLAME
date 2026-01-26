# Class: PySubtitleTrack

**Module**: `flame`

**Inherits from**: [PyTrack](PyTrack.md), [PyFlameObject](PyFlameObject.md), instance, object

## Description
Object representing a Subtitle Track.


## Properties
| Name | Description |
| --- | --- |
| `attributes` | The attributes of a python object. |
| `parent` | The parent object of this object. |
| `segments` | Return a list of the Track's segments. |
| `transitions` | Return a list of the Track's transitions. |


## Methods
### `copy_to_media_panel`
```python
copy_to_media_panel
```


copy_to_media_panel( (PyTrack)arg1, (PyArchiveEntry)destination [, (str)duplicate_action='add']) -> object :

    Create a new clip with a copy of the PyObject.

    

---

### `cut`
```python
cut
```


cut( (PyTrack)arg1, (PyTime)cut_time [, (bool)sync=False]) -> None :

    Cut the Track.

---

### `export_as_srt_file`
```python
export_as_srt_file
```


export_as_srt_file( (PySubtitleTrack)arg1, (str)file_name [, (bool)character_based_attributes=True [, (bool)export_colours=False [, (str)exclude_colour='' [, (bool)use_original_colours=False [, (bool)use_original_alignment=False [, (bool)export_alignments=False [, (str)alignment_type='an' [, (str)exclude_alignment='' [, (str)start_timecode='Same as Clip']]]]]]]]]) -> None :

    Export the Subtitles Track as a SubRip (srt) file.Keyword arguments:

    file_name -- The path and name of the file to write.

    character_based_attributes -- Export the bold, italic, and underline attributes.

    export_colours -- Export colours.

    exclude_colour -- Specify a colour, in hexadecimal or CSS colour name, to ignore.

    use_original_colours -- Reuse hexadecimal or CSS colour names from the imported file.

    use_original_alignment -- Reuse alignment tokens from the imported file .

    export_alignments -- Export alignments.

    alignment_type -- Set to a or an alignment style tokens.

    exclude_alignment -- Specify an alignment to ignore.

    start_timecode -- Specify the timecode mode, Same as Clip or, Relative to Clip Start.

---

### `insert_transition`
```python
insert_transition
```


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

---
