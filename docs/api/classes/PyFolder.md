
# Class: PyFolder

**Module**: `flame`

## Inheritance & Hierarchy
* **Base class:** `PyArchiveEntry` (inherits from `PyFlameObject`)
* **Functional Role:** Generic container for organization in a Flame project.
* **Contained by:** `PyLibrary`, `PyFolder`, `PyDesktop`
* **Contains:** Nested `PyFolder`s, `PyReelGroup`, `PyReel`, `PyClip`, `PySequence`

## Description
Represents a Folder, used to organize media, reels, and sequences within a Library or Desktop.


## API Insight: Definition, Attributes, Methods, and Usage
The **PyFolder** class represents a standard organizational folder, serving as a container for other objects and media elements in the Media Panel.

### Definition and Hierarchy
| Property      | Value         | Description |
|-------------- |-------------- |-------------|
| Class Name    | PyFolder      | Object representing a Folder. |
| Parent Class  | PyArchiveEntry| Inherits foundational media management attributes and methods. |
| Primary Role  | Organizational Container | Used for nested hierarchy and grouping media. |

### Inherited and Core Attributes
| Attribute         | Type           | Access     | Inherited From | Description |
|-------------------|---------------|------------|---------------|-------------|
| attributes        | PyAttribute    | Read-only  | PyFlameObject | Dynamic properties (name, colour, etc.). |
| parent            | PyArchiveEntry | Read-only  | PyFlameObject | Container object. |
| id                | str            | Read-only  | PyArchiveEntry| Unique database identifier. |
| name              | str            | Read/Write | PyArchiveEntry| Display name of the folder. |
| colour            | tuple          | Read/Write | PyArchiveEntry| Color label in the UI. |

### Container and Management Methods
| Method                | Arguments                        | Returns   | Description |
|-----------------------|----------------------------------|-----------|-------------|
| create_folder()       | name                             | PyFolder  | Create a nested folder. |
| create_reel_group()   | name                             | PyReelGroup| Create a Reel Group inside the folder. |
| get_children()        | None                             | list      | List all objects directly contained. |
| delete([confirm=True])| confirm                          | bool      | Delete the folder and its contents. |
| duplicate()           | None                             | PyFolder  | Duplicate the folder and its contents. |
| move()                | destination                      | bool      | Move the folder to a new container. |

### Usage Context
PyFolder is the building block for organizational scripts, enabling deep folder structures for media management.

```python
# Example: Creating a nested folder structure
# Assume 'desktop' is a PyDesktop object (e.g., flame.project.desktop)

client_folder = desktop.create_folder("CLIENT_X_SHOW")

# Create a sub-folder for editorial sequences
edit_folder = client_folder.create_folder("EDL_TIMELINES")

# Create a sub-folder for rendered outputs
renders_folder = client_folder.create_folder("RENDERS")
```

**Notes**
- The `colour` attribute is stored as an `(R, G, B, A)` tuple.
- Use `create_reel_group()` when grouping multiple reel versions inside folders.

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
- `children(...)` — None( (flame.PyFolder)arg1) -> list 
None( (flame.PyFolder)arg1) -> list

- `folders(...)` — None( (flame.PyFolder)arg1) -> list 
None( (flame.PyFolder)arg1) -> list

- `batch_iterations(...)` — None( (flame.PyFolder)arg1) -> list 
None( (flame.PyFolder)arg1) -> list

- `desktops(...)` — None( (flame.PyFolder)arg1) -> list 
None( (flame.PyFolder)arg1) -> list

- `reel_groups(...)` — None( (flame.PyFolder)arg1) -> list 
None( (flame.PyFolder)arg1) -> list

- `reels(...)` — None( (flame.PyFolder)arg1) -> list 
None( (flame.PyFolder)arg1) -> list

- `sequences(...)` — None( (flame.PyFolder)arg1) -> list 
None( (flame.PyFolder)arg1) -> list

- `clips(...)` — None( (flame.PyFolder)arg1) -> list 
None( (flame.PyFolder)arg1) -> list

- `batch_groups(...)` — None( (flame.PyFolder)arg1) -> list 
None( (flame.PyFolder)arg1) -> list


### Built-in methods
- `clear(...)` — clear( (PyFolder)arg1 [, (bool)confirm=True]) -> bool : 
clear( (PyFolder)arg1 [, (bool)confirm=True]) -> bool :
    Clear the contents of the Folder object.

- `create_reel_group(...)` — create_reel_group( (PyFolder)arg1, (str)name) -> object : 
create_reel_group( (PyFolder)arg1, (str)name) -> object :
    Create a new Reel Group object inside the Folder.

- `create_reel(...)` — create_reel( (PyFolder)arg1, (str)name) -> object : 
create_reel( (PyFolder)arg1, (str)name) -> object :
    Create a new Reel object inside the Folder.

- `create_folder(...)` — create_folder( (PyFolder)arg1, (str)name) -> object : 
create_folder( (PyFolder)arg1, (str)name) -> object :
    Create a new Folder object inside the Folder.

- `create_sequence(...)` — create_sequence( (PyFolder)arg1 [, (str)name='Untitled Sequence' [, (int)video_tracks=1 [, (bool)video_stereo=False [, (object)width=None [, (object)height=None [, (object)ratio=None [, (object)bit_depth=None [, (object)scan_mode=None [, (object)frame_rate=None [, (object)start_at=00:00:00+00 [, (object)duration=00:00:00+01 [, (int)audio_tracks=1 [, (bool)audio_stereo=True]]]]]]]]]]]]]) -> object : 
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


