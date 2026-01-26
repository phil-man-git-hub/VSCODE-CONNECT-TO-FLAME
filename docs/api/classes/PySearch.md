# Class: PySearch

**Module**: `flame`

This class represents the search.

## Methods
### `use_weight(...)`

None( (flame.PySearch)arg1) -> bool

### `set_tool_favorite(...)`

set_tool_favorite( (PySearch)arg1, (str)arg2, (str)name, (bool)type) -> None :
    Return the favorite status of a tool.

### `set_tool_hidden(...)`

set_tool_hidden( (PySearch)arg1, (str)arg2, (str)name, (bool)type) -> None :
    Return the hidden status of a tool.

### `set_tool_weight(...)`

set_tool_weight( (PySearch)arg1, (str)arg2, (str)name, (int)type) -> None :
    Return the tool weight.

### `search_results(...)`

search_results( (PySearch)arg1 [, (str)search_str='*' [, (str)tab='Tools']]) -> list :
    Search results that match a string.

### `activate_search_result(...)`

activate_search_result( (PySearch)arg1, (str)name, (str)type [, (str)tab='Tools']) -> None :
    Activate a search result.

