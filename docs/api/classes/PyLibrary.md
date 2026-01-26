
# Class: PyLibrary

**Module**: `flame`

## Inheritance & Hierarchy
* **Base class:** `PyArchiveEntry` (inherits from `PyFlameObject`)
* **Functional Role:** The central shared media container in a Flame project.
* **Contained by:** `PyProject`
* **Contains:** `PyFolder`, `PyReelGroup`, `PyReel`

## Description
Represents a Library, a top-level container for organizing media, folders, reels, and sequences in a Flame project.


## API Insight: Definition, Attributes, Methods, and Usage
The **PyLibrary** class represents a Shared Library container, serving as a top-level collaborative structure for media and folders.

### Definition and Hierarchy
| Property      | Value         | Description |
|-------------- |-------------- |-------------|
| Class Name    | PyLibrary     | Shared Library container. |
| Parent Class  | PyArchiveEntry| Inherits foundational attributes and methods. |
| Grandparent   | PyFlameObject | Inherits base attributes and parent property. |
| Primary Role  | Shared Media Container | Top-level container for folders and reel groups. |
| Location      | Contained by PyProject | Direct child of the project object. |

### Inherited and Core Attributes
| Attribute         | Type           | Access     | Inherited From | Description |
|-------------------|---------------|------------|---------------|-------------|
| attributes        | PyAttribute    | Read-only  | PyFlameObject | Dynamic access to object properties. |
| parent            | PyProject      | Read-only  | PyFlameObject | Container project object. |
| id                | str            | Read-only  | PyArchiveEntry| Unique database identifier. |
| name              | str            | Read/Write | PyArchiveEntry| Display name in the Media Panel. |
| online            | bool           | Read-only  | PyArchiveEntry| Database entry availability. |

### Container and Management Methods
| Method                | Arguments                        | Returns   | Description |
|-----------------------|----------------------------------|-----------|-------------|
| create_folder()       | name                             | PyFolder  | Create a folder inside the library. |
| create_reel_group()   | name                             | PyReelGroup| Create a reel group inside the library. |
| get_children()        | None                             | list      | List all immediate children. |
| delete([confirm=True])| confirm                          | bool      | Delete the library. |
| duplicate()           | None                             | PyLibrary | Duplicate the library and contents. |
| move()                | destination                      | bool      | Move the library to a new container. |

### Usage Context
PyLibrary is used in automation scripts to manage shared resources and structure project organization, often accessed after retrieving the PyProject object.

**Example:**

```python
library = flame.project.library
# Acquire exclusive access to the library if needed
if library.acquire_exclusive_access():
    assets = library.create_folder('01_ASSETS')
    render_grp = library.create_reel_group('02_RENDERS')
    library.release_exclusive_access()
```


## Attributes
| Attribute    | Type   | Description |
|--------------|--------|-------------|
| name         | str    | The name of an object in the Media Panel, resolving tokens if any are present. |
| uid          | str    | The unique identifier of an object in the Media Panel. |
| token_name   | str    | The tokenized name of an object in the Media Panel. |
| expanded     | bool   | The expanded state of an object in the Media Panel. Values: True/False |
| colour       | tuple  | The colour of an object in the Media Panel. |

---


## Methods
### Properties
- `children(...)` — None( (flame.PyLibrary)arg1) -> list 
None( (flame.PyLibrary)arg1) -> list

- `folders(...)` — None( (flame.PyLibrary)arg1) -> list 
None( (flame.PyLibrary)arg1) -> list

- `batch_iterations(...)` — None( (flame.PyLibrary)arg1) -> list 
None( (flame.PyLibrary)arg1) -> list

- `desktops(...)` — None( (flame.PyLibrary)arg1) -> list 
None( (flame.PyLibrary)arg1) -> list

- `reel_groups(...)` — None( (flame.PyLibrary)arg1) -> list 
None( (flame.PyLibrary)arg1) -> list

- `reels(...)` — None( (flame.PyLibrary)arg1) -> list 
None( (flame.PyLibrary)arg1) -> list

- `sequences(...)` — None( (flame.PyLibrary)arg1) -> list 
None( (flame.PyLibrary)arg1) -> list

- `clips(...)` — None( (flame.PyLibrary)arg1) -> list 
None( (flame.PyLibrary)arg1) -> list

- `batch_groups(...)` — None( (flame.PyLibrary)arg1) -> list 
None( (flame.PyLibrary)arg1) -> list

- `opened(...)` — None( (flame.PyLibrary)arg1) -> bool 
None( (flame.PyLibrary)arg1) -> bool


### Built-in methods
- `open(...)` — open( (PyLibrary)arg1) -> bool : 
open( (PyLibrary)arg1) -> bool :
    Open a Library and load it in the application memory. Until a Library is open, it cannot be accessed. Libraries are created open.

- `close(...)` — close( (PyLibrary)arg1) -> bool : 
close( (PyLibrary)arg1) -> bool :
    Close a Library to release it from the application memory.

- `clear(...)` — clear( (PyLibrary)arg1 [, (bool)confirm=True]) -> bool : 
clear( (PyLibrary)arg1 [, (bool)confirm=True]) -> bool :
    Clear the Library's contents.

- `acquire_exclusive_access(...)` — acquire_exclusive_access( (PyLibrary)arg1) -> bool : 
acquire_exclusive_access( (PyLibrary)arg1) -> bool :
    Acquire exclusive access to the Shared Library. Shared Libraries are created locked. Only use with Shared Libraries.

- `release_exclusive_access(...)` — release_exclusive_access( (PyLibrary)arg1) -> bool : 
release_exclusive_access( (PyLibrary)arg1) -> bool :
    Release exclusive access to the Shared Library. Only used for Shared Libraries. Only use with Shared Libraries.

- `create_reel_group(...)` — create_reel_group( (PyLibrary)arg1, (str)name) -> object : 
create_reel_group( (PyLibrary)arg1, (str)name) -> object :
    Create a Reel Group inside a Library.

- `create_reel(...)` — create_reel( (PyLibrary)arg1, (str)name) -> object : 
create_reel( (PyLibrary)arg1, (str)name) -> object :
    Create a Reel inside a Library.

- `create_folder(...)` — create_folder( (PyLibrary)arg1, (str)name) -> object : 
create_folder( (PyLibrary)arg1, (str)name) -> object :
    Create a Folder inside a Library.

- `create_sequence(...)` — create_sequence( (PyLibrary)arg1 [, (str)name='Untitled Sequence' [, (int)video_tracks=1 [, (bool)video_stereo=False [, (object)width=None [, (object)height=None [, (object)ratio=None [, (object)bit_depth=None [, (object)scan_mode=None [, (object)frame_rate=None [, (object)start_at=00:00:00+00 [, (object)duration=00:00:00+01 [, (int)audio_tracks=1 [, (bool)audio_stereo=True]]]]]]]]]]]]]) -> object : 
create_sequence( (PyLibrary)arg1 [, (str)name='Untitled Sequence' [, (int)video_tracks=1 [, (bool)video_stereo=False [, (object)width=None [, (object)height=None [, (object)ratio=None [, (object)bit_depth=None [, (object)scan_mode=None [, (object)frame_rate=None [, (object)start_at=00:00:00+00 [, (object)duration=00:00:00+01 [, (int)audio_tracks=1 [, (bool)audio_stereo=True]]]]]]]]]]]]]) -> object :
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


