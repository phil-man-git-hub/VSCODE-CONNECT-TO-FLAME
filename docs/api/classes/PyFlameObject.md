
# Class: PyFlameObject

**Module**: `flame`

## Inheritance & Hierarchy
* **Root base class** for nearly all scriptable objects in the Flame Python API.
* **Functional Role:** Provides core methods and properties for all Flame objects, including attribute access and parent relationships.

## Description
Represents the root object for the Flame Python API, from which most other objects inherit.


## API Insight: Definition, Attributes, Methods, and Usage
The **PyFlameObject** is the root class for nearly all scriptable entities, providing fundamental properties and behaviors for all derived PyObjects.

### Inheritance and Core Role
| Property      | Value         | Description |
|-------------- |-------------- |-------------|
| Class Name    | PyFlameObject | Absolute base class for the API. |
| Primary Role  | API Root      | Framework for object identification, traversal, and attribute management. |
| Inheritance   | All other PyObjects | Most classes inherit from PyFlameObject. |

### Core Attributes
| Attribute         | Type           | Access     | Description |
|-------------------|---------------|------------|-------------|
| attributes        | PyAttribute    | Read-only  | Dictionary-like object for getting/setting properties. |
| parent            | PyFlameObject  | Read-only  | Immediate parent object in the hierarchy. |

### Universal Static Methods
| Method                | Type         | Description |
|-----------------------|-------------|-------------|
| __getattr__           | Static      | Access properties by name. |
| __setattr__           | Static      | Set properties by name. |
| __init__              | Static      | Instantiation via parent object's method. |

### Usage Context
PyFlameObject ensures consistency and recursive traversal across the API model, allowing robust scripting for project structure and metadata management.

**Example:**

```python
# Access attributes and walk up to the parent
print(my_clip.attributes.name)
parent = my_clip.parent
while parent is not None:
    print(f"Parent: {parent.__class__.__name__} - {getattr(parent, 'attributes', None)}")
    parent = parent.parent
```

## Methods
### Properties
- `attributes(...)` — None( (flame.PyFlameObject)arg1) -> list 
None( (flame.PyFlameObject)arg1) -> list

- `parent(...)` — None( (flame.PyFlameObject)arg1) -> object 
None( (flame.PyFlameObject)arg1) -> object


