
# Class: PyClrMgmtNode

**Module**: `flame`

## Inheritance & Hierarchy
* **Base class:** `PyNode` (inherits from `PyFlameObject`)
* **Functional Role:** Color Management node in the Batch schematic, used for color space conversions and management.

## Description
Represents a Colour Management node, providing color space and transform operations in the node graph.

---

### Example
```python
# Example: Import a colour transform into a Colour Management node
# Assume 'clr_node' is a PyClrMgmtNode object
clr_node.import_transform('/mnt/ocio/transforms/rec709_to_acescg.cube')

# Use context variables to set runtime behaviour
clr_node.set_context_variable('use_gpu', 'True')
print(clr_node.get_context_variables())
```

## Methods
### Built-in methods
- `set_context_variable(...)` — set_context_variable( (PyClrMgmtNode)arg1, (str)name, (str)value) -> None : 
set_context_variable( (PyClrMgmtNode)arg1, (str)name, (str)value) -> None :
    Set the value for the specified context variable.

- `get_context_variables(...)` — get_context_variables( (PyClrMgmtNode)arg1) -> dict : 
get_context_variables( (PyClrMgmtNode)arg1) -> dict :
    Get the context variables in a dictionary.

- `reset_context_variables(...)` — reset_context_variables( (PyClrMgmtNode)arg1) -> None : 
reset_context_variables( (PyClrMgmtNode)arg1) -> None :
    Reset the context variables to their initial state from the ocio config.

- `import_transform(...)` — import_transform( (PyClrMgmtNode)arg1, (str)file_path) -> None : 
import_transform( (PyClrMgmtNode)arg1, (str)file_path) -> None :
    Import a transform from a file.


