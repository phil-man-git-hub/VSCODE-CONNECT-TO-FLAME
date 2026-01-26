
# Class: PyClip

**Module**: `flame`

## Inheritance & Hierarchy
* **Base class:** `PyArchiveEntry` (inherits from `PyFlameObject`)
* **Functional Role:** Represents a simple media asset or file reference in a Flame project.
* **Contained by:** `PyReel`, `PyFolder`, `PyLibrary`
* **Contains:** `PyVersion`

## Description
Represents a Clip, a media asset or file reference, as seen in the Media Panel.


## API Insight: Definition, Attributes, Methods, and Usage
The **PyClip** class is a fundamental object representing a media asset (clip, sequence, or timeline) stored in the Media Panel.

### Definition and Hierarchy
| Property      | Value         | Description |
|-------------- |-------------- |-------------|
| Class Name    | PyClip        | Represents a Clip. |
| Parent Class  | PyArchiveEntry| Inherits organizational management methods. |
| Primary Role  | Media Asset   | Represents a contiguous piece of media with defined characteristics. |
| Location      | Contained by PyReel | Typically located inside a PyReel. |

### Core Properties
| Attribute         | Type           | Access     | Description |
|-------------------|---------------|------------|-------------|
| duration          | int           | Read-only  | Duration of the clip in frames. |
| start_frame       | int           | Read/Write | Start frame of the clip's timeline. |
| end_frame         | int           | Read/Write | End frame of the clip's timeline. |
| frame_rate        | float         | Read-only  | Frame rate of the clip. |
| resolution        | PyResolution  | Read-only  | Details like width, height, scan format. |
| colour_space      | str           | Read/Write | Color space of the clip. |
| parent            | PyReel        | Read-only  | Container object. |
| attributes        | PyAttribute   | Read-only  | Metadata including name and colour. |

### Key Methods
| Method                | Arguments                        | Returns   | Description |
|-----------------------|----------------------------------|-----------|-------------|
| create_version()      | name                             | PyReel    | Create a new version in the parent group. |
| get_markers()         | None                             | list      | Get all markers associated with the clip. |
| import_setup()        | file_name                        | bool      | Load a clip setup file. |
| save_setup()          | file_name                        | bool      | Save the clip's current setup. |
| export_clip()         | path, file_name, ...             | PyExporter| Export the clip with specified parameters. |
| open()                | None                             | bool      | Open the clip in the application. |
| delete([confirm=True])| confirm                          | bool      | Delete the clip object. |

### Usage Context
PyClip objects are frequently targeted for automation, rendering, conforming, and metadata management.

```python
# Example: Checking clip length and resolution
# Assume 'clip' is a PyClip object

print(f"Clip Name: {clip.attributes.name}")
print(f"Duration: {clip.duration} frames")
print(f"Frame Rate: {clip.frame_rate} FPS")

res = clip.resolution
print(f"Resolution: {res.width}x{res.height}")

# Exporting a clip and checking result
# Many implementations return an exporter-like object or job handle
export_job = clip.export_clip(
    path="/mnt/exports/shot010",
    file_name="shot010_v003",
    options={'export_type': 'OpenEXR Sequence', 'colour_space':'Rec.709'}
)
if hasattr(export_job, 'execute'):
    export_job.execute([clip], '/mnt/exports')
else:
    print('Export job handle returned:', export_job)
```

## Attributes
| Attribute            | Type   | Description |
|----------------------|--------|-------------|
| name                 | str    | The name of an object in the Media Panel, resolving tokens if any are present. |
| shot_name            | str    | The shot name of an object in the Media Panel, resolving tokens if any are present. |
| tokenized_shot_name  | str    | The shot name including unresolved tokens, if present. |
| dynamic_shot_name    | str    | Dynamic attribute; auto-disabled when shot_name is set. Values: True/False |
| uid                  | str    | Unique identifier of the object in the Media Panel. |

---


## Methods
### Properties
- `frame_rate(...)` — None( (flame.PyClip)arg1) -> object 
None( (flame.PyClip)arg1) -> object

- `duration(...)` — None( (flame.PyClip)arg1) -> object 
None( (flame.PyClip)arg1) -> object

- `versions(...)` — None( (flame.PyClip)arg1) -> list 
None( (flame.PyClip)arg1) -> list

- `audio_tracks(...)` — None( (flame.PyClip)arg1) -> list 
None( (flame.PyClip)arg1) -> list

- `markers(...)` — None( (flame.PyClip)arg1) -> list 
None( (flame.PyClip)arg1) -> list

- `subtitles(...)` — None( (flame.PyClip)arg1) -> list 
None( (flame.PyClip)arg1) -> list

- `width(...)` — None( (flame.PyClip)arg1) -> int 
None( (flame.PyClip)arg1) -> int

- `height(...)` — None( (flame.PyClip)arg1) -> int 
None( (flame.PyClip)arg1) -> int

