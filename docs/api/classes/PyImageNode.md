# Class: PyImageNode

**Module**: `flame`

**Inherits from**: [PyActionFamilyNode](PyActionFamilyNode.md), [PyNode](PyNode.md), [PyFlameObject](PyFlameObject.md), instance, object

## Description
Class derived from PyActionFamilyNode. Represents an Image node object.


## Properties
| Name | Description |
| --- | --- |
| `all_tabs` | Return a list of the object tabs. |
| `attributes` | The attributes of a python object. |
| `cursor_position` | Return a tuple that provides the cursor position in the Action/Image/GMaskTracer schematic. |
| `input_sockets` | Return a list of the node input sockets names. |
| `left_tabs` | Return a list of the object left tabs. |
| `media_layers` | Return a list of the Media layers of the Action/Image/GMaskTracer node. |
| `media_nodes` | Return a list of the Media nodes attached to the Image node. |
| `node_types` | Return a list of the node types available in the Action/Image/GMaskTracer schematic. |
| `nodes` | Return a list of Action/Image/GMaskTracer nodes used in the the Action/Image/GMaskTracer schematic. |
| `output_sockets` | Return a list of the node output sockets names. |
| `parent` | The parent object of this object. |
| `right_tabs` | Return a list of the object right tabs. |
| `sockets` | Return a dictionary of the input/output sockets names and their connections. |


## Methods
### `add_media`
```python
add_media
```


add_media( (PyActionFamilyNode)arg1) -> object :

    Add a Media layer to the Batch Image node.

---

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

### `clear_schematic`
```python
clear_schematic
```


clear_schematic( (PyActionFamilyNode)arg1) -> bool :

    Clear the Action/Image/GMaskTracer schematic of all nodes.

---

### `clear_schematic_colour`
```python
clear_schematic_colour
```


clear_schematic_colour( (PyNode)arg1) -> None :

    Clear the schematic colour of the Node.

---

### `connect_nodes`
```python
connect_nodes
```


connect_nodes( (PyActionFamilyNode)arg1, (PyFlameObject)parent_node, (PyFlameObject)child_node [, (str)link_type='Default']) -> bool :

    Connect two nodes in the Action/Image/GMaskTracer schematic.

    Keyword argument:

    type -- The type of link used to connect the nodes (default, look at, gmask, gmask exclusive, light, light exclusive, mimic)

---

### `create_node`
```python
create_node
```


create_node( (PyActionFamilyNode)arg1, (str)node_type [, (str)file_path='' [, (bool)is_udim=False [, (int)tile_resolution=0 [, (str)input_colour_space='']]]]) -> object :

    Add an Action/Image/GMaskTracer object node to the Action/Image/GMaskTracer schematic.

    Keyword argument:

    file_path -- Required by nodes that load an asset, such as Matchbox.

    input_colour_space -- Optional for nodes that load external media, such as IBL.

---

### `delete`
```python
delete
```


delete( (PyFlameObject)arg1 [, (bool)confirm=True]) -> bool :

    Delete the node.

---

### `disconnect_nodes`
```python
disconnect_nodes
```


disconnect_nodes( (PyActionFamilyNode)arg1, (PyFlameObject)parent_node, (PyFlameObject)child_node [, (str)link_type='Default']) -> bool :

    Disconnect two nodes in the Action/Image/GMaskTracer schematic.

    Keyword argument:

    type -- The type of link used to connect the nodes (default, look at, gmask, gmask exclusive, light, light exclusive, mimic)

---

### `duplicate`
```python
duplicate
```


duplicate( (PyNode)arg1 [, (bool)keep_node_connections=False]) -> object :

    Duplicate the node.

---

### `encompass_nodes`
```python
encompass_nodes
```


encompass_nodes( (PyActionFamilyNode)arg1, (list)node_list) -> object :

    Create a compass including the node list given as argument

    Keyword argument:

    node_list -- a list of nodes (either string or node objects)

    output_type -- the created compass node

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

### `get_node`
```python
get_node
```


get_node( (PyActionFamilyNode)arg1, (str)node_name) -> object :

    Get a node by node name. Doesn't select it in the UI.

---

### `load_node_setup`
```python
load_node_setup
```


load_node_setup( (PyNode)arg1, (str)file_name) -> bool :

    Load a Node setup. A path and a file name must be defined as arguments.

---

### `organize`
```python
organize
```


organize( (PyActionFamilyNode)arg1) -> bool :

    Clean up the Action/Image/GMaskTracer schematic.

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

### `set_context`
```python
set_context
```


set_context( (PyNode)arg1, (int)index [, (str)socket_name='Default']) -> bool :

    Set a Context view on a Node socket. An index and a socket name must be defined as arguments.

---
