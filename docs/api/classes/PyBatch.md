# Class: PyBatch

**Module**: `flame`

Class derived from PyFlameObject. This class represents a Batch Group.

## Methods
### Properties
- `nodes(...)` — None( (flame.PyBatch)arg1) -> list 
None( (flame.PyBatch)arg1) -> list

- `node_types(...)` — None( (flame.PyBatch)arg1) -> list 
None( (flame.PyBatch)arg1) -> list

- `reels(...)` — None( (flame.PyBatch)arg1) -> list 
None( (flame.PyBatch)arg1) -> list

- `shelf_reels(...)` — None( (flame.PyBatch)arg1) -> list 
None( (flame.PyBatch)arg1) -> list

- `batch_iterations(...)` — None( (flame.PyBatch)arg1) -> list 
None( (flame.PyBatch)arg1) -> list

- `current_iteration(...)` — None( (flame.PyBatch)arg1) -> object 
None( (flame.PyBatch)arg1) -> object

- `contexts(...)` — None( (flame.PyBatch)arg1) -> dict 
None( (flame.PyBatch)arg1) -> dict

- `cursor_position(...)` — None( (flame.PyBatch)arg1) -> tuple 
None( (flame.PyBatch)arg1) -> tuple

- `opened(...)` — None( (flame.PyBatch)arg1) -> bool 
None( (flame.PyBatch)arg1) -> bool

- `current_iteration_number(...)` — None( (flame.PyBatch)arg1) -> int 
None( (flame.PyBatch)arg1) -> int


### Built-in methods
- `get_node(...)` — get_node( (PyBatch)arg1, (str)node_name) -> object : 
get_node( (PyBatch)arg1, (str)node_name) -> object :
    Return a Batch node object with a name matching the parameter. Every node in a Batch schematic has a unique name: no duplicates allowed.
    Keyword argument:
    node_name -- Node name.

- `create_node(...)` — create_node( (PyBatch)arg1, (str)node_type [, (str)file_path='']) -> object : 
create_node( (PyBatch)arg1, (str)node_type [, (str)file_path='']) -> object :
    Create a Batch node object in the Batch schematic.
     Keyword argument:
    node_type -- Must be a value from the PyBatch.node_types or the name of a node in the User, Project, or Shared bin.

- `connect_nodes(...)` — connect_nodes( (PyBatch)arg1, (PyNode)output_node, (str)output_socket_name='Default', (PyNode)input_node [, (str)input_socket_name='Default']) -> bool : 
connect_nodes( (PyBatch)arg1, (PyNode)output_node, (str)output_socket_name='Default', (PyNode)input_node [, (str)input_socket_name='Default']) -> bool :
    Connect two nodes in the Batch schematic.
    Keyword arguments:
    output_node -- The Batch node object, the origin of the connection.
    output_socket_name -- The name of the output socket where the connector starts; use *Default* to use the first output socket, usually *Result*.
    input_node -- The child Batch node object, the target of the connection.
    input_socket_name -- The name of the input socket where the connector ends; use *Default* to use the first input socket, usually *Front*. Using *Default* on an Action node connects to the Background socket. To connect to an Action media node, use <ActionNode>.media_nodes[].

- `disconnect_node(...)` — disconnect_node( (PyBatch)arg1, (PyNode)node [, (str)input_socket_name='']) -> bool : 
disconnect_node( (PyBatch)arg1, (PyNode)node [, (str)input_socket_name='']) -> bool :
    Disconnect the input links of a given node, given an input socket.
    Keyword arguments:
    node -- The Batch node object, the origin of the connection.
    input_socket_name -- The name of the input socket to disconnect.

- `mimic_link(...)` — mimic_link( (PyBatch)arg1, (PyNode)leader_node, (PyNode)follower_node) -> bool : 
mimic_link( (PyBatch)arg1, (PyNode)leader_node, (PyNode)follower_node) -> bool :
    Create a Mimic Link between two Batch nodes. They must be of the same node_type.
    Keyword arguments:
    leader_node -- The node being mimicked.
    follower_node -- The node doing the mimicking.

- `clear_context(...)` — clear_context( (PyBatch)arg1, (int)index) -> bool : 
clear_context( (PyBatch)arg1, (int)index) -> bool :
    Clear a specific Context view in the Batch Group.

- `clear_all_contexts(...)` — clear_all_contexts( (PyBatch)arg1) -> bool : 
clear_all_contexts( (PyBatch)arg1) -> bool :
    Clear all registered Context views in the Batch Group.

- `organize(...)` — organize( (PyBatch)arg1) -> bool : 
organize( (PyBatch)arg1) -> bool :
    Clean up the nodes layout in the Batch schematic.

- `frame_selected(...)` — frame_selected( (PyBatch)arg1) -> bool : 
frame_selected( (PyBatch)arg1) -> bool :
    Set the Batch schematic view to frame the nodes selected in the Batch schematic.

