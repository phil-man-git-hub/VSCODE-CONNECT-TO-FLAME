# Class: PyFolder

**Module**: `flame`

**Inherits from**: [PyArchiveEntry](PyArchiveEntry.md), [PyFlameObject](PyFlameObject.md), instance, object

## Description
Class derived from PyArchiveEntry. This class represents a Folder.


## Properties
| Name | Description |
| --- | --- |
| `attributes` | The attributes of a python object. |
| `batch_groups` | Return a list of Batch Group objects that are immediate children of the current object. |
| `batch_iterations` | Return a list of Batch Iteration objects that are immediate children of the current object. |
| `children` | Return a list of the immediate children of the current object. |
| `clips` | Return a list of Clip objects that are immediate children of the current object. |
| `desktops` | Return a list Desktop objects that are immediate children of the current object. |
| `folders` | Return a list of the Folder objects that are immediate children of the current object. |
| `parent` | The parent object of this object. |
| `reel_groups` | Return a list of Reel Group objects that are immediate children of the current object. |
| `reels` | Return a list of Reel objects that are immediate children of the current object. |
| `sequences` | Return a list of Sequence objects that are immediate children of the current object. |


## Methods
### `clear`
```python
clear
```


clear( (PyFolder)arg1 [, (bool)confirm=True]) -> bool :

    Clear the contents of the Folder object.

---

### `clear_colour`
```python
clear_colour
```


clear_colour( (PyArchiveEntry)arg1) -> None :

    Clear the colour of an object in the Media Panel.

---

### `commit`
```python
commit
```


commit( (PyArchiveEntry)arg1) -> None :

    Commit to disk the Media Panel object or its closest container possible.

---

### `create_folder`
```python
create_folder
```


create_folder( (PyFolder)arg1, (str)name) -> object :

    Create a new Folder object inside the Folder.

---

### `create_reel`
```python
create_reel
```


create_reel( (PyFolder)arg1, (str)name) -> object :

    Create a new Reel object inside the Folder.

---

### `create_reel_group`
```python
create_reel_group
```


create_reel_group( (PyFolder)arg1, (str)name) -> object :

    Create a new Reel Group object inside the Folder.

---

### `create_sequence`
```python
create_sequence
```


create_sequence( (PyFolder)arg1 [, (str)name='Untitled Sequence' [, (int)video_tracks=1 [, (bool)video_stereo=False [, (object)width=None [, (object)height=None [, (object)ratio=None [, (object)bit_depth=None [, (object)scan_mode=None [, (object)frame_rate=None [, (object)start_at=00:00:00+00 [, (object)duration=00:00:00+01 [, (int)audio_tracks=1 [, (bool)audio_stereo=True]]]]]]]]]]]]]) -> object :

    Create a Sequence in a PyReel, PyLibrary, PyFolder.

    Keywords arguments:

    video_tracks -- Number of video tracks. Integer between 1 and 8.

    video_stereo -- Stereoscopy. False for mono, True for stereo.

    width -- Integer between 24 and 16384.

    height -- Integer between 24 and 16384.

    ratio -- Frame aspect ratio. Float between 0.01 and 100.

    scan_mode -- Scan mode of the sequence. (F1, F2, P)

    frame_rate -- Frame rate. (60 fps, 59.54 NDF, 59.94 DF, 50 fps, 30 fps, 29.97 NDF, 29.97 DF, 25 fps, 24 fps, 23.976 fps)

    start_at -- Start timecode. The timecode format must be of the format specified by *frame_rate*.

    duration -- Can be an end timecode or an integer. If an end timecode, format must be of the format specified by *frame_rate*. If an integer, it represents a number of frames.

    audio_tracks -- Number of audio tracks. (0, 1, 2, 4, 8, 12, 16)

    audio_stereo -- Stereophony, apply to all *audio_tracks*. False for mono tracks, True for stereo.

---

### `get_wiretap_node_id`
```python
get_wiretap_node_id
```


get_wiretap_node_id( (PyArchiveEntry)arg1) -> str :

    Return the Wiretap Node ID of the Flame object, but only if the object is in the Media Panel.

---

### `get_wiretap_storage_id`
```python
get_wiretap_storage_id
```


get_wiretap_storage_id( (PyArchiveEntry)arg1) -> str :

    Return the Wiretap server's storage ID for the Flame object, but only if the object is in the Media Panel.

---
