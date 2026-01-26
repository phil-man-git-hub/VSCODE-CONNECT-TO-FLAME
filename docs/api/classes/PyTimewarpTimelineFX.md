# Class: PyTimewarpTimelineFX

**Module**: `flame`

**Inherits from**: [PyTimelineFX](PyTimelineFX.md), [PyFlameObject](PyFlameObject.md), instance, object

## Description
Object representing a Timewarp node.


## Properties
| Name | Description |
| --- | --- |
| `attributes` | The attributes of a python object. |
| `has_maps_cache_media` | Return whether the Timeline FX has Maps or ML cached media. |
| `parent` | The parent object of this object. |
| `type` | Return the type of the Timeline FX. |


## Methods
### `clear_maps_cache_media`
```python
clear_maps_cache_media
```


clear_maps_cache_media( (PyTimelineFX)arg1) -> bool :

    Clear the Timeline FX Maps and ML cached media.

---

### `flush_maps_cache_media`
```python
flush_maps_cache_media
```


flush_maps_cache_media( (PyTimelineFX)arg1) -> bool :

    Clear the Timeline FX Maps and ML cached media.(Deprecated: Use clear_maps_cache_media instead.)

    

---

### `get_duration_timing`
```python
get_duration_timing
```


get_duration_timing( (PyTimewarpTimelineFX)arg1, (float)frame) -> float :

    Return the timing value for the current frame while in the duration mode.

---

### `get_speed`
```python
get_speed
```


get_speed( (PyTimewarpTimelineFX)arg1, (float)frame) -> float :

    Return the speed attribute at the requested frame.

---

### `get_speed_timing`
```python
get_speed_timing
```


get_speed_timing( (PyTimewarpTimelineFX)arg1, (float)frame) -> float :

    The timing value for the current frame while in the speed mode.

---

### `get_timing`
```python
get_timing
```


get_timing( (PyTimewarpTimelineFX)arg1, (float)frame) -> float :

    Return the timing value at the requested frame.

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

### `save_setup`
```python
save_setup
```


save_setup( (PyTimelineFX)arg1, (str)file_name) -> bool :

    Save a Node setup. A path and a file name must be defined as arguments.

---

### `set_speed`
```python
set_speed
```


set_speed( (PyTimewarpTimelineFX)arg1, (float)frame, (float)new_speed) -> None :

    Set the speed at the requested frame.

---

### `set_timing`
```python
set_timing
```


set_timing( (PyTimewarpTimelineFX)arg1, (float)frame, (float)new_timing) -> None :

    Set the timing at the requested frame.

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
