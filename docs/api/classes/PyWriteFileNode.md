# Class: PyWriteFileNode

**Module**: `flame`

**Inherits from**: [PyRenderNode](PyRenderNode.md), [PyNode](PyNode.md), [PyFlameObject](PyFlameObject.md), instance, object

## Description
Class derived from PyRenderNode. This class represents a WriteFile node.


## Properties
| Name | Description |
| --- | --- |
| `attributes` | The attributes of a python object. |
| `channels` | The channels attribute is a list of tuples, where each tuple is made of a socket name and its channel name. |
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

### `get_resolved_media_path`
```python
get_resolved_media_path
```


get_resolved_media_path( (PyWriteFileNode)arg1 [, (bool)show_extension=True [, (bool)translate_path=True [, (object)frame=None]]]) -> object :

    Return the resolved media path.

    Keyword arguments:

    show_extension -- Set True to display the extension.

    translate_path -- Set True to apply the Media Location Path Translation.

    frame -- Pass a frame number, between range_start and range_end, to get the path for that frame.

    

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

### `save_node_setup`
```python
save_node_setup
```


save_node_setup( (PyNode)arg1, (str)file_name) -> bool :

    Save a Node setup. A path and a file name must be defined as arguments.

---

### `set_channel_name`
```python
set_channel_name
```


set_channel_name( (PyRenderNode)arg1, (object)channel, (object)name) -> None :

    Rename a channel, using its index or front channel name as the index key.

    Keyword arguments:

    channel -- The channel to rename. Can be the channel index or the current name of the channel's front socket.

    name -- The new name of the channel. The type is either a string or a tuple. A Write File node always takes a string. A Render node takes a string or a tuple.

    In a Render node, a string only sets the name of the channel's front socket; the function creates the name of the matte socket by appending '_alpha' to 'name'. In the UI, the channel is flagged 'Sync'. A Write File node has only one socket per channel, and requires only a string to set a socket name.

    In a Render node, a tuple sets the names of the front and matte sockets. In the UI, the channel is not flagged 'Sync'. A Write File node does not accept a tuple.

---

### `set_context`
```python
set_context
```


set_context( (PyNode)arg1, (int)index [, (str)socket_name='Default']) -> bool :

    Set a Context view on a Node socket. An index and a socket name must be defined as arguments.

---

### `set_metadata_discarded`
```python
set_metadata_discarded
```


set_metadata_discarded( (PyNode)arg1 [, (str)socket_name='Default' [, (str)key='' [, (bool)discarded=True]]]) -> None :

    Discard key from the Node's metadata output.

    Keyword arguments:

    socket_name -- The socket on which the discarded status of the metadata must be changed.

    key -- Metadata key to be discarded or restored.

    discarded -- True to discard the key from the node metadata output, False to restore the key.

    

---

### `set_metadata_key`
```python
set_metadata_key
```


set_metadata_key( (PyNode)arg1 [, (str)socket_name='Default' [, (str)key='' [, (object)name=None]]]) -> None :

    Rename a metadata key on the Node.

    Keyword arguments:

    socket_name -- The socket on which to rename the key. The default output is used when not specified.

    key -- The current metadata key name to be renamed.

    name -- The new metadata key name. If None, the current key name will revert to its original value.

    

---

### `set_metadata_value`
```python
set_metadata_value
```


set_metadata_value( (PyNode)arg1 [, (str)socket_name='Default' [, (str)key='' [, (object)value=None [, (bool)is_dynamic=False]]]]) -> None :

    Set the metadata on the Node.

    Keyword arguments:

    socket_name -- The socket on which to set the metadata. The default output is used when not specified.

    key -- Metadata key to be set or added.

    value -- Metadata value to be set or edited for the specified key. If None is specified, the current value will revert to the original value.

    is_dynamic -- Set the Metadata value to be resolved dynamically if it contains tokens.

    

---
