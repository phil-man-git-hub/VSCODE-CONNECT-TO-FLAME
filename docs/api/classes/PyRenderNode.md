# Class: PyRenderNode

**Module**: `flame`

Class derived from PyNode. This class represents a Render node.

## Methods
### `channels(...)`

None( (flame.PyRenderNode)arg1) -> list

### `set_channel_name(...)`

set_channel_name( (PyRenderNode)arg1, (object)channel, (object)name) -> None :
    Rename a channel, using its index or front channel name as the index key.
    Keyword arguments:
    channel -- The channel to rename. Can be the channel index or the current name of the channel's front socket.
    name -- The new name of the channel. The type is either a string or a tuple. A Write File node always takes a string. A Render node takes a string or a tuple.
    In a Render node, a string only sets the name of the channel's front socket; the function creates the name of the matte socket by appending '_alpha' to 'name'. In the UI, the channel is flagged 'Sync'. A Write File node has only one socket per channel, and requires only a string to set a socket name.
    In a Render node, a tuple sets the names of the front and matte sockets. In the UI, the channel is not flagged 'Sync'. A Write File node does not accept a tuple.

### `set_metadata_value(...)`

set_metadata_value( (PyNode)arg1 [, (str)socket_name='Default' [, (str)key='' [, (object)value=None [, (bool)is_dynamic=False]]]]) -> None :
    Set the metadata on the Node.
    Keyword arguments:
    socket_name -- The socket on which to set the metadata. The default output is used when not specified.
    key -- Metadata key to be set or added.
    value -- Metadata value to be set or edited for the specified key. If None is specified, the current value will revert to the original value.
    is_dynamic -- Set the Metadata value to be resolved dynamically if it contains tokens.
    

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
    