- `frame_all(...)` — frame_all( (PyBatch)arg1) -> bool : 
frame_all( (PyBatch)arg1) -> bool :
    Set the Batch schematic view to frame all the nodes in the Batch schematic.

- `import_clip(...)` — import_clip( (PyBatch)arg1, (str)file_path, (str)reel_name) -> object : 
import_clip( (PyBatch)arg1, (str)file_path, (str)reel_name) -> object :
    Import a clip using the Import node, and create a Clip node.
    Keyword arguments:
    file_path -- The path to the media can be:
     - A path to a single media file.
     - A path to a sequence of media files (ie "/dir/clip.[100-2000].dpx").
     - A pattern to media files (ie "/dir/name_v{version}.{frame}.{extension}").reel_name -- The name of the destination Schematic Reel.

- `import_clips(...)` — import_clips( (PyBatch)arg1, (object)file_paths, (str)reel_name) -> object : 
import_clips( (PyBatch)arg1, (object)file_paths, (str)reel_name) -> object :
    Import clips using the Import node, and then create Clip nodes in the Schematic Reel.
    Keyword arguments:
    file_paths -- A path, or a list of paths, to the media that can be:
     - A path to a single media file.
     - A path to a sequence of media files (ie "/dir/clip.[100-2000].dpx").
     - A pattern to media files (ie "/dir/name_v{version}.{frame}.{extension}").reel_name -- The name of the destination Schematic Reel.

- `save_setup(...)` — save_setup( (PyBatch)arg1, (str)setup_path) -> bool : 
save_setup( (PyBatch)arg1, (str)setup_path) -> bool :
    Save the Batch Group setup to disk. Includes media paths for clip node object, but not the media files themselves.
    Keyword argument:
    setup_path -- The filepath includes the filename. File extension must be .batch.

- `append_setup(...)` — append_setup( (PyBatch)arg1, (str)setup_path [, (bool)confirm=True]) -> bool : 
append_setup( (PyBatch)arg1, (str)setup_path [, (bool)confirm=True]) -> bool :
    Append a Batch setup file to the existing Batch setup.
    Keywords arguments:
    setup_path -- A path and a filename must be defined as arguments.
    confirm -- Set to True (default) to display a dialogue box in case of

- `set_viewport_layout(...)` — set_viewport_layout( (PyBatch)arg1, (object)num_views) -> bool : 
set_viewport_layout( (PyBatch)arg1, (object)num_views) -> bool :
    Set the viewport layout for Batch.
    Keyword argument:
    num_views -- The layout used. (1-Up, 2-Up, 3-Up, 3-Up Split Top, 3-Up Split Left, 3-Up Split Right, 3-Up Split Bottom, 4-Up Split, 4-Up)

- `create_batch_group(...)` — create_batch_group( (PyBatch)arg1, (str)name [, (object)nb_reels=None [, (object)nb_shelf_reels=None [, (list)reels=[] [, (list)shelf_reels=[] [, (int)start_frame=1 [, (object)duration=None]]]]]]) -> object : 
create_batch_group( (PyBatch)arg1, (str)name [, (object)nb_reels=None [, (object)nb_shelf_reels=None [, (list)reels=[] [, (list)shelf_reels=[] [, (int)start_frame=1 [, (object)duration=None]]]]]]) -> object :
    Create a new Batch Group object in the Desktop catalogue.
    Keyword arguments:
    name -- Name of the Batch Group.
    nb_reels -- Number of reels created. *reels* overrides *nb_reels*.
    nb_shelf_reels -- Number of shelf reels. The first shelf reel created is named Batch Renders. *shelf_reels* ovverides *nb_shelf_reels*.
    reels -- A list of reel names. Overrides *nb_reels*.
    shelf_reels -- A list of shelf reel names. Overrides *nb_shelf_reels*.
    start_frame -- The Batch Group's start frame. No timecodes, only a frame value.
    duration -- The number of frames. Sets the Duration field in the Batch UI. Will be set to the first clip duration when not specified.

- `encompass_nodes(...)` — encompass_nodes( (PyBatch)arg1, (list)nodes) -> object : 
encompass_nodes( (PyBatch)arg1, (list)nodes) -> object :
    Create a Compass around a list of nodes in the Batch schematic.
     Keyword argument:
    nodes -- List of strings of node names.

- `select_nodes(...)` — select_nodes( (PyBatch)arg1, (object)nodes) -> bool : 
select_nodes( (PyBatch)arg1, (object)nodes) -> bool :
    Select nodes.
    Keyword argument:
    nodes -- A list of the names of Batch node objects.

- `open(...)` — open( (PyBatch)arg1) -> bool : 
open( (PyBatch)arg1) -> bool :
    Open the Batch Group and display it in the Batch view.

- `close(...)` — close( (PyBatch)arg1) -> bool : 
close( (PyBatch)arg1) -> bool :
    Close the Batch Group. You cannot close the Batch Group currently selected.
    Closing a Batch Group frees up the application it occupies when open. The size of the used memory is significant if in Batch Group schematic hosts many Action nodes with textures or 3D geoms.

