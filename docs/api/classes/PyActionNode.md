# Class: PyActionNode

**Module**: `flame`

**Inherits from**: [PyActionFamilyNode](PyActionFamilyNode.md), [PyNode](PyNode.md), [PyFlameObject](PyFlameObject.md), instance, object

## Description
Class derived from PyActionFamilyNode. Represents an Action node object.


## Properties
| Name | Description |
| --- | --- |
| `all_tabs` | Return a list of the object tabs. |
| `attributes` | The attributes of a python object. |
| `cursor_position` | Return a tuple that provides the cursor position in the Action/Image/GMaskTracer schematic. |
| `input_sockets` | Return a list of the node input sockets names. |
| `left_tabs` | Return a list of the object left tabs. |
| `media_layers` | Return a list of the Media layers of the Action/Image/GMaskTracer node. |
| `media_nodes` | Return a list of the Media nodes attached to the Action node. |
| `node_types` | Return a list of the node types available in the Action/Image/GMaskTracer schematic. |
| `nodes` | Return a list of Action/Image/GMaskTracer nodes used in the the Action/Image/GMaskTracer schematic. |
| `output_sockets` | Return a list of the node output sockets names. |
| `output_types` | Return a list of the output types available to the Action node. |
| `parent` | The parent object of this object. |
| `right_tabs` | Return a list of the object right tabs. |
| `sockets` | Return a dictionary of the input/output sockets names and their connections. |


## Methods
### `add_media`
```python
add_media
```


add_media( (PyActionFamilyNode)arg1) -> object :

    Add a Media layer to the Batch Action node.

    Also instantiates a matching Surface node (and Axis) in the Action node schematic.

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

### `disable_output`
```python
disable_output
```


disable_output( (PyActionFamilyNode)arg1, (str)output_type) -> bool :

    Disable the render output_type for the Action node.

    Keyword argument:

    output_type -- The output to enable. (Comp, Matte, 3D Motion, Albedo, AO, Background, Emissive, GMask, Lens Flare, Motion Vectors, Normals, Object ID, Occluder, Position, Projectors Matte, Reflection, Roughness, Shadow, Specular, UV, Z-Depth HQ, Z-Depth)

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

### `enable_output`
```python
enable_output
```


enable_output( (PyActionFamilyNode)arg1, (str)output_type) -> bool :

    Enable the render output_type for the Action node.

    Keyword argument:

    output_type -- The output to enable. (Comp, Matte, 3D Motion, Albedo, AO, Background, Emissive, GMask, Lens Flare, Motion Vectors, Normals, Object ID, Occluder, Position, Projectoars Matte, Reflection, Roughness, Shadow, Specular, UV, Z-Depth HQ, Z-Depth)

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

### `export_fbx`
```python
export_fbx
```


export_fbx( (PyActionFamilyNode)arg1, (str)file_path [, (bool)only_selected_nodes=False [, (float)pixel_to_units=0.10000000149011612 [, (str)frame_rate='23.976 fps' [, (bool)bake_animation=False [, (bool)export_axes=True [, (bool)export_point_locators=False [, (bool)combine_material=True [, (bool)duplicate_material=False]]]]]]]]) -> bool :

    Export Action nodes to an FBX file.

    Keyword argument:

    file_path -- Path to the output FBX file. Mandatory.

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

### `import_abc`
```python
import_abc
```


import_abc( (PyActionFamilyNode)arg1, (str)file_path [, (bool)lights=True [, (bool)cameras=True [, (bool)models=True [, (bool)normals=True [, (bool)mesh_animations=True [, (str)frame_rate='23.976 fps' [, (bool)auto_fit=False [, (float)unit_to_pixels=10.0 [, (bool)consolidate_geometry=True [, (bool)create_object_group=False]]]]]]]]]]) -> list :

    Import an Alembic (ABC) file into the Action schematic using the Action Objects mode.

    Keyword argument:

    file_path -- Path to the ABC file. Mandatory.

---

### `import_fbx`
```python
import_fbx
```


import_fbx( (PyActionFamilyNode)arg1, (str)file_path [, (bool)lights=True [, (bool)cameras=True [, (bool)models=True [, (bool)normals=True [, (bool)mesh_animations=True [, (bool)keep_frame_rate=True [, (bool)bake_animation=False [, (bool)object_properties=True [, (bool)auto_fit=False [, (float)unit_to_pixels=10.0 [, (bool)create_media=True [, (bool)is_udim=False [, (bool)relink_material=True [, (str)input_colour_space='']]]]]]]]]]]]]]) -> list :

    Import an FBX file into the Action schematic using the Action Objects mode.

    Keyword argument:

    file_path -- Path to the FBX file. Mandatory.

    input_colour_space -- Colour space name used as input for textures. Optional.

---

### `import_psd`
```python
import_psd
```


import_psd( (PyActionFamilyNode)arg1, (str)file_path [, (str)input_colour_space='']) -> list :

    Import a PSD file into the Action schematic.

    Keyword arguments:

    file_path -- Path to the PSD file. Mandatory.

    input_colour_space -- The colour space used as input. Optional.

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

### `read_abc`
```python
read_abc
```


read_abc( (PyActionFamilyNode)arg1, (str)file_path [, (bool)lights=True [, (bool)cameras=True [, (bool)models=True [, (bool)normals=True [, (bool)mesh_animations=True [, (str)frame_rate='23.976 fps' [, (bool)auto_fit=False [, (float)unit_to_pixels=10.0 [, (bool)consolidate_geometry=True [, (bool)create_object_group=False]]]]]]]]]]) -> object :

    Import an Alembic (ABC) file into the Action schematic using the Read File mode.

    Keyword argument:

    file_path -- Path to the ABC file. Mandatory.

---

### `read_fbx`
```python
read_fbx
```


read_fbx( (PyActionFamilyNode)arg1, (str)file_path [, (bool)lights=True [, (bool)cameras=True [, (bool)models=True [, (bool)normals=True [, (bool)mesh_animations=True [, (bool)keep_frame_rate=True [, (bool)bake_animation=False [, (bool)object_properties=True [, (bool)auto_fit=False [, (float)unit_to_pixels=10.0 [, (bool)is_udim=False [, (bool)relink_material=True [, (str)input_colour_space='']]]]]]]]]]]]]) -> object :

    Import an FBX file into the Action schematic using the Read File mode.

    Keyword argument:

    file_path -- Path to the FBX file. Mandatory.

    input_colour_space -- Colour space name used as input for textures. Optional.

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
