
# Class: PyReel

**Module**: `flame`

## Inheritance & Hierarchy
* **Base Class:** PyFlameObject
* **Contained By:** PyReelGroup, PyLibrary, PyFolder

## Functional Role & Context
* **Functional Role:** Represents a Reel, providing access to sequences, clips, and child objects.
* **Context:** Used for organizing, creating, and managing sequences and clips in the Flame environment.

## Description
The PyReel class provides programmatic access to reels, supporting automation of sequence and clip management, and organization in libraries and folders.


Object representing a Reel.

## API Insight
### Autodesk Flame API Insight (2026)

`PyReel` is a container representing a single version of an asset, holding the actual media objects (e.g., `PyClip`, `PySequence`). It is typically accessed as a child of a `PyReelGroup`.

**Core members & behaviour:**
- `children`, `clips`, `sequences` — access the contained media items.
- `is_current` (bool) — mark this reel as the current version in its `PyReelGroup`.
- `get_clips()`, `get_sequences()` — convenience accessors for contained media.

**Example:**

```python
# Mark a reel as the current version and inspect its media
shot_group = my_folder.get_item('SHOT_010')
v002 = shot_group.reels[1]
v002.is_current = True
current = v002.get_clips()[0]
print('Current clip:', current.attributes.name)
```

## Attributes
| Attribute   | Type   | Description |
|-------------|--------|-------------|
| name        | str    | The name of an object in the Media Panel, resolving tokens if any are present. |
| uid         | str    | The unique identifier of an object in the Media Panel. |
| token_name  | str    | The tokenized name of an object in the Media Panel. |
| expanded    | bool   | The expanded state of an object in the Media Panel. True or False. |
| colour      | tuple  | The colour of an object in the Media Panel. |

## Methods
### Properties
- `children(...)` — None( (flame.PyReel)arg1) -> list 
None( (flame.PyReel)arg1) -> list

- `sequences(...)` — None( (flame.PyReel)arg1) -> list 
None( (flame.PyReel)arg1) -> list

- `clips(...)` — None( (flame.PyReel)arg1) -> list 
None( (flame.PyReel)arg1) -> list

- `type(...)` — None( (flame.PyReel)arg1) -> object 
None( (flame.PyReel)arg1) -> object


### Built-in methods
- `clear(...)` — clear( (PyReel)arg1 [, (bool)confirm=True]) -> bool : 
clear( (PyReel)arg1 [, (bool)confirm=True]) -> bool :
    Clear the Reel content.

- `create_sequence(...)` — create_sequence( (PyReel)arg1 [, (str)name='Untitled Sequence' [, (int)video_tracks=1 [, (bool)video_stereo=False [, (object)width=None [, (object)height=None [, (object)ratio=None [, (object)bit_depth=None [, (object)scan_mode=None [, (object)frame_rate=None [, (object)start_at=00:00:00+00 [, (object)duration=00:00:00+01 [, (int)audio_tracks=1 [, (bool)audio_stereo=True]]]]]]]]]]]]]) -> object : 
create_sequence( (PyReel)arg1 [, (str)name='Untitled Sequence' [, (int)video_tracks=1 [, (bool)video_stereo=False [, (object)width=None [, (object)height=None [, (object)ratio=None [, (object)bit_depth=None [, (object)scan_mode=None [, (object)frame_rate=None [, (object)start_at=00:00:00+00 [, (object)duration=00:00:00+01 [, (int)audio_tracks=1 [, (bool)audio_stereo=True]]]]]]]]]]]]]) -> object :
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

- `save(...)` — save( (PyReel)arg1) -> bool : 
save( (PyReel)arg1) -> bool :
    Save the Reel to the defined save destination.