- `bit_depth(...)` — None( (flame.PyClip)arg1) -> int 
None( (flame.PyClip)arg1) -> int

- `ratio(...)` — None( (flame.PyClip)arg1) -> float 
None( (flame.PyClip)arg1) -> float

- `scan_mode(...)` — None( (flame.PyClip)arg1) -> str 
None( (flame.PyClip)arg1) -> str

- `colour_primaries(...)` — None( (flame.PyClip)arg1) -> int 
None( (flame.PyClip)arg1) -> int

- `transfer_characteristics(...)` — None( (flame.PyClip)arg1) -> int 
None( (flame.PyClip)arg1) -> int

- `matrix_coefficients(...)` — None( (flame.PyClip)arg1) -> int 
None( (flame.PyClip)arg1) -> int

- `proxy_resolution(...)` — None( (flame.PyClip)arg1) -> object 
None( (flame.PyClip)arg1) -> object

- `has_deliverables(...)` — None( (flame.PyClip)arg1) -> bool 
None( (flame.PyClip)arg1) -> bool

- `has_history(...)` — None( (flame.PyClip)arg1) -> bool 
None( (flame.PyClip)arg1) -> bool

- `unlinked(...)` — None( (flame.PyClip)arg1) -> str 
None( (flame.PyClip)arg1) -> str

- `creation_date(...)` — None( (flame.PyClip)arg1) -> str 
None( (flame.PyClip)arg1) -> str

- `archive_date(...)` — None( (flame.PyClip)arg1) -> str 
None( (flame.PyClip)arg1) -> str

- `archive_error(...)` — None( (flame.PyClip)arg1) -> str 
None( (flame.PyClip)arg1) -> str

- `essence_uid(...)` — None( (flame.PyClip)arg1) -> str 
None( (flame.PyClip)arg1) -> str

- `source_uid(...)` — None( (flame.PyClip)arg1) -> str 
None( (flame.PyClip)arg1) -> str

- `original_source_uid(...)` — None( (flame.PyClip)arg1) -> str 
None( (flame.PyClip)arg1) -> str

- `sample_rate(...)` — None( (flame.PyClip)arg1) -> str 
None( (flame.PyClip)arg1) -> str

- `cached(...)` — None( (flame.PyClip)arg1) -> str 
None( (flame.PyClip)arg1) -> str

- `start_frame(...)` — None( (flame.PyClip)arg1) -> int 
None( (flame.PyClip)arg1) -> int


### Built-in methods
- `open_as_sequence(...)` — open_as_sequence( (PyClip)arg1) -> object : 
open_as_sequence( (PyClip)arg1) -> object :
    Open the Clip as a Sequence. Mutates the PyClip object into a PySequence object.

- `open_container(...)` — open_container( (PyClip)arg1) -> bool : 
open_container( (PyClip)arg1) -> bool :
    Open the container timeline if the Clip is inside a container.

- `close_container(...)` — close_container( (PyClip)arg1) -> None : 
close_container( (PyClip)arg1) -> None :
    Close the container timeline if the Clip is inside a container.

- `reformat(...)` — reformat( (PyClip)arg1 [, (int)width=0 [, (int)height=0 [, (float)ratio=0.0 [, (int)bit_depth=0 [, (str)scan_mode='' [, (str)frame_rate='' [, (str)resize_mode='Letterbox']]]]]]]) -> None : 
reformat( (PyClip)arg1 [, (int)width=0 [, (int)height=0 [, (float)ratio=0.0 [, (int)bit_depth=0 [, (str)scan_mode='' [, (str)frame_rate='' [, (str)resize_mode='Letterbox']]]]]]]) -> None :
    Reformat the Clip to the specified format.
    Keywords arguments:
    width -- Integer between 24 and 16384.
    height -- Integer between 24 and 16384.
    ratio -- Frame aspect ratio. Float between 0.01 and 100.
    bit_depth -- Bit depth. (8, 10, 12, 16 or 32)
    scan_mode -- Scan mode of the sequence. (F1, F2, P)
    frame_rate -- Frame rate. (60 fps, 59.54 NDF, 59.94 DF, 50 fps, 30 fps, 29.97 NDF, 29.97 DF, 25 fps, 24 fps, 23.976 fps)
    resize_mode -- Resize mode. (Letterbox, Crop Edges, Fill, Centre)

- `create_marker(...)` — create_marker( (PyClip)arg1, (object)location) -> object : 
create_marker( (PyClip)arg1, (object)location) -> object :
    Add a Marker to the Clip.Keyword argument:
    location -- The frame where the marker gets created.

- `change_dominance(...)` — change_dominance( (PyClip)arg1, (str)scan_mode) -> None : 
change_dominance( (PyClip)arg1, (str)scan_mode) -> None :
    Change the Clip's dominance. Changes only the clip's metadata.
    Keyword argument:
    scan_mode -- Field dominance. (P, F1, F2)

