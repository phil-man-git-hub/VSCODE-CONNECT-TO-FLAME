# Class: PyClipNode

**Module**: `flame`

Class derived from PyNode. This class represents a Clip node.

## Methods
### `clip(...)`

None( (flame.PyClipNode)arg1) -> object

### `version_uids(...)`

None( (flame.PyClipNode)arg1) -> list

### `version_uid(...)`

None( (flame.PyClipNode)arg1) -> object

### `set_version_uid(...)`

set_version_uid( (PyClipNode)arg1, (str)version_uid) -> bool :
    Set the clip node's current version unique ID.
    Keywords argument:
    version_uid -- version unique ID.

### `set_metadata_value(...)`

set_metadata_value( (PyNode)arg1 [, (str)socket_name='Default' [, (str)key='' [, (object)value=None]]]) -> None :
    Set the metadata on the Node.
    Keyword arguments:
    socket_name -- The socket on which to set the metadata. The default output is used when not specified.
    key -- Metadata key to be set or added.
    value -- Metadata value to be set or edited for the specified key. If None is specified, the current value will revert to the original value.
    

### `set_metadata_discarded(...)`

set_metadata_discarded( (PyNode)arg1 [, (str)socket_name='Default' [, (str)key='' [, (bool)discarded=True]]]) -> None :
    Discard key from the Node's metadata output.
    Keyword arguments:
    socket_name -- The socket on which the discarded status of the metadata must be changed.
    key -- Metadata key to be discarded or restored.
    discarded -- True to discard the key from the node metadata output, False to restore the key.
    

### `set_metadata_key(...)`

set_metadata_key( (PyNode)arg1 [, (str)socket_name='Default' [, (str)key='' [, (object)name=None]]]) -> None :
    Rename a metadata key on the Node.
    Keyword arguments:
    socket_name -- The socket on which to rename the key. The default output is used when not specified.
    key -- The current metadata key name to be renamed.
    name -- The new metadata key name. If None, the current key name will revert to its original value.
    

