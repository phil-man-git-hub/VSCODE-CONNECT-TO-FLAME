
# Class: PyImageNode

**Module**: `flame`

## Inheritance & Hierarchy
* **Base class:** `PyActionFamilyNode` (inherits from `PyNode` → `PyFlameObject`)
* **Functional Role:** Represents an Image node in the schematic, used for image compositing and processing.

## Description
Represents an Image node, providing tools for image compositing and media management in the node graph.

---

### Example
```python
# Example: Add media to an Image node in Batch
# Assume 'image_node' is a PyImageNode and 'read_node' is a PyClipNode or Read File node
image_node.add_media(read_node)
print('Media layers on node:', [m.attributes.name for m in image_node.media_nodes])
```

## Methods
### Properties
- `media_nodes(...)` — None( (flame.PyImageNode)arg1) -> list 
None( (flame.PyImageNode)arg1) -> list


### Built-in methods
- `add_media(...)` — add_media( (PyActionFamilyNode)arg1) -> object : 
add_media( (PyActionFamilyNode)arg1) -> object :
    Add a Media layer to the Batch Image node.


