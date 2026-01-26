
# Class: PyPaintNode

**Module**: `flame`

## Inheritance & Hierarchy
* **Base Class:** PyNode
* **Context:** Used in Batch and TimelineFX for paint operations.

## Functional Role & Context
* **Functional Role:** Represents a Paint node, allowing programmatic creation and manipulation of paint layers and sources.
* **Context:** Used for automating paint effects, adding sources, and managing paint operations in node-based compositing.

## Description
The PyPaintNode class provides access to the Paint node in Flame, enabling the addition of source layers and automation of paint-related tasks within a node graph.


Object representing a Paint node.

## Attributes
| Attribute   | Type | Description |
|-------------|------|-------------|
| pos_x       | int  | The x position of a node in the Batch schematic. Range: -2147483647 to 2147483647 |
| pos_y       | int  | The y position of a node in the Batch schematic. Range: -2147483647 to 2147483647 |
| name        | str  | The name of the node in the Batch schematic. |
| collapsed   | bool | The collapsed status of a node in the Batch schematic. True or False |
| note        | str  | The Node's note. |

## Methods
### Built-in methods
- `add_source(...)` — add_source( (PyPaintNode)arg1) -> object : 
add_source( (PyPaintNode)arg1) -> object :
    Add a Source layer to a Paint node.

### Example
```python
# Add a new source to a Paint node
# Assume 'paint_node' is a PyPaintNode object
new_source = paint_node.add_source()
print('Added paint source:', new_source.attributes.name)
```


