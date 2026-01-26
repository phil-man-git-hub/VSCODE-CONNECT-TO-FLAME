# Class: PyColourMgtTimelineFX

**Module**: `flame`

**Inherits from**: [PyTimelineFX](PyTimelineFX.md), [PyFlameObject](PyFlameObject.md), instance, object

## Description
Object representing a Colour Mgmt Timeline FX.


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

### `get_context_variables`
```python
get_context_variables
```


get_context_variables( (PyColourMgtTimelineFX)arg1) -> dict :

    Get the context variables in a dictionary.

---

### `import_transform`
```python
import_transform
```


import_transform( (PyColourMgtTimelineFX)arg1, (str)file_path) -> None :

    Import a transform from a file.

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

### `reset_context_variables`
```python
reset_context_variables
```


reset_context_variables( (PyColourMgtTimelineFX)arg1) -> None :

    Reset the context variables to their initial state from the ocio config.

---

### `save_setup`
```python
save_setup
```


save_setup( (PyTimelineFX)arg1, (str)file_name) -> bool :

    Save a Node setup. A path and a file name must be defined as arguments.

---

### `set_context_variable`
```python
set_context_variable
```


set_context_variable( (PyColourMgtTimelineFX)arg1, (str)name, (str)value) -> None :

    Set the value for the specified context variable.

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
