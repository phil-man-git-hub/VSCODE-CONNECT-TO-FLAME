# Class: PyClip

**Module**: `flame`

CLass derived from PyArchiveEntry. This class represents a Clip.

## Methods
### `frame_rate(...)`

None( (flame.PyClip)arg1) -> object

### `duration(...)`

None( (flame.PyClip)arg1) -> object

### `versions(...)`

None( (flame.PyClip)arg1) -> list

### `audio_tracks(...)`

None( (flame.PyClip)arg1) -> list

### `markers(...)`

None( (flame.PyClip)arg1) -> list

### `subtitles(...)`

None( (flame.PyClip)arg1) -> list

### `width(...)`

None( (flame.PyClip)arg1) -> int

### `height(...)`

None( (flame.PyClip)arg1) -> int

### `bit_depth(...)`

None( (flame.PyClip)arg1) -> int

### `ratio(...)`

None( (flame.PyClip)arg1) -> float

### `scan_mode(...)`

None( (flame.PyClip)arg1) -> str

### `colour_primaries(...)`

None( (flame.PyClip)arg1) -> int

### `transfer_characteristics(...)`

None( (flame.PyClip)arg1) -> int

### `matrix_coefficients(...)`

None( (flame.PyClip)arg1) -> int

### `proxy_resolution(...)`

None( (flame.PyClip)arg1) -> object

### `has_deliverables(...)`

None( (flame.PyClip)arg1) -> bool

### `has_history(...)`

None( (flame.PyClip)arg1) -> bool

### `unlinked(...)`

None( (flame.PyClip)arg1) -> str

### `creation_date(...)`

None( (flame.PyClip)arg1) -> str

### `archive_date(...)`

None( (flame.PyClip)arg1) -> str

### `archive_error(...)`

None( (flame.PyClip)arg1) -> str

### `essence_uid(...)`

None( (flame.PyClip)arg1) -> str

### `source_uid(...)`

None( (flame.PyClip)arg1) -> str

### `original_source_uid(...)`

None( (flame.PyClip)arg1) -> str

### `sample_rate(...)`

None( (flame.PyClip)arg1) -> str

### `cached(...)`

None( (flame.PyClip)arg1) -> str

### `start_frame(...)`

None( (flame.PyClip)arg1) -> int

### `open_as_sequence(...)`

open_as_sequence( (PyClip)arg1) -> object :
    Open the Clip as a Sequence. Mutates the PyClip object into a PySequence object.

### `open_container(...)`

open_container( (PyClip)arg1) -> bool :
    Open the container timeline if the Clip is inside a container.

### `close_container(...)`

close_container( (PyClip)arg1) -> None :
    Close the container timeline if the Clip is inside a container.

### `reformat(...)`

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

### `create_marker(...)`

create_marker( (PyClip)arg1, (object)location) -> object :
    Add a Marker to the Clip.Keyword argument:
    location -- The frame where the marker gets created.

### `change_dominance(...)`

change_dominance( (PyClip)arg1, (str)scan_mode) -> None :
    Change the Clip's dominance. Changes only the clip's metadata.
    Keyword argument:
    scan_mode -- Field dominance. (P, F1, F2)

### `cache_media(...)`

cache_media( (PyClip)arg1 [, (str)mode='current']) -> bool :
    Cache the Clip's linked media.
    Keyword argument:
    mode -- Determine the version to cache (currently selected or all versions). All Versions is only useful with to multi-version clips (Current, All Versions)

### `flush_cache_media(...)`

flush_cache_media( (PyClip)arg1 [, (str)mode='current']) -> bool :
    Clear the Clip's media cache.
    Keyword argument:
    mode -- Determine the version's cache to clear. (Current, All Versions, All But Current)(Deprecated: use 'clear_cache_media' instead.)
    

### `clear_cache_media(...)`

clear_cache_media( (PyClip)arg1 [, (str)mode='current']) -> bool :
    Clear the Clip's media cache.
    Keyword argument:
    mode -- Determine the version's cache to clear. (Current, All Versions, All But Current)

### `render(...)`

render( (PyClip)arg1 [, (str)render_mode='All' [, (str)render_option='Foreground' [, (str)render_quality='Full Resolution' [, (str)effect_type='' [, (str)effect_caching_mode='Current' [, (bool)include_handles=False]]]]]]) -> bool :
    Trigger a render of the Clip
    The following attributes can be defined: render_mode, render_option, render_quality, effect_type, effect_caching_mode and include_handles.

### `flush_renders(...)`

flush_renders( (PyClip)arg1) -> None :
    Clear the Clip's Timeline FX renders.(Deprecated: use 'clear_renders' instead.)
    

### `clear_renders(...)`

clear_renders( (PyClip)arg1) -> None :
    Clear the Clip's Timeline FX renders.

### `is_rendered(...)`

is_rendered( (PyClip)arg1 [, (bool)top_only=False [, (str)render_quality='Full Resolution']]) -> bool :
    Return if a Clip is rendered.
    The following attributes can be defined: top_only, render_quality.

### `save(...)`

save( (PyClip)arg1) -> bool :
    Save the Clip to the defined save destination.

### `cut(...)`

cut( (PyClip)arg1, (PyTime)cut_time) -> None :
    Cut all tracks of the Clip.

### `get_colour_space(...)`

get_colour_space( (PyClip)arg1 [, (PyTime)time=None]) -> str :
    Return the colour space at the requested time. Use current_time when no time is supplied.

### `change_start_frame(...)`

change_start_frame( (PyClip)arg1, (int)start_frame [, (bool)use_segment_connections=True]) -> None :
    Modify the start frame of a source Clip.
    Keywords argument:
    start_frame -- New start frame of the clip.
    use_segment_connections -- Sync the start frame of connected segments.
    

### `get_metadata(...)`

get_metadata( (PyClip)arg1 [, (str)key='' [, (PyTime)time=None]]) -> object :
    Return the metadata of the clip.
    Keywords argument:
    key -- Key of the requested metadata. All metadata is returned when not specified.
    time -- Must be a PyTime. If not specified, the current clip time is used.

