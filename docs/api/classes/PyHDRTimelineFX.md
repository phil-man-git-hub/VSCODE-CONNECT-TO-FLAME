# Class: PyHDRTimelineFX

**Module**: `flame`

**Inherits from**: [PyTimelineFX](PyTimelineFX.md), [PyFlameObject](PyFlameObject.md), instance, object

## Description
Object representing a HDR Timeline FX.


## Properties
| Name | Description |
| --- | --- |
| `analysis_status` | Return the current state of the HDR analysis. |
| `attributes` | The attributes of a python object. |
| `has_maps_cache_media` | Return whether the Timeline FX has Maps or ML cached media. |
| `mastering_display_ids` | List of available Mastering Display Ids. |
| `mastering_display_info` | Dictionary containing Mastering Display information. Returned object is a copy. |
| `parent` | The parent object of this object. |
| `target_display_ids` | List of available Target Display Ids. |
| `target_display_info` | Dictionary containing Target Display information. Returned object is a copy. |
| `type` | Return the type of the Timeline FX. |


## Methods
### `analyze`
```python
analyze
```


analyze( (PyHDRTimelineFX)arg1 [, (str)analyze_mode='Current Shot']) -> None :

    Perform HDR analysis.

---

### `clear_maps_cache_media`
```python
clear_maps_cache_media
```


clear_maps_cache_media( (PyTimelineFX)arg1) -> bool :

    Clear the Timeline FX Maps and ML cached media.

---

### `export_DolbyVision_xml`
```python
export_DolbyVision_xml
```


export_DolbyVision_xml( (PyHDRTimelineFX)arg1, (str)file_name [, (bool)shot_only=False [, (str)comment='']]) -> None :

    Export the current HDR to a Dolby Vision XML file.

---

### `flush_maps_cache_media`
```python
flush_maps_cache_media
```


flush_maps_cache_media( (PyTimelineFX)arg1) -> bool :

    Clear the Timeline FX Maps and ML cached media.(Deprecated: Use clear_maps_cache_media instead.)

    

---

### `has_trim`
```python
has_trim
```


has_trim( (PyHDRTimelineFX)arg1, (int)target_display_id) -> bool :

    Returns True if the given Target Display ID has trims.

---

### `import_DolbyVision_xml`
```python
import_DolbyVision_xml
```


import_DolbyVision_xml( (PyHDRTimelineFX)arg1, (str)file_name [, (str)mode='Include Frame Based Transitions Trims' [, (int)shot_idx=0]]) -> None :

    Import the current HDR from a Dolby Vision XML file.

---

### `interpolate_trims`
```python
interpolate_trims
```


interpolate_trims( (PyHDRTimelineFX)arg1, (str)arg2) -> None :

    Interpolate the current HDR trims.

---

### `keep_analysis`
```python
keep_analysis
```


keep_analysis( (PyHDRTimelineFX)arg1) -> None :

    Remove the dirty flag from the HDR analysis.

---

### `l2_from_l8`
```python
l2_from_l8
```


l2_from_l8( (PyHDRTimelineFX)arg1) -> object :

    Dictionary containing the L2 values based on L8 values. Not valid in Dolby Vision 2.9.

---

### `load_setup`
```python
load_setup
```


load_setup( (PyTimelineFX)arg1, (str)file_name) -> bool :

    Load a Node setup. A path and a file name must be defined as arguments.

---

### `output_channel_as_metadata_key`
```python
output_channel_as_metadata_key
```


output_channel_as_metadata_key( (PyTimelineFX)arg1, (str)channel_name [, (bool)enable=True]) -> None :

    Enable/Disable the output as metadata of a channel.

    Keyword arguments:

    channel_name -- The name of the channel to output in the metadata; the Timeline FX name can be omitted.

    enable -- True to output metadata, False to stop outputting.

---

### `reset_analysis`
```python
reset_analysis
```


reset_analysis( (PyHDRTimelineFX)arg1) -> None :

    Reset the current HDR analysis.

---

### `reset_trims`
```python
reset_trims
```


reset_trims( (PyHDRTimelineFX)arg1) -> None :

    Reset the current HDR trims.

---

### `save_setup`
```python
save_setup
```


save_setup( (PyTimelineFX)arg1, (str)file_name) -> bool :

    Save a Node setup. A path and a file name must be defined as arguments.

---

### `slide_keyframes`
```python
slide_keyframes
```


slide_keyframes( (PyTimelineFX)arg1, (float)offset) -> None :

    Slide the keyframes the PySegment.

    Keywords argument:

    offset -- Relative offset to slide the keyframes.

    sync -- Enable to perform the same operation on the segments that belong to the same sync group as the current PySegment.

    

---

### `sync_connected_segments`
```python
sync_connected_segments
```


sync_connected_segments( (PyTimelineFX)arg1) -> None :

    Push the Timeline FX to connected segments.

---
