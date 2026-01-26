
# Class: PyTimelineFX

**Module**: `flame`

## Inheritance & Hierarchy
* **Base Class:** PyFlameObject
* **Context:** Used in the timeline for effects processing.

## Functional Role & Context
* **Functional Role:** Represents a Timeline FX, providing access to effect setup, cache, and keyframe operations.
* **Context:** Used for automating and managing timeline effects in Flame.

## Description
The PyTimelineFX class provides access to timeline effects, enabling automation of effect setup, cache management, and keyframe operations in the timeline.

---

Object representing a Timeline FX.

## API Insight
### Autodesk Flame API Insight (2026)

`PyTimelineFX` is the base class for all timeline effects (Action, Keyer, Timewarp, etc.). It exposes effect identification (type), cache status (`has_maps_cache_media`), and universal methods for setup and keyframe handling.

**Common methods:** `load_setup(file_name)`, `save_setup(file_name)`, `clear_maps_cache_media()`, `slide_keyframes(offset, sync=False)`, `sync_connected_segments()`.

**Example:**

```python
# Iterate effects on a segment and clear maps cache if necessary
for fx in segment.effects:
    print('FX:', fx.type)
    if fx.has_maps_cache_media:
        fx.clear_maps_cache_media()
```


## Methods
### Properties
- `type(...)` — None( (flame.PyTimelineFX)arg1) -> object 
None( (flame.PyTimelineFX)arg1) -> object

- `has_maps_cache_media(...)` — None( (flame.PyTimelineFX)arg1) -> bool 
None( (flame.PyTimelineFX)arg1) -> bool


### Built-in methods
- `load_setup(...)` — load_setup( (PyTimelineFX)arg1, (str)file_name) -> bool : 
load_setup( (PyTimelineFX)arg1, (str)file_name) -> bool :
    Load a Node setup. A path and a file name must be defined as arguments.

- `save_setup(...)` — save_setup( (PyTimelineFX)arg1, (str)file_name) -> bool : 
save_setup( (PyTimelineFX)arg1, (str)file_name) -> bool :
    Save a Node setup. A path and a file name must be defined as arguments.

- `flush_maps_cache_media(...)` — flush_maps_cache_media( (PyTimelineFX)arg1) -> bool : 
flush_maps_cache_media( (PyTimelineFX)arg1) -> bool :
    Clear the Timeline FX Maps and ML cached media.(Deprecated: Use clear_maps_cache_media instead.)

- `clear_maps_cache_media(...)` — clear_maps_cache_media( (PyTimelineFX)arg1) -> bool : 
clear_maps_cache_media( (PyTimelineFX)arg1) -> bool :
    Clear the Timeline FX Maps and ML cached media.

- `sync_connected_segments(...)` — sync_connected_segments( (PyTimelineFX)arg1) -> None : 
sync_connected_segments( (PyTimelineFX)arg1) -> None :
    Push the Timeline FX to connected segments.

- `slide_keyframes(...)` — slide_keyframes( (PyTimelineFX)arg1, (float)offset) -> None : 
slide_keyframes( (PyTimelineFX)arg1, (float)offset) -> None :
    Slide the keyframes the PySegment.
    Keywords argument:
    offset -- Relative offset to slide the keyframes.
    sync -- Enable to perform the same operation on the segments that belong to the same sync group as the current PySegment.

- `output_channel_as_metadata_key(...)` — output_channel_as_metadata_key( (PyTimelineFX)arg1, (str)channel_name [, (bool)enable=True]) -> None : 
output_channel_as_metadata_key( (PyTimelineFX)arg1, (str)channel_name [, (bool)enable=True]) -> None :
    Enable/Disable the output as metadata of a channel.
    Keyword arguments:
    channel_name -- The name of the channel to output in the metadata; the Timeline FX name can be omitted.
    enable -- True to output metadata, False to stop outputting.


