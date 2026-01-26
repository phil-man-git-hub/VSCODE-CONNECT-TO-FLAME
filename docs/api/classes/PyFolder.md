# Class: PyFolder

**Module**: `flame`

Class derived from PyArchiveEntry. This class represents a Folder.

## Methods
### `children(...)`

None( (flame.PyFolder)arg1) -> list

### `folders(...)`

None( (flame.PyFolder)arg1) -> list

### `batch_iterations(...)`

None( (flame.PyFolder)arg1) -> list

### `desktops(...)`

None( (flame.PyFolder)arg1) -> list

### `reel_groups(...)`

None( (flame.PyFolder)arg1) -> list

### `reels(...)`

None( (flame.PyFolder)arg1) -> list

### `sequences(...)`

None( (flame.PyFolder)arg1) -> list

### `clips(...)`

None( (flame.PyFolder)arg1) -> list

### `batch_groups(...)`

None( (flame.PyFolder)arg1) -> list

### `clear(...)`

clear( (PyFolder)arg1 [, (bool)confirm=True]) -> bool :
    Clear the contents of the Folder object.

### `create_reel_group(...)`

create_reel_group( (PyFolder)arg1, (str)name) -> object :
    Create a new Reel Group object inside the Folder.

### `create_reel(...)`

create_reel( (PyFolder)arg1, (str)name) -> object :
    Create a new Reel object inside the Folder.

### `create_folder(...)`

create_folder( (PyFolder)arg1, (str)name) -> object :
    Create a new Folder object inside the Folder.

### `create_sequence(...)`

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

