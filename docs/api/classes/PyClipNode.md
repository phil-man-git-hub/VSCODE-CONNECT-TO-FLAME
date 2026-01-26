
# Class: PyClipNode

**Module**: `flame`

## Inheritance & Hierarchy
* **Base class:** `PyNode` (inherits from `PyFlameObject`)
* **Functional Role:** Node representing a clip input in the Batch schematic.


## Description
Represents a Clip node, used to bring media into the Batch schematic for processing and compositing.

---

## Attributes
| Attribute           | Type | Description |
|---------------------|------|-------------|
| shot_name           | str  | The shot name of a node in the Batch schematic, resolving tokens if any are present. |
| tokenized_shot_name | str  | The shot name of a clip node, including unresolved tokens if present. |
| dynamic_shot_name   | str  | The Dynamic attribute of a clip node. Automatically disabled when shot_name is set. Values: True/False |

---


## Methods
### Properties
- `clip(...)` — None( (flame.PyClipNode)arg1) -> object 
None( (flame.PyClipNode)arg1) -> object

- `version_uids(...)` — None( (flame.PyClipNode)arg1) -> list 
None( (flame.PyClipNode)arg1) -> list

### Example
```python
# Example: Set the clip node to a specific version and add metadata
# Assume 'clip_node' is a PyClipNode object

# Set the current version UID (string retrieved from a PyReel or external source)
clip_node.set_version_uid('1234-5678-90ab')

# Add or update a metadata key on the default output socket
clip_node.set_metadata_value(socket_name='Default', key='SceneID', value='SCN010')
```

- `version_uid(...)` — None( (flame.PyClipNode)arg1) -> object 
None( (flame.PyClipNode)arg1) -> object


### Built-in methods
- `set_version_uid(...)` — set_version_uid( (PyClipNode)arg1, (str)version_uid) -> bool : 
set_version_uid( (PyClipNode)arg1, (str)version_uid) -> bool :
    Set the clip node's current version unique ID.
    Keywords argument:
    version_uid -- version unique ID.

- `set_metadata_value(...)` — set_metadata_value( (PyNode)arg1 [, (str)socket_name='Default' [, (str)key='' [, (object)value=None]]]) -> None : 
set_metadata_value( (PyNode)arg1 [, (str)socket_name='Default' [, (str)key='' [, (object)value=None]]]) -> None :
    Set the metadata on the Node.
    Keyword arguments:
    socket_name -- The socket on which to set the metadata. The default output is used when not specified.
    key -- Metadata key to be set or added.
    value -- Metadata value to be set or edited for the specified key. If None is specified, the current value will revert to the original value.

- `set_metadata_discarded(...)` — set_metadata_discarded( (PyNode)arg1 [, (str)socket_name='Default' [, (str)key='' [, (bool)discarded=True]]]) -> None : 
set_metadata_discarded( (PyNode)arg1 [, (str)socket_name='Default' [, (str)key='' [, (bool)discarded=True]]]) -> None :
    Discard key from the Node's metadata output.
    Keyword arguments:
    socket_name -- The socket on which the discarded status of the metadata must be changed.
    key -- Metadata key to be discarded or restored.
    discarded -- True to discard the key from the node metadata output, False to restore the key.

- `set_metadata_key(...)` — set_metadata_key( (PyNode)arg1 [, (str)socket_name='Default' [, (str)key='' [, (object)name=None]]]) -> None : 
set_metadata_key( (PyNode)arg1 [, (str)socket_name='Default' [, (str)key='' [, (object)name=None]]]) -> None :
    Rename a metadata key on the Node.
    Keyword arguments:
    socket_name -- The socket on which to rename the key. The default output is used when not specified.
    key -- The current metadata key name to be renamed.
    name -- The new metadata key name. If None, the current key name will revert to its original value.