- `cache_media(...)` — cache_media( (PyClip)arg1 [, (str)mode='current']) -> bool : 
cache_media( (PyClip)arg1 [, (str)mode='current']) -> bool :
    Cache the Clip's linked media.
    Keyword argument:
    mode -- Determine the version to cache (currently selected or all versions). All Versions is only useful with to multi-version clips (Current, All Versions)

- `flush_cache_media(...)` — flush_cache_media( (PyClip)arg1 [, (str)mode='current']) -> bool : 
flush_cache_media( (PyClip)arg1 [, (str)mode='current']) -> bool :
    Clear the Clip's media cache.
    Keyword argument:
    mode -- Determine the version's cache to clear. (Current, All Versions, All But Current)(Deprecated: use 'clear_cache_media' instead.)

- `clear_cache_media(...)` — clear_cache_media( (PyClip)arg1 [, (str)mode='current']) -> bool : 
clear_cache_media( (PyClip)arg1 [, (str)mode='current']) -> bool :
    Clear the Clip's media cache.
    Keyword argument:
    mode -- Determine the version's cache to clear. (Current, All Versions, All But Current)

- `render(...)` — render( (PyClip)arg1 [, (str)render_mode='All' [, (str)render_option='Foreground' [, (str)render_quality='Full Resolution' [, (str)effect_type='' [, (str)effect_caching_mode='Current' [, (bool)include_handles=False]]]]]]) -> bool : 
render( (PyClip)arg1 [, (str)render_mode='All' [, (str)render_option='Foreground' [, (str)render_quality='Full Resolution' [, (str)effect_type='' [, (str)effect_caching_mode='Current' [, (bool)include_handles=False]]]]]]) -> bool :
    Trigger a render of the Clip
    The following attributes can be defined: render_mode, render_option, render_quality, effect_type, effect_caching_mode and include_handles.

- `flush_renders(...)` — flush_renders( (PyClip)arg1) -> None : 
flush_renders( (PyClip)arg1) -> None :
    Clear the Clip's Timeline FX renders.(Deprecated: use 'clear_renders' instead.)

- `clear_renders(...)` — clear_renders( (PyClip)arg1) -> None : 
clear_renders( (PyClip)arg1) -> None :
    Clear the Clip's Timeline FX renders.

- `is_rendered(...)` — is_rendered( (PyClip)arg1 [, (bool)top_only=False [, (str)render_quality='Full Resolution']]) -> bool : 
is_rendered( (PyClip)arg1 [, (bool)top_only=False [, (str)render_quality='Full Resolution']]) -> bool :
    Return if a Clip is rendered.
    The following attributes can be defined: top_only, render_quality.

- `save(...)` — save( (PyClip)arg1) -> bool : 
save( (PyClip)arg1) -> bool :
    Save the Clip to the defined save destination.

- `cut(...)` — cut( (PyClip)arg1, (PyTime)cut_time) -> None : 
cut( (PyClip)arg1, (PyTime)cut_time) -> None :
    Cut all tracks of the Clip.

- `get_colour_space(...)` — get_colour_space( (PyClip)arg1 [, (PyTime)time=None]) -> str : 
get_colour_space( (PyClip)arg1 [, (PyTime)time=None]) -> str :
    Return the colour space at the requested time. Use current_time when no time is supplied.

- `change_start_frame(...)` — change_start_frame( (PyClip)arg1, (int)start_frame [, (bool)use_segment_connections=True]) -> None : 
change_start_frame( (PyClip)arg1, (int)start_frame [, (bool)use_segment_connections=True]) -> None :
    Modify the start frame of a source Clip.
    Keywords argument:
    start_frame -- New start frame of the clip.
    use_segment_connections -- Sync the start frame of connected segments.

- `export_clip(...)` — export_clip( (PyClip)arg1, (str)path, (str)file_name [, (dict)options={}]) -> object : 
export_clip( (PyClip)arg1, (str)path, (str)file_name [, (dict)options={}]) -> object :
    Initiate an export of the Clip using the provided parameters. Returns a `PyExporter`-like object or export job handle. Keyword arguments:
    path -- Destination directory for the exported files.
    file_name -- Base filename or template to use for output.
    options -- Optional dictionary containing export settings (format, codec, color_space, render_quality, include_handles, etc.).

- `get_metadata(...)` — get_metadata( (PyClip)arg1 [, (str)key='' [, (PyTime)time=None]]) -> object : 
get_metadata( (PyClip)arg1 [, (str)key='' [, (PyTime)time=None]]) -> object :
    Return the metadata of the clip.
    Keywords argument:
    key -- Key of the requested metadata. All metadata is returned when not specified.
    time -- Must be a PyTime. If not specified, the current clip time is used.


