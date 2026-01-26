
# Class: PyNode

**Module**: `flame`

## Inheritance & Hierarchy
* **Base Class:** PyFlameObject
* **Derived Classes:** Many node types in Batch, TimelineFX, and Schematic inherit from PyNode.

## Functional Role & Context
* **Functional Role:** Represents a generic node in the Flame compositing, schematic, or effects graph. Nodes are the building blocks for effects, processing, and data flow in Batch and TimelineFX.
* **Context:** Used for manipulating, connecting, and querying nodes in the schematic. Provides access to sockets, metadata, and node setup operations.

## Description
The PyNode class is the core abstraction for all node-based operations in Flame. It provides methods for managing node connections, loading/saving setups, duplicating, deleting, and accessing node-specific metadata. Most effect, processing, and utility nodes in Flame derive from PyNode.

---


## Attributes
| Attribute   | Type | Description |
|-------------|------|-------------|
| pos_x       | int  | The x position of a node in the Batch schematic. Range: -2147483647 to 2147483647 |
| pos_y       | int  | The y position of a node in the Batch schematic. Range: -2147483647 to 2147483647 |
| name        | str  | The name of the node in the Batch schematic. |
| shot_name   | str  | The shot name of the node in the Batch schematic, resolving tokens if any are present. |
| collapsed   | bool | The collapsed status of a node in the Batch schematic. Values: True/False |

---
Object representing a Node.

### Example
```python
# Example: Duplicate a node and save its node setup
# Assume 'node' is a PyNode object
copy = node.duplicate(keep_node_connections=False)
node.save_node_setup('/tmp/node_setup.xml')
print('Duplicated node:', copy.attributes.name)
```

## Methods
### Properties
- `sockets(...)` — None( (flame.PyNode)arg1) -> dict 
None( (flame.PyNode)arg1) -> dict

- `input_sockets(...)` — None( (flame.PyNode)arg1) -> list 
None( (flame.PyNode)arg1) -> list

- `output_sockets(...)` — None( (flame.PyNode)arg1) -> list 
None( (flame.PyNode)arg1) -> list


### Built-in methods
- `load_node_setup(...)` — load_node_setup( (PyNode)arg1, (str)file_name) -> bool : 
load_node_setup( (PyNode)arg1, (str)file_name) -> bool :
    Load a Node setup. A path and a file name must be defined as arguments.

- `save_node_setup(...)` — save_node_setup( (PyNode)arg1, (str)file_name) -> bool : 
save_node_setup( (PyNode)arg1, (str)file_name) -> bool :
    Save a Node setup. A path and a file name must be defined as arguments.

- `delete(...)` — delete( (PyFlameObject)arg1 [, (bool)confirm=True]) -> bool : 
delete( (PyFlameObject)arg1 [, (bool)confirm=True]) -> bool :
    Delete the node.

- `duplicate(...)` — duplicate( (PyNode)arg1 [, (bool)keep_node_connections=False]) -> object : 
duplicate( (PyNode)arg1 [, (bool)keep_node_connections=False]) -> object :
    Duplicate the node.

- `set_context(...)` — set_context( (PyNode)arg1, (int)index [, (str)socket_name='Default']) -> bool : 
set_context( (PyNode)arg1, (int)index [, (str)socket_name='Default']) -> bool :
    Set a Context view on a Node socket. An index and a socket name must be defined as arguments.

- `clear_schematic_colour(...)` — clear_schematic_colour( (PyNode)arg1) -> None : 
clear_schematic_colour( (PyNode)arg1) -> None :
    Clear the schematic colour of the Node.

- `get_metadata(...)` — get_metadata( (PyNode)arg1 [, (str)socket_name='Default' [, (str)key='' [, (object)frame=None]]]) -> object : 
get_metadata( (PyNode)arg1 [, (str)socket_name='Default' [, (str)key='' [, (object)frame=None]]]) -> object :
    Return the metadata of the Node.
    Keyword arguments:
    socket_name -- The socket from which to pull the metadata. The default output is used when not specified.
    key -- key of the requested metadata. All metadata is returned when not specified.
    frame -- frame of the requested metadata. The current frame is used when not specified.

- `cache_range(...)` — cache_range( (PyNode)arg1 [, (object)start=None [, (object)end=None]]) -> int : 
cache_range( (PyNode)arg1 [, (object)start=None [, (object)end=None]]) -> int :
    Cache the Node result.
    Keyword arguments:
    start -- The first frame of the cache range. The current Batch start frame is used when not specified.
    end -- The last frame of the cache range. The current Batch end frame is used when not specified.

- `output_channel_as_metadata_key(...)` — output_channel_as_metadata_key( (PyNode)arg1, (str)channel_name [, (bool)enable=True]) -> None : 
output_channel_as_metadata_key( (PyNode)arg1, (str)channel_name [, (bool)enable=True]) -> None :
    Enable/Disable the output as metadata of a channel.
    Keyword arguments:
    channel_name -- The name of the channel to output in the metadata; the Node name can be omitted.
    enable -- True to output metadata, False to stop outputting.


