# Class: PyMediaHubFilesTab

**Module**: `flame`

**Inherits from**: [PyMediaHubTab](PyMediaHubTab.md), instance, object

## Description
This class represents the MediaHub Files tab.


## Properties
| Name | Description |
| --- | --- |
| `options` | None( (flame.PyMediaHubFilesTab)arg1) -> object |


## Methods
### `get_path`
```python
get_path
```


get_path( (PyMediaHubTab)arg1) -> str :

    Return the MediaHub tab current path.

---

### `set_path`
```python
set_path
```


set_path( (PyMediaHubTab)arg1, (str)arg2 [, (bool)allow_partial_success=False]) -> bool :

    Set the MediaHub tab current path. If allow_partial_success is True, the path will be set to the last valid folder in the path.

---
