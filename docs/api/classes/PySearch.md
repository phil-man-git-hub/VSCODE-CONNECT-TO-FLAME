
# Class: PySearch

**Module**: `flame`

## Inheritance & Hierarchy
* **Base Class:** PyFlameObject
* **Context:** Used for searching and managing tool visibility and favorites in Flame.

## Functional Role & Context
* **Functional Role:** Represents the search system, providing access to tool search, favorites, and visibility management.
* **Context:** Used for automating search, tool management, and UI customization in Flame.

## Description
The PySearch class provides programmatic access to the search system, supporting automation of tool search, favorites, and visibility management in the Flame environment.

---

This class represents the search.

## Methods
### Properties
- `use_weight(...)` — None( (flame.PySearch)arg1) -> bool 
None( (flame.PySearch)arg1) -> bool


### Built-in methods
- `set_tool_favorite(...)` — set_tool_favorite( (PySearch)arg1, (str)arg2, (str)name, (bool)type) -> None : 
set_tool_favorite( (PySearch)arg1, (str)arg2, (str)name, (bool)type) -> None :
    Return the favorite status of a tool.

- `set_tool_hidden(...)` — set_tool_hidden( (PySearch)arg1, (str)arg2, (str)name, (bool)type) -> None : 
set_tool_hidden( (PySearch)arg1, (str)arg2, (str)name, (bool)type) -> None :
    Return the hidden status of a tool.

- `set_tool_weight(...)` — set_tool_weight( (PySearch)arg1, (str)arg2, (str)name, (int)type) -> None : 
set_tool_weight( (PySearch)arg1, (str)arg2, (str)name, (int)type) -> None :
    Return the tool weight.

- `search_results(...)` — search_results( (PySearch)arg1 [, (str)search_str='*' [, (str)tab='Tools']]) -> list : 
search_results( (PySearch)arg1 [, (str)search_str='*' [, (str)tab='Tools']]) -> list :
    Search results that match a string.

- `activate_search_result(...)` — activate_search_result( (PySearch)arg1, (str)name, (str)type [, (str)tab='Tools']) -> None : 
activate_search_result( (PySearch)arg1, (str)name, (str)type [, (str)tab='Tools']) -> None :
    Activate a search result.

## API Insight

- `search_results(search_str='*', tab='Tools')` returns a list of matches; `activate_search_result(name, type, tab='Tools')` triggers the selected tool or panel.
- Use `set_tool_favorite`/`set_tool_hidden`/`set_tool_weight` to manage tool availability and prioritisation in the UI.

**Example:**

```python
# Find tools matching 'color' and activate the first result
results = search.search_results('color')
if results:
    name, type = results[0]['name'], results[0]['type']
    search.activate_search_result(name, type)
```

