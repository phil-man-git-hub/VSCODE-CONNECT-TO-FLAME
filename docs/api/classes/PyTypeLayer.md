
# Class: PyTypeLayer

**Module**: `flame`

## Inheritance & Hierarchy
* **Base Class:** PyFlameObject
* **Contained By:** PyTypeFX, PyTypeNode

## Functional Role & Context
* **Functional Role:** Represents a type/text layer, providing access to text layer properties and management.
* **Context:** Used for automating text layer management and editing in type effects and nodes.

## Description
The PyTypeLayer class provides programmatic access to type/text layers, supporting automation of text layer management and editing in the Flame environment.

---

Object representing a Type Layer.

## Methods
### Properties
- `type(...)` — None( (flame.PyTypeLayer)arg1) -> object 
None( (flame.PyTypeLayer)arg1) -> object

## API Insight

- A Type Layer represents editable text content; inspect the `type` property for layer text and attributes.
- Modifying `type` properties allows programmatic editing of the text layer content and basic styling.

**Example:**

```python
# Inspect a type layer
print(layer.type)
```

