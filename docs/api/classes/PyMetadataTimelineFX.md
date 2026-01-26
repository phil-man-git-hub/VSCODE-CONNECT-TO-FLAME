
# Class: PyMetadataTimelineFX

**Module**: `flame`

## Inheritance & Hierarchy
* **Base Class:** PyTimelineFX
* **Context:** Used for timeline-based metadata effects and automation.

## Functional Role & Context
* **Functional Role:** Represents a Metadata Timeline FX, providing access to timeline-based metadata key/value management.
* **Context:** Used for automating metadata operations, including setting, discarding, and renaming metadata keys and values in timeline effects.

## Description
The PyMetadataTimelineFX class enables advanced metadata management for timeline effects, supporting automation of metadata editing, discarding, and renaming in the Flame timeline.

---

Object representing a Metadata Timeline FX.

## Methods
### Built-in methods
- `get_metadata(...)` — get_metadata( (PyMetadataTimelineFX)arg1 [, (str)key='' [, (int)frame=1]]) -> object : 
get_metadata( (PyMetadataTimelineFX)arg1 [, (str)key='' [, (int)frame=1]]) -> object :
    Return the metadata of a Metadata Timeline FX.
    Keywords argument:
    key -- Key of the requested metadata. All metadata is returned when not specified.
    frame -- Frame number. The first exposed frame being 1. If not specified, the current frame is used.

- `set_metadata_value(...)` — set_metadata_value( (PyMetadataTimelineFX)arg1, (str)key [, (object)value=None]) -> None : 
set_metadata_value( (PyMetadataTimelineFX)arg1, (str)key [, (object)value=None]) -> None :
    Set the metadata on a Metadata Timeline FX.
    Keywords argument:
    key -- Metadata key to be set or added.
    value -- Metadata value to be set or edited for the specified key. If None is specified, the current value will revert to the original value.

- `set_metadata_discarded(...)` — set_metadata_discarded( (PyMetadataTimelineFX)arg1 [, (str)key='' [, (bool)discarded=True]]) -> None : 
set_metadata_discarded( (PyMetadataTimelineFX)arg1 [, (str)key='' [, (bool)discarded=True]]) -> None :
    Discard key from the metadata output of a Metadata Timeline FX.
    Keywords argument:
    key -- Metadata key to be discarded or restored.
    discarded -- True to discard the key from the Metadata Timeline FX output, False to restore the key.

- `set_metadata_key(...)` — set_metadata_key( (PyMetadataTimelineFX)arg1 [, (str)key='' [, (object)name=None]]) -> None : 
set_metadata_key( (PyMetadataTimelineFX)arg1 [, (str)key='' [, (object)name=None]]) -> None :
    Rename a metadata key on a Metadata Timeline FX.
    Keyword arguments:
    key -- The current metadata key name to be renamed.
    name -- The new metadata key name. If None, the current key name will revert to its original value.

- `load_setup(...)` — load_setup( (PyMetadataTimelineFX)arg1, (str)file_name [, (bool)edited_keys=True [, (bool)discarded_keys=True [, (bool)added_keys=True [, (bool)update_tokens=True]]]]) -> bool : 
load_setup( (PyMetadataTimelineFX)arg1, (str)file_name [, (bool)edited_keys=True [, (bool)discarded_keys=True [, (bool)added_keys=True [, (bool)update_tokens=True]]]]) -> bool :
    Load a Metadata Timeline FX setup.
    Keywords argument:
    file_name -- the path and file name of the setup.
    edited_keys -- apply edited keys from the setup.
    discarded_keys -- apply discarded keys from the setup.
    added_keys -- apply added keys from the setup.

## API Insight

- Metadata Timeline FX mirrors the Metadata node API but operates on timeline frames; use `set_metadata_value` and `get_metadata` for frame-specific metadata.
- Passing `value=None` to `set_metadata_value` will revert the key to its original value.

**Example:**

```python
# Set a metadata value on frame 100 and read it back
fx.set_metadata_value('shot', 'A001')
print(fx.get_metadata('shot', frame=100))
```

