
# Class: PyOFXNode

**Module**: `flame`

## Inheritance & Hierarchy
* **Base Class:** PyNode
* **Context:** Used for integrating OpenFX plugins in node-based compositing.

## Functional Role & Context
* **Functional Role:** Represents an OpenFX node, providing access to plugin management and integration.
* **Context:** Used for automating plugin changes and OpenFX node management in Flame.

## Description
The PyOFXNode class provides programmatic access to OpenFX nodes, supporting automation of plugin changes and integration in node-based workflows.

---


## Attributes
| Attribute   | Type | Description |
|-------------|------|-------------|
| pos_x       | int  | The x position of a node in the Batch schematic. Range: -2147483647 to 2147483647 |
| pos_y       | int  | The y position of a node in the Batch schematic. Range: -2147483647 to 2147483647 |
| name        | str  | The name of the node in the Batch schematic. |
| collapsed   | bool | The collapsed status of a node in the Batch schematic. Values: True/False |
| note        | str  | The Node's note. |

---

## Methods
### Built-in methods
- `change_plugin(...)` — change_plugin( (PyOFXNode)arg1, (str)plugin_name) -> bool : 
change_plugin( (PyOFXNode)arg1, (str)plugin_name) -> bool :
    Change the active plugin for the openFX node

### Example
```python
# Example: Change the plugin used by an OFX node
# Assume 'ofx_node' is a PyOFXNode object
if ofx_node.change_plugin('LensDistortion_v2'):
    print('Plugin updated to LensDistortion_v2')
else:
    print('Plugin change failed')
```


