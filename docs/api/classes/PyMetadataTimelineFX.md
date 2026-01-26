# Class: PyMetadataTimelineFX

**Module**: `flame`

**Inherits from**: [PyTimelineFX](PyTimelineFX.md), [PyFlameObject](PyFlameObject.md), instance, object

## Description
Object representing a Metadata Timeline FX.


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

### `get_metadata`
```python
get_metadata
```


get_metadata( (PyMetadataTimelineFX)arg1 [, (str)key='' [, (int)frame=1]]) -> object :

    Return the metadata of a Metadata Timeline FX.

    Keywords argument:

    key -- Key of the requested metadata. All metadata is returned when not specified.

    frame -- Frame number. The first exposed frame being 1. If not specified, the current frame is used.

---

### `load_setup`
```python
load_setup
```


load_setup( (PyMetadataTimelineFX)arg1, (str)file_name [, (bool)edited_keys=True [, (bool)discarded_keys=True [, (bool)added_keys=True [, (bool)update_tokens=True]]]]) -> bool :

    Load a Metadata Timeline FX setup.

    Keywords argument:

    file_name -- the path and file name of the setup.

    edited_keys -- apply edited keys from the setup.

    discarded_keys -- apply discarded keys from the setup.

    added_keys -- apply added keys from the setup.

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

### `set_metadata_discarded`
```python
set_metadata_discarded
```


set_metadata_discarded( (PyMetadataTimelineFX)arg1 [, (str)key='' [, (bool)discarded=True]]) -> None :

    Discard key from the metadata output of a Metadata Timeline FX.

    Keywords argument:

    key -- Metadata key to be discarded or restored.

    discarded -- True to discard the key from the Metadata Timeline FX output, False to restore the key.

    

---

### `set_metadata_key`
```python
set_metadata_key
```


set_metadata_key( (PyMetadataTimelineFX)arg1 [, (str)key='' [, (object)name=None]]) -> None :

    Rename a metadata key on a Metadata Timeline FX.

    Keyword arguments:

    key -- The current metadata key name to be renamed.

    name -- The new metadata key name. If None, the current key name will revert to its original value.

    

---

### `set_metadata_value`
```python
set_metadata_value
```


set_metadata_value( (PyMetadataTimelineFX)arg1, (str)key [, (object)value=None]) -> None :

    Set the metadata on a Metadata Timeline FX.

    Keywords argument:

    key -- Metadata key to be set or added.

    value -- Metadata value to be set or edited for the specified key. If None is specified, the current value will revert to the original value.

    

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
