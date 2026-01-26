
# Class: PyCompassNode

**Module**: `flame`

## Inheritance & Hierarchy
* **Base class:** `PyCoNode` (inherits from `PyNode` → `PyFlameObject`)
* **Functional Role:** Schematic container/grouping node in the Batch environment.


## Description
Represents a Compass node, used for grouping and organizing nodes in the schematic.

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
### Properties
- `nodes(...)` — None( (flame.PyCompassNode)arg1) -> list 
None( (flame.PyCompassNode)arg1) -> list

## API Insight

- A Compass node groups nodes in the Batch schematic; properties like `name` and `collapsed` are commonly modified in automation.
- Use `nodes` to iterate children, and set `collapsed` to hide details in batch UIs.

**Example:**

```python
# Rename and collapse a compass node, then list its children
node.name = 'MyGroup'
node.collapsed = True
for c in node.nodes:
    print(c.name)
```

