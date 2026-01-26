
# Class: PyCoNode

**Module**: `flame`

## Inheritance & Hierarchy
* **Base class:** `PyNode` (inherits from `PyFlameObject`)
* **Functional Role:** Base class for Connectionist Nodes (e.g., Compass, Camera Analysis) in the schematic.

## Description
Represents a Connectionist Node, providing advanced node types for grouping, analysis, and connections in the schematic.

---


## Methods
### Properties
- `type(...)` — None( (flame.PyCoNode)arg1) -> str 
None( (flame.PyCoNode)arg1) -> str


### Built-in methods
- `assign_media(...)` — assign_media( (PyCoNode)arg1, (object)media_name) -> bool : 
assign_media( (PyCoNode)arg1, (object)media_name) -> bool :
    Assign a media layer to the node.
    Keyword argument
    media_name -- The index of the media layer from Actions' *media_layers*; or the name of the media layer.

- `cache_range(...)` — cache_range( (PyCoNode)arg1, (object)arg2, (object)start) -> bool : 
cache_range( (PyCoNode)arg1, (object)arg2, (object)start) -> bool :
    Cache the selected Map Analysis over the specified range.
    Keyword arguments
    start -- The first frame of the range. An integer.
    end -- The last frame of the range. An integer.

- `add_reference(...)` — add_reference( (PyCoNode)arg1, (object)frame) -> bool : 
add_reference( (PyCoNode)arg1, (object)frame) -> bool :
    Add a Motion Warp map's reference frame at specified index.
    Keyword argument
    frame -- The reference frame's index. An integer.

- `parents(...)` — parents( (PyCoNode)arg1 [, (str)link_type='Default']) -> list : 
parents( (PyCoNode)arg1 [, (str)link_type='Default']) -> list :
    Return a list of PyCoNode objects that are the parents of the action node.
    Keyword argument:
    link_type -- The type of link used to connect the nodes (default, look at, gmask, gmask exclusive, light, light exclusive, mimic)

- `children(...)` — children( (PyCoNode)arg1 [, (str)link_type='Default']) -> list : 
children( (PyCoNode)arg1 [, (str)link_type='Default']) -> list :
    Return a list of PyCoNode objects that are the children of the action node.
    Keyword argument:
    link_type -- The type of link used to connect the nodes (default, look at, gmask, gmask exclusive, light, light exclusive, mimic)

### Example
```python
# Example: Assign a media layer and cache an analysis range
# Assume 'co_node' is a PyCoNode object
co_node.assign_media('Diffuse')
co_node.cache_range(start=100, end=200)
print('Assigned media and cached analysis range')
```


