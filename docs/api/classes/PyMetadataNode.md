# Class: PyMetadataNode

**Module**: `flame`

Class derived from PyNode. This class represents a Metadata node.

## Methods
### Built-in methods
- `set_metadata_value(...)` — set_metadata_value( (PyNode)arg1 [, (str)socket_name='Default' [, (str)key='' [, (object)value=None]]]) -> None : 
set_metadata_value( (PyNode)arg1 [, (str)socket_name='Default' [, (str)key='' [, (object)value=None]]]) -> None :
    Set the metadata on the Node.
    Keyword arguments:
    socket_name -- The socket on which to set the metadata. The default output is used when not specified.
    key -- Metadata key to be set or added.
    value -- Metadata value to be set or edited for the specified key. If None is specified, the current value will revert to the original value.

- `set_metadata_discarded(...)` — set_metadata_discarded( (PyNode)arg1 [, (str)socket_name='Default' [, (str)key='' [, (bool)discarded=True]]]) -> None : 
set_metadata_discarded( (PyNode)arg1 [, (str)socket_name='Default' [, (str)key='' [, (bool)discarded=True]]]) -> None :
    Discard key from the Node's metadata output.
    Keyword arguments:
    socket_name -- The socket on which the discarded status of the metadata must be changed.
    key -- Metadata key to be discarded or restored.
    discarded -- True to discard the key from the node metadata output, False to restore the key.

- `set_metadata_key(...)` — set_metadata_key( (PyNode)arg1 [, (str)socket_name='Default' [, (str)key='' [, (object)name=None]]]) -> None : 
set_metadata_key( (PyNode)arg1 [, (str)socket_name='Default' [, (str)key='' [, (object)name=None]]]) -> None :
    Rename a metadata key on the Node.
    Keyword arguments:
    socket_name -- The socket on which to rename the key. The default output is used when not specified.
    key -- The current metadata key name to be renamed.
    name -- The new metadata key name. If None, the current key name will revert to its original value.

- `load_node_setup(...)` — load_node_setup( (PyMetadataNode)arg1, (str)file_name [, (bool)edited_keys=True [, (bool)discarded_keys=True [, (bool)added_keys=True [, (bool)replaced_keys=True [, (bool)update_tokens=True]]]]]) -> bool : 
load_node_setup( (PyMetadataNode)arg1, (str)file_name [, (bool)edited_keys=True [, (bool)discarded_keys=True [, (bool)added_keys=True [, (bool)replaced_keys=True [, (bool)update_tokens=True]]]]]) -> bool :
    Load a Metadata Node setup.
    Keywords argument:
    file_name -- the path and file name of the setup.
    edited_keys -- apply edited keys from the setup.
    discarded_keys -- apply discarded keys from the setup.
    added_keys -- apply added keys from the setup.
    replaced_keys -- apply replaced keys from the setup.


