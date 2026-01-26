
# Class: PyWriteFileNode

**Module**: `flame`

## Inheritance & Hierarchy
* **Base Class:** PyRenderNode
* **Context:** Used for writing rendered outputs to files in node-based compositing.

## Functional Role & Context
* **Functional Role:** Represents a WriteFile node, providing access to file output and resolved media path operations.
* **Context:** Used for automating file output, path resolution, and media management in Batch and TimelineFX.

## Description
The PyWriteFileNode class provides programmatic access to write file nodes, supporting automation of file output and media path resolution in node-based workflows.

---

Class derived from PyRenderNode. This class represents a WriteFile node.

## Methods
### Built-in methods
- `get_resolved_media_path(...)` — get_resolved_media_path( (PyWriteFileNode)arg1 [, (bool)show_extension=True [, (bool)translate_path=True [, (object)frame=None]]]) -> object : 
get_resolved_media_path( (PyWriteFileNode)arg1 [, (bool)show_extension=True [, (bool)translate_path=True [, (object)frame=None]]]) -> object :
    Return the resolved media path.
    Keyword arguments:
    show_extension -- Set True to display the extension.
    translate_path -- Set True to apply the Media Location Path Translation.
    frame -- Pass a frame number, between range_start and range_end, to get the path for that frame.


### Example
```python
# Get the resolved output path from a WriteFile node
# Assume 'write_node' is a PyWriteFileNode object
path = write_node.get_resolved_media_path(show_extension=True, translate_path=True)
print('Resolved output path:', path)
```