- `clear(...)` — clear( (PyBatch)arg1 [, (bool)confirm=True]) -> bool : 
clear( (PyBatch)arg1 [, (bool)confirm=True]) -> bool :
    Clear the Batch Group.

- `save(...)` — save( (PyBatch)arg1) -> object : 
save( (PyBatch)arg1) -> object :
    Save the Batch Group to the location defined by PyDesktop.destination.

- `append_to_setup(...)` — append_to_setup( (PyBatch)arg1, (PyBatchIteration)batch_iteration) -> bool : 
append_to_setup( (PyBatch)arg1, (PyBatchIteration)batch_iteration) -> bool :
    Append a Batch Iteration object to the Batch Group's setup.

- `append_to_batch(...)` — append_to_batch( (PyBatch)arg1, (PyBatchIteration)batch_iteration) -> bool : 
append_to_batch( (PyBatch)arg1, (PyBatchIteration)batch_iteration) -> bool :
    Append a Batch Iteration object to the current Batch Group. A duplicate Batch Iteration object is renamed to the next available *vDD*. Batch Iteration objects are displayed in the Iterations folder. Iterations folder is a UI construction, not accessible directly.

- `open_as_batch_group(...)` — open_as_batch_group( (PyBatch)arg1 [, (bool)confirm=True]) -> bool : 
open_as_batch_group( (PyBatch)arg1 [, (bool)confirm=True]) -> bool :
    Open a Batch Group as a new Batch Group, adding it to PyDesktop.batch_groups. Can only be called from a Library.

- `replace_setup(...)` — replace_setup( (PyBatch)arg1, (PyBatchIteration)batch_iteration [, (bool)confirm=True]) -> bool : 
replace_setup( (PyBatch)arg1, (PyBatchIteration)batch_iteration [, (bool)confirm=True]) -> bool :
    Replace the Batch Group setup with the specified Batch Iteration. Cannot be called on the Batch Group currently selected and displayed in the Batch view.

- `create_reel(...)` — create_reel( (PyBatch)arg1, (str)name) -> object : 
create_reel( (PyBatch)arg1, (str)name) -> object :
    Create a new Schematic Reel in the Batch Gtroup.

- `create_shelf_reel(...)` — create_shelf_reel( (PyBatch)arg1, (str)name) -> object : 
create_shelf_reel( (PyBatch)arg1, (str)name) -> object :
    Create a new Shelf Reel in the Batch Group.

- `clear_colour(...)` — clear_colour( (PyBatch)arg1) -> None : 
clear_colour( (PyBatch)arg1) -> None :
    Clear the colour of an object in the Media Panel.

- `go_to(...)` — go_to( (PyBatch)arg1) -> bool : 
go_to( (PyBatch)arg1) -> bool :
    Display and set the Batch tab as the active environment.

- `load_setup(...)` — load_setup( (PyBatch)arg1, (str)setup_path) -> bool : 
load_setup( (PyBatch)arg1, (str)setup_path) -> bool :
    Load a Batch setup from disk and replace the current Batch Group's setup.
     Keyword argument:
    setup_path -- Filepath + Batch Setup filename.

- `clear_setup(...)` — clear_setup( (PyBatch)arg1) -> bool : 
clear_setup( (PyBatch)arg1) -> bool :
    Clear the Batch Group's setup.

- `iterate(...)` — iterate( (PyBatch)arg1 [, (int)index=-1]) -> object : 
iterate( (PyBatch)arg1 [, (int)index=-1]) -> object :
    Iterate the current Batch Setup, creating a new iteration named BatchSetupName_X, where X is the Batch Iteration's index, and starts at 001.
     Keyword argument:
    index -- Specifies the iteration's index. If none is specified, the iteration is assigned the next available index (max index + 1). If the index matches that of an existing Batch Iteration, its overwrites the iteration without warning.

- `save_current_iteration(...)` — save_current_iteration( (PyBatch)arg1) -> object : 
save_current_iteration( (PyBatch)arg1) -> object :
    Save the current Batch Group setup to the location defined by PyDesktop.destination.

- `render(...)` — render( (PyBatch)arg1 [, (str)render_option='Foreground' [, (bool)generate_proxies=False [, (bool)include_history=False]]]) -> bool : 
render( (PyBatch)arg1 [, (str)render_option='Foreground' [, (bool)generate_proxies=False [, (bool)include_history=False]]]) -> bool :
    Trigger the rendering of the Batch Group setup. Every active Render and Write File nodes render. If specified render_option is not supported by the workstation, returns an error.
    Keyword arguments:
    render_option -- Defines the rendering method used. (Foreground, Background Reactor, Burn)
    generate_proxies -- Set to True to render at proxy resolution. (Default: False)
    include_history -- Set to True to create History with the rendering. (Default:False)


