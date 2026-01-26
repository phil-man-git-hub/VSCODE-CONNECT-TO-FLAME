
# Class: PyMetadataValue

**Module**: `flame`

## Inheritance & Hierarchy
* **Base Class:** PyFlameObject
* **Context:** Used for representing and manipulating metadata values of various types.

## Functional Role & Context
* **Functional Role:** Represents a metadata value, providing access to its type and value operations.
* **Context:** Used for programmatic access to metadata values, supporting get/set operations for automation and scripting.

## Description
The PyMetadataValue class encapsulates a metadata value, supporting type inspection and value manipulation for advanced metadata workflows in Flame.

---

This class holds the metadata of a specific data type.

### Example
```python
# Example: Read and update a metadata value
# Assume 'md_value' is a PyMetadataValue object
current = md_value.get_value()
print('Current metadata value:', current)

# Update the metadata value
md_value.set_value('COMPOSITE')
```

## Methods
### Properties
- `type(...)` — None( (flame.PyMetadataValue)arg1) -> str 
None( (flame.PyMetadataValue)arg1) -> str


### Built-in methods
- `get_value(...)` — get_value( (PyMetadataValue)arg1) -> object : 
get_value( (PyMetadataValue)arg1) -> object :
    Get the metadata value.

- `set_value(...)` — set_value( (PyMetadataValue)arg1, (object)value) -> None : 
set_value( (PyMetadataValue)arg1, (object)value) -> None :
    Set the metadata value.


