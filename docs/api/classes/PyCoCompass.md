
# Class: PyCoCompass

**Module**: `flame`

## Inheritance & Hierarchy
* **Base class:** `PyCoNode` (inherits from `PyNode` → `PyFlameObject`)
* **Functional Role:** A specific type of Compass node in the schematic, used for grouping and organizing nodes.


## Description
Represents a Compass node, providing a container for grouping nodes in the schematic.

---

## Attributes
| Attribute            | Type   | Description |
|----------------------|--------|-------------|
| name                 | str    | The name of the Action node in the Action schematic. |
| position             | tuple  | The XYZ position of the Action node in the Action 3D space. Range: (-3.4028234663852886e+38, -3.4028234663852886e+38, -3.4028234663852886e+38) to (3.4028234663852886e+38, 3.4028234663852886e+38, 3.4028234663852886e+38) |
| selected             | bool   | The Action node is selected. Values: True/False |
| collapsed_in_manager | bool   | The Action node is collapsed in the Action Manager. Values: True/False |
| colour               | tuple  | The colour of the Action node. |

---


## Methods
### Properties
- `nodes(...)` — None( (flame.PyCoCompass)arg1) -> list 
None( (flame.PyCoCompass)arg1) -> list
## API Insight

- Compass nodes are containers for organizing schematic nodes; use the `nodes` property to access contained nodes.
- Typical usage iterates over `compass.nodes` to inspect or modify child nodes.

**Example:**

```python
# Print names of nodes inside a Compass
for child in compass.nodes:
    print(child.name)
```
