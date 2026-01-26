
# Class: PyTypeNode

**Module**: `flame`

## Inheritance & Hierarchy
* **Base Class:** PyNode
* **Context:** Used for type/text effects in node-based compositing.

## Functional Role & Context
* **Functional Role:** Represents a Type node, providing access to text layers and type setup operations in node graphs.
* **Context:** Used for automating text effects, layer management, and type setup in node-based workflows.

## Description
The PyTypeNode class provides programmatic access to type nodes, supporting automation of text layer management and type setup in the Flame environment.

---

Object representing a Type node.

## Methods
### Properties
- `layers(...)` — None( (flame.PyTypeNode)arg1) -> list 
None( (flame.PyTypeNode)arg1) -> list


### Built-in methods
- `add_layer(...)` — add_layer( (PyTypeNode)arg1 [, (str)layer_type='Centre']) -> object : 
add_layer( (PyTypeNode)arg1 [, (str)layer_type='Centre']) -> object :
    Create a new layer.
    Keyword argument:
    layer_type -- Must be one of Left, Centre(default), Right, Roll, or Crawl.

- `append_type_setup(...)` — append_type_setup( (PyTypeNode)arg1, (str)file_name) -> bool : 
append_type_setup( (PyTypeNode)arg1, (str)file_name) -> bool :
    Append a setup to the current Type setup.

### Example
```python
# Example: Add a text layer to a Type node and set its text
# Assume 'type_node' is a PyTypeNode object
layer = type_node.add_layer('Centre')
layer.attributes.text = 'Client Title'
print('Layer text set to:', layer.attributes.text)
```


