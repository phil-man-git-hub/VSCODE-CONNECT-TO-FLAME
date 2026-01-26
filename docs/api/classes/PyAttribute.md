
# Class: PyAttribute

**Module**: `flame`

## Inheritance & Hierarchy
* **Standalone class** (not derived from PyFlameObject)
* **Functional Role:** Wrapper for accessing and modifying an object's properties (attributes) in the Flame API.

## Description
Represents a property or attribute of a Flame object. Used to get/set values and enumerate possible values for attributes.


## API Insight: Definition, Methods, and Usage
The **PyAttribute** class is a specialized utility for accessing and manipulating dynamic parameters of core Flame objects (Nodes, Segments, Timeline FX).

### Definition and Hierarchy
| Property      | Value         | Description |
|-------------- |-------------- |-------------|
| Class Name    | PyAttribute   | Utility class for accessing and controlling an object's parameters. |
| Parent Class  | None          | Standalone class. |
| Access Point  | .attributes   | Accessed via the `.attributes` property of PyFlameObject-derived objects. |

### Core Methods
| Method              | Arguments                        | Returns   | Description |
|---------------------|----------------------------------|-----------|-------------|
| value()             | attribute_name, [new_value]      | object    | Get/set the value of an attribute. |
| keyframe_count()    | attribute_name                   | int       | Number of keyframes on the attribute. |
| is_keyframed()      | attribute_name                   | bool      | Whether the attribute is animated. |
| get_keyframe()      | attribute_name, frame            | object    | Get keyframe value at a frame. |
| set_keyframe()      | attribute_name, frame, value     | None      | Set a keyframe at a frame. |
| delete_keyframe()   | attribute_name, frame            | None      | Delete a keyframe at a frame. |
| type()              | attribute_name                   | str       | Data type of the attribute. |
| is_visible()        | attribute_name                   | bool      | Whether the attribute is visible in UI. |
| attribute_names()   | None                             | list      | List all available attribute names. |

### Usage Context
PyAttribute is essential for automation and rigging, as most interactive controls in Flame are represented as attributes. It is used for changing effect looks, animation, and querying available parameters.

**Example Scenario (Setting a value and checking animation):**

```python
# Assuming 'my_blur' is an instance of PyNode
blur_attributes = my_blur.attributes

# Set the blur radius
blur_attributes.value('Blur_Radius', 50.0)

# Check if the radius is animated
is_animated = blur_attributes.is_keyframed('Blur_Radius')

# Print the result
print(f"Blur_Radius is animated: {is_animated}")
```


## Special Methods & Properties
| Method/Property      | Description |
|----------------------|-------------|
| `get_value()`        | Get the value of an attribute. |
| `set_value(value)`   | Set the value of an attribute. |
| `values`             | List the possible values or the range of possible values for an attribute. |
| `__add__`, `__sub__`, `__mul__`, `__truediv__`, `__floordiv__`, `__eq__`, `__ne__`, `__lt__`, `__le__`, `__gt__`, `__ge__`, `__str__`, etc. | Supports rich comparison and arithmetic operations with numbers and strings. |

---


## Methods
### Properties
- `values(...)` — None( (flame.PyAttribute)arg1) -> object 
None( (flame.PyAttribute)arg1) -> object


### Built-in methods
- `set_value(...)` — set_value( (PyAttribute)arg1, (object)arg2) -> bool : 
set_value( (PyAttribute)arg1, (object)arg2) -> bool :
    Set the value of an attribute.

- `get_value(...)` — get_value( (PyAttribute)arg1) -> object : 
get_value( (PyAttribute)arg1) -> object :
    Get the value of an attribute.


