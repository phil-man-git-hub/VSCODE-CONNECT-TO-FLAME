# Class: PySearch

**Module**: `flame`

**Inherits from**: instance, object

## Description
This class represents the search.


## Properties
| Name | Description |
| --- | --- |
| `use_weight` | Return true if the search sorting is done using weight. |


## Methods
### `activate_search_result`
```python
activate_search_result
```


activate_search_result( (PySearch)arg1, (str)name, (str)type [, (str)tab='Tools']) -> None :

    Activate a search result.

---

### `search_results`
```python
search_results
```


search_results( (PySearch)arg1 [, (str)search_str='*' [, (str)tab='Tools']]) -> list :

    Search results that match a string.

---

### `set_tool_favorite`
```python
set_tool_favorite
```


set_tool_favorite( (PySearch)arg1, (str)arg2, (str)name, (bool)type) -> None :

    Return the favorite status of a tool.

---

### `set_tool_hidden`
```python
set_tool_hidden
```


set_tool_hidden( (PySearch)arg1, (str)arg2, (str)name, (bool)type) -> None :

    Return the hidden status of a tool.

---

### `set_tool_weight`
```python
set_tool_weight
```


set_tool_weight( (PySearch)arg1, (str)arg2, (str)name, (int)type) -> None :

    Return the tool weight.

---
