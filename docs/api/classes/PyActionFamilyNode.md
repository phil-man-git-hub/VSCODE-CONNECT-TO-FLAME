# Class: PyActionFamilyNode

**Module**: `flame`

Class derived from PyNode. Represents an Action Family node object.

## Methods
### Properties
- `node_types(...)` — None( (flame.PyActionFamilyNode)arg1) -> list 
None( (flame.PyActionFamilyNode)arg1) -> list

- `nodes(...)` — None( (flame.PyActionFamilyNode)arg1) -> list 
None( (flame.PyActionFamilyNode)arg1) -> list

- `cursor_position(...)` — None( (flame.PyActionFamilyNode)arg1) -> tuple 
None( (flame.PyActionFamilyNode)arg1) -> tuple

- `all_tabs(...)` — None( (flame.PyActionFamilyNode)arg1) -> list 
None( (flame.PyActionFamilyNode)arg1) -> list

- `left_tabs(...)` — None( (flame.PyActionFamilyNode)arg1) -> list 
None( (flame.PyActionFamilyNode)arg1) -> list

- `right_tabs(...)` — None( (flame.PyActionFamilyNode)arg1) -> list 
None( (flame.PyActionFamilyNode)arg1) -> list

- `media_layers(...)` — None( (flame.PyActionFamilyNode)arg1) -> list 
None( (flame.PyActionFamilyNode)arg1) -> list


### Built-in methods
- `create_node(...)` — create_node( (PyActionFamilyNode)arg1, (str)node_type [, (str)file_path='' [, (bool)is_udim=False [, (int)tile_resolution=0 [, (str)input_colour_space='']]]]) -> object : 
create_node( (PyActionFamilyNode)arg1, (str)node_type [, (str)file_path='' [, (bool)is_udim=False [, (int)tile_resolution=0 [, (str)input_colour_space='']]]]) -> object :
    Add an Action/Image/GMaskTracer object node to the Action/Image/GMaskTracer schematic.
    Keyword argument:
    file_path -- Required by nodes that load an asset, such as Matchbox.
    input_colour_space -- Optional for nodes that load external media, such as IBL.

- `organize(...)` — organize( (PyActionFamilyNode)arg1) -> bool : 
organize( (PyActionFamilyNode)arg1) -> bool :
    Clean up the Action/Image/GMaskTracer schematic.

- `get_node(...)` — get_node( (PyActionFamilyNode)arg1, (str)node_name) -> object : 
get_node( (PyActionFamilyNode)arg1, (str)node_name) -> object :
    Get a node by node name. Doesn't select it in the UI.

- `connect_nodes(...)` — connect_nodes( (PyActionFamilyNode)arg1, (PyFlameObject)parent_node, (PyFlameObject)child_node [, (str)link_type='Default']) -> bool : 
connect_nodes( (PyActionFamilyNode)arg1, (PyFlameObject)parent_node, (PyFlameObject)child_node [, (str)link_type='Default']) -> bool :
    Connect two nodes in the Action/Image/GMaskTracer schematic.
    Keyword argument:
    type -- The type of link used to connect the nodes (default, look at, gmask, gmask exclusive, light, light exclusive, mimic)

- `disconnect_nodes(...)` — disconnect_nodes( (PyActionFamilyNode)arg1, (PyFlameObject)parent_node, (PyFlameObject)child_node [, (str)link_type='Default']) -> bool : 
disconnect_nodes( (PyActionFamilyNode)arg1, (PyFlameObject)parent_node, (PyFlameObject)child_node [, (str)link_type='Default']) -> bool :
    Disconnect two nodes in the Action/Image/GMaskTracer schematic.
    Keyword argument:
    type -- The type of link used to connect the nodes (default, look at, gmask, gmask exclusive, light, light exclusive, mimic)

- `clear_schematic(...)` — clear_schematic( (PyActionFamilyNode)arg1) -> bool : 
clear_schematic( (PyActionFamilyNode)arg1) -> bool :
    Clear the Action/Image/GMaskTracer schematic of all nodes.

- `encompass_nodes(...)` — encompass_nodes( (PyActionFamilyNode)arg1, (list)node_list) -> object : 
encompass_nodes( (PyActionFamilyNode)arg1, (list)node_list) -> object :
    Create a compass including the node list given as argument
    Keyword argument:
    node_list -- a list of nodes (either string or node objects)
    output_type -- the created compass node


