# Class: PyClip

**Module**: `flame`

**Inherits from**: [PyArchiveEntry](PyArchiveEntry.md), [PyFlameObject](PyFlameObject.md), instance, object

## Description
CLass derived from PyArchiveEntry. This class represents a Clip.


## Properties
| Name | Description |
| --- | --- |
| `archive_date` | Return the Clip's last archive date. |
| `archive_error` | Return the Clip's last archive error. |
| `attributes` | The attributes of a python object. |
| `audio_tracks` | Return a list of the Clip's Audio Tracks. |
| `bit_depth` | Return the Clip's bit depth. |
| `cached` | Return the Clip's cache status. |
| `colour_primaries` | Deduce the Clip's 'colour primaries' export attribute. |
| `creation_date` | Return the Clip's creation date. |
| `duration` | Return the Clip's duration. |
| `essence_uid` | Return the Clip's essence uid. |
| `frame_rate` | Return the Clip's frame rate. |
| `has_deliverables` | Return the existence of deliverables on the Clip. |
| `has_history` | Return the existence of history inside the Clip. |
| `height` | Return the Clip's height. |
| `markers` | Return a list of the Clip's Markers. |
| `matrix_coefficients` | Deduce the Clip's 'matrix coefficients' export attribute. |
| `original_source_uid` | Return the Clip's original source UID. |
| `parent` | The parent object of this object. |
| `proxy_resolution` | Return the Clip's proxy resolution if it has proxies. |
| `ratio` | Return the Clip's frame ratio. |
| `sample_rate` | Return the Clip's audio sample rate. |
| `scan_mode` | Return the Clip's scan mode. |
| `source_uid` | Return the Clip's source uid. |
| `start_frame` | Return the Clip's start frame. |
| `subtitles` | Return a list of the Clip's Subtitles Tracks. |
| `transfer_characteristics` | Deduce the Clip's 'transfer characteristics' export attribute. |
| `unlinked` | Return the Clip's unlinked status. |
| `versions` | Return a list of the Clip's versions. |
| `width` | Return the Clip's width. |


## Methods
### `cache_media`
```python
cache_media
```


cache_media( (PyClip)arg1 [, (str)mode='current']) -> bool :

    Cache the Clip's linked media.

    Keyword argument:

    mode -- Determine the version to cache (currently selected or all versions). All Versions is only useful with to multi-version clips (Current, All Versions)

---

### `change_dominance`
```python
change_dominance
```


change_dominance( (PyClip)arg1, (str)scan_mode) -> None :

    Change the Clip's dominance. Changes only the clip's metadata.

    Keyword argument:

    scan_mode -- Field dominance. (P, F1, F2)

---

### `change_start_frame`
```python
change_start_frame
```


change_start_frame( (PyClip)arg1, (int)start_frame [, (bool)use_segment_connections=True]) -> None :

    Modify the start frame of a source Clip.

    Keywords argument:

    start_frame -- New start frame of the clip.

    use_segment_connections -- Sync the start frame of connected segments.

    

---

### `clear_cache_media`
```python
clear_cache_media
```


clear_cache_media( (PyClip)arg1 [, (str)mode='current']) -> bool :

    Clear the Clip's media cache.

    Keyword argument:

    mode -- Determine the version's cache to clear. (Current, All Versions, All But Current)

---

### `clear_colour`
```python
clear_colour
```


clear_colour( (PyArchiveEntry)arg1) -> None :

    Clear the colour of an object in the Media Panel.

---

### `clear_renders`
```python
clear_renders
```


clear_renders( (PyClip)arg1) -> None :

    Clear the Clip's Timeline FX renders.

---

### `close_container`
```python
close_container
```


close_container( (PyClip)arg1) -> None :

    Close the container timeline if the Clip is inside a container.

---

### `commit`
```python
commit
```


commit( (PyArchiveEntry)arg1) -> None :

    Commit to disk the Media Panel object or its closest container possible.

---

### `create_marker`
```python
create_marker
```


create_marker( (PyClip)arg1, (object)location) -> object :

    Add a Marker to the Clip.Keyword argument:

    location -- The frame where the marker gets created.

---

### `cut`
```python
cut
```


cut( (PyClip)arg1, (PyTime)cut_time) -> None :

    Cut all tracks of the Clip.

---

### `flush_cache_media`
```python
flush_cache_media
```


flush_cache_media( (PyClip)arg1 [, (str)mode='current']) -> bool :

    Clear the Clip's media cache.

    Keyword argument:

    mode -- Determine the version's cache to clear. (Current, All Versions, All But Current)(Deprecated: use 'clear_cache_media' instead.)

    

---

### `flush_renders`
```python
flush_renders
```


flush_renders( (PyClip)arg1) -> None :

    Clear the Clip's Timeline FX renders.(Deprecated: use 'clear_renders' instead.)

    

---

### `get_colour_space`
```python
get_colour_space
```


get_colour_space( (PyClip)arg1 [, (PyTime)time=None]) -> str :

    Return the colour space at the requested time. Use current_time when no time is supplied.

---

### `get_metadata`
```python
get_metadata
```


get_metadata( (PyClip)arg1 [, (str)key='' [, (PyTime)time=None]]) -> object :

    Return the metadata of the clip.

    Keywords argument:

    key -- Key of the requested metadata. All metadata is returned when not specified.

    time -- Must be a PyTime. If not specified, the current clip time is used.

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

### `is_rendered`
```python
is_rendered
```


is_rendered( (PyClip)arg1 [, (bool)top_only=False [, (str)render_quality='Full Resolution']]) -> bool :

    Return if a Clip is rendered.

    The following attributes can be defined: top_only, render_quality.

---

### `open_as_sequence`
```python
open_as_sequence
```


open_as_sequence( (PyClip)arg1) -> object :

    Open the Clip as a Sequence. Mutates the PyClip object into a PySequence object.

---

### `open_container`
```python
open_container
```


open_container( (PyClip)arg1) -> bool :

    Open the container timeline if the Clip is inside a container.

---

### `reformat`
```python
reformat
```


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

---

### `render`
```python
render
```


render( (PyClip)arg1 [, (str)render_mode='All' [, (str)render_option='Foreground' [, (str)render_quality='Full Resolution' [, (str)effect_type='' [, (str)effect_caching_mode='Current' [, (bool)include_handles=False]]]]]]) -> bool :

    Trigger a render of the Clip

    The following attributes can be defined: render_mode, render_option, render_quality, effect_type, effect_caching_mode and include_handles.

---

### `save`
```python
save
```


save( (PyClip)arg1) -> bool :

    Save the Clip to the defined save destination.

---
