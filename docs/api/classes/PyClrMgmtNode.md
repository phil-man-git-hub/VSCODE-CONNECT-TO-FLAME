# Class: PyClrMgmtNode

**Module**: `flame`

**Inherits from**: [PyNode](PyNode.md), [PyFlameObject](PyFlameObject.md), instance, object

## Description
Object representing a Colour Mgmt node.


## Properties
| Name | Description |
| --- | --- |
| `attributes` | The attributes of a python object. |
| `input_sockets` | Return a list of the node input sockets names. |
| `output_sockets` | Return a list of the node output sockets names. |
| `parent` | The parent object of this object. |
| `sockets` | Return a dictionary of the input/output sockets names and their connections. |


## Methods
### `cache_range`
```python
cache_range
```


cache_range( (PyNode)arg1 [, (object)start=None [, (object)end=None]]) -> int :

    Cache the Node result.

    Keyword arguments:

    start -- The first frame of the cache range. The current Batch start frame is used when not specified.

    end -- The last frame of the cache range. The current Batch end frame is used when not specified.

---

### `clear_schematic_colour`
```python
clear_schematic_colour
```


clear_schematic_colour( (PyNode)arg1) -> None :

    Clear the schematic colour of the Node.

---

### `delete`
```python
delete
```


delete( (PyFlameObject)arg1 [, (bool)confirm=True]) -> bool :

    Delete the node.

---

### `duplicate`
```python
duplicate
```


duplicate( (PyNode)arg1 [, (bool)keep_node_connections=False]) -> object :

    Duplicate the node.

---

### `get_context_variables`
```python
get_context_variables
```


get_context_variables( (PyClrMgmtNode)arg1) -> dict :

    Get the context variables in a dictionary.

---

### `get_metadata`
```python
get_metadata
```


get_metadata( (PyNode)arg1 [, (str)socket_name='Default' [, (str)key='' [, (object)frame=None]]]) -> object :

    Return the metadata of the Node.

    Keyword arguments:

    socket_name -- The socket from which to pull the metadata. The default output is used when not specified.

    key -- key of the requested metadata. All metadata is returned when not specified.

    frame -- frame of the requested metadata. The current frame is used when not specified.

---

### `import_transform`
```python
import_transform
```


import_transform( (PyClrMgmtNode)arg1, (str)file_path) -> None :

    Import a transform from a file.

---

### `load_node_setup`
```python
load_node_setup
```


load_node_setup( (PyNode)arg1, (str)file_name) -> bool :

    Load a Node setup. A path and a file name must be defined as arguments.

---

### `output_channel_as_metadata_key`
```python
output_channel_as_metadata_key
```


output_channel_as_metadata_key( (PyNode)arg1, (str)channel_name [, (bool)enable=True]) -> None :

    Enable/Disable the output as metadata of a channel.

    Keyword arguments:

    channel_name -- The name of the channel to output in the metadata; the Node name can be omitted.

    enable -- True to output metadata, False to stop outputting.

---

### `reset_context_variables`
```python
reset_context_variables
```


reset_context_variables( (PyClrMgmtNode)arg1) -> None :

    Reset the context variables to their initial state from the ocio config.

---

### `save_node_setup`
```python
save_node_setup
```


save_node_setup( (PyNode)arg1, (str)file_name) -> bool :

    Save a Node setup. A path and a file name must be defined as arguments.

---

### `set_context`
```python
set_context
```


set_context( (PyNode)arg1, (int)index [, (str)socket_name='Default']) -> bool :

    Set a Context view on a Node socket. An index and a socket name must be defined as arguments.

---

### `set_context_variable`
```python
set_context_variable
```


set_context_variable( (PyClrMgmtNode)arg1, (str)name, (str)value) -> None :

    Set the value for the specified context variable.

---
