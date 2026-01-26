# Class: PyCoNode

**Module**: `flame`

Class derived from PyFlameObject. This class represents an Action node in the Action schematic.

## Methods
### `assign_media(...)`

assign_media( (PyCoNode)arg1, (object)media_name) -> bool :
    Assign a media layer to the node.
    Keyword argument
    media_name -- The index of the media layer from Actions' *media_layers*; or the name of the media layer.

### `cache_range(...)`

cache_range( (PyCoNode)arg1, (object)arg2, (object)start) -> bool :
    Cache the selected Map Analysis over the specified range.
    Keyword arguments
    start -- The first frame of the range. An integer.
    end -- The last frame of the range. An integer.

### `add_reference(...)`

add_reference( (PyCoNode)arg1, (object)frame) -> bool :
    Add a Motion Warp map's reference frame at specified index.
    Keyword argument
    frame -- The reference frame's index. An integer.

### `parents(...)`

parents( (PyCoNode)arg1 [, (str)link_type='Default']) -> list :
    Return a list of PyCoNode objects that are the parents of the action node.
    Keyword argument:
    link_type -- The type of link used to connect the nodes (default, look at, gmask, gmask exclusive, light, light exclusive, mimic)

### `children(...)`

children( (PyCoNode)arg1 [, (str)link_type='Default']) -> list :
    Return a list of PyCoNode objects that are the children of the action node.
    Keyword argument:
    link_type -- The type of link used to connect the nodes (default, look at, gmask, gmask exclusive, light, light exclusive, mimic)

### `type(...)`

None( (flame.PyCoNode)arg1) -> str

