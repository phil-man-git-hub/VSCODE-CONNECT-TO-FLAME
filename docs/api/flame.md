# Module: flame

## Classes
### class [PyActionFamilyNode](classes/PyActionFamilyNode.md)

Class derived from PyNode. Represents an Action Family node object.

#### Methods
- `node_types(...)` — None( (flame.PyActionFamilyNode)arg1) -> list
- `nodes(...)` — None( (flame.PyActionFamilyNode)arg1) -> list
- `cursor_position(...)` — None( (flame.PyActionFamilyNode)arg1) -> tuple
- `all_tabs(...)` — None( (flame.PyActionFamilyNode)arg1) -> list
- `left_tabs(...)` — None( (flame.PyActionFamilyNode)arg1) -> list
- `right_tabs(...)` — None( (flame.PyActionFamilyNode)arg1) -> list
- `create_node(...)` — create_node( (PyActionFamilyNode)arg1, (str)node_type [, (str)file_path='' [, (bool)is_udim=False [, (int)tile_resolution=0 [, (str)input_colour_space='']]]]) -> object :
- `organize(...)` — organize( (PyActionFamilyNode)arg1) -> bool :
- `get_node(...)` — get_node( (PyActionFamilyNode)arg1, (str)node_name) -> object :
- `connect_nodes(...)` — connect_nodes( (PyActionFamilyNode)arg1, (PyFlameObject)parent_node, (PyFlameObject)child_node [, (str)link_type='Default']) -> bool :
- `disconnect_nodes(...)` — disconnect_nodes( (PyActionFamilyNode)arg1, (PyFlameObject)parent_node, (PyFlameObject)child_node [, (str)link_type='Default']) -> bool :
- `media_layers(...)` — None( (flame.PyActionFamilyNode)arg1) -> list
- `clear_schematic(...)` — clear_schematic( (PyActionFamilyNode)arg1) -> bool :
- `encompass_nodes(...)` — encompass_nodes( (PyActionFamilyNode)arg1, (list)node_list) -> object :

### class [PyActionNode](classes/PyActionNode.md)

Class derived from PyActionFamilyNode. Represents an Action node object.

#### Methods
- `media_nodes(...)` — None( (flame.PyActionNode)arg1) -> list
- `add_media(...)` — add_media( (PyActionFamilyNode)arg1) -> object :
- `import_fbx(...)` — import_fbx( (PyActionFamilyNode)arg1, (str)file_path [, (bool)lights=True [, (bool)cameras=True [, (bool)models=True [, (bool)normals=True [, (bool)mesh_animations=True [, (bool)keep_frame_rate=True [, (bool)bake_animation=False [, (bool)object_properties=True [, (bool)auto_fit=False [, (float)unit_to_pixels=10.0 [, (bool)create_media=True [, (bool)is_udim=False [, (bool)relink_material=True [, (str)input_colour_space='']]]]]]]]]]]]]]) -> list :
- `export_fbx(...)` — export_fbx( (PyActionFamilyNode)arg1, (str)file_path [, (bool)only_selected_nodes=False [, (float)pixel_to_units=0.10000000149011612 [, (str)frame_rate='23.976 fps' [, (bool)bake_animation=False [, (bool)export_axes=True [, (bool)export_point_locators=False [, (bool)combine_material=True [, (bool)duplicate_material=False]]]]]]]]) -> bool :
- `read_fbx(...)` — read_fbx( (PyActionFamilyNode)arg1, (str)file_path [, (bool)lights=True [, (bool)cameras=True [, (bool)models=True [, (bool)normals=True [, (bool)mesh_animations=True [, (bool)keep_frame_rate=True [, (bool)bake_animation=False [, (bool)object_properties=True [, (bool)auto_fit=False [, (float)unit_to_pixels=10.0 [, (bool)is_udim=False [, (bool)relink_material=True [, (str)input_colour_space='']]]]]]]]]]]]]) -> object :
- `import_abc(...)` — import_abc( (PyActionFamilyNode)arg1, (str)file_path [, (bool)lights=True [, (bool)cameras=True [, (bool)models=True [, (bool)normals=True [, (bool)mesh_animations=True [, (str)frame_rate='23.976 fps' [, (bool)auto_fit=False [, (float)unit_to_pixels=10.0 [, (bool)consolidate_geometry=True [, (bool)create_object_group=False]]]]]]]]]]) -> list :
- `read_abc(...)` — read_abc( (PyActionFamilyNode)arg1, (str)file_path [, (bool)lights=True [, (bool)cameras=True [, (bool)models=True [, (bool)normals=True [, (bool)mesh_animations=True [, (str)frame_rate='23.976 fps' [, (bool)auto_fit=False [, (float)unit_to_pixels=10.0 [, (bool)consolidate_geometry=True [, (bool)create_object_group=False]]]]]]]]]]) -> object :
- `import_psd(...)` — import_psd( (PyActionFamilyNode)arg1, (str)file_path [, (str)input_colour_space='']) -> list :
- `enable_output(...)` — enable_output( (PyActionFamilyNode)arg1, (str)output_type) -> bool :
- `disable_output(...)` — disable_output( (PyActionFamilyNode)arg1, (str)output_type) -> bool :
- `output_types(...)` — None( (flame.PyActionNode)arg1) -> list

### class [PyArchiveEntry](classes/PyArchiveEntry.md)

Class derived from PyFlameObject. Base class for any object displayed in the Media Panel.

#### Methods
- `get_wiretap_storage_id(...)` — get_wiretap_storage_id( (PyArchiveEntry)arg1) -> str :
- `get_wiretap_node_id(...)` — get_wiretap_node_id( (PyArchiveEntry)arg1) -> str :
- `commit(...)` — commit( (PyArchiveEntry)arg1) -> None :
- `clear_colour(...)` — clear_colour( (PyArchiveEntry)arg1) -> None :

### class [PyAttribute](classes/PyAttribute.md)

#### Methods
- `values(...)` — None( (flame.PyAttribute)arg1) -> object
- `set_value(...)` — set_value( (PyAttribute)arg1, (object)arg2) -> bool :
- `get_value(...)` — get_value( (PyAttribute)arg1) -> object :

### class [PyAudioTrack](classes/PyAudioTrack.md)

Object representing an Audio Track.

#### Methods
- `channels(...)` — None( (flame.PyAudioTrack)arg1) -> list
- `stereo(...)` — None( (flame.PyAudioTrack)arg1) -> bool
- `copy_to_media_panel(...)` — copy_to_media_panel( (PyAudioTrack)arg1, (PyArchiveEntry)destination [, (str)duplicate_action='add']) -> object :

### class [PyBatch](classes/PyBatch.md)

Class derived from PyFlameObject. This class represents a Batch Group.

#### Methods
- `nodes(...)` — None( (flame.PyBatch)arg1) -> list
- `node_types(...)` — None( (flame.PyBatch)arg1) -> list
- `reels(...)` — None( (flame.PyBatch)arg1) -> list
- `shelf_reels(...)` — None( (flame.PyBatch)arg1) -> list
- `batch_iterations(...)` — None( (flame.PyBatch)arg1) -> list
- `current_iteration(...)` — None( (flame.PyBatch)arg1) -> object
- `contexts(...)` — None( (flame.PyBatch)arg1) -> dict
- `cursor_position(...)` — None( (flame.PyBatch)arg1) -> tuple
- `opened(...)` — None( (flame.PyBatch)arg1) -> bool
- `current_iteration_number(...)` — None( (flame.PyBatch)arg1) -> int
- `get_node(...)` — get_node( (PyBatch)arg1, (str)node_name) -> object :
- `create_node(...)` — create_node( (PyBatch)arg1, (str)node_type [, (str)file_path='']) -> object :
- `connect_nodes(...)` — connect_nodes( (PyBatch)arg1, (PyNode)output_node, (str)output_socket_name='Default', (PyNode)input_node [, (str)input_socket_name='Default']) -> bool :
- `disconnect_node(...)` — disconnect_node( (PyBatch)arg1, (PyNode)node [, (str)input_socket_name='']) -> bool :
- `mimic_link(...)` — mimic_link( (PyBatch)arg1, (PyNode)leader_node, (PyNode)follower_node) -> bool :
- `clear_context(...)` — clear_context( (PyBatch)arg1, (int)index) -> bool :
- `clear_all_contexts(...)` — clear_all_contexts( (PyBatch)arg1) -> bool :
- `organize(...)` — organize( (PyBatch)arg1) -> bool :
- `frame_selected(...)` — frame_selected( (PyBatch)arg1) -> bool :
- `frame_all(...)` — frame_all( (PyBatch)arg1) -> bool :
- `import_clip(...)` — import_clip( (PyBatch)arg1, (str)file_path, (str)reel_name) -> object :
- `import_clips(...)` — import_clips( (PyBatch)arg1, (object)file_paths, (str)reel_name) -> object :
- `save_setup(...)` — save_setup( (PyBatch)arg1, (str)setup_path) -> bool :
- `append_setup(...)` — append_setup( (PyBatch)arg1, (str)setup_path [, (bool)confirm=True]) -> bool :
- `set_viewport_layout(...)` — set_viewport_layout( (PyBatch)arg1, (object)num_views) -> bool :
- `create_batch_group(...)` — create_batch_group( (PyBatch)arg1, (str)name [, (object)nb_reels=None [, (object)nb_shelf_reels=None [, (list)reels=[] [, (list)shelf_reels=[] [, (int)start_frame=1 [, (object)duration=None]]]]]]) -> object :
- `encompass_nodes(...)` — encompass_nodes( (PyBatch)arg1, (list)nodes) -> object :
- `select_nodes(...)` — select_nodes( (PyBatch)arg1, (object)nodes) -> bool :
- `open(...)` — open( (PyBatch)arg1) -> bool :
- `close(...)` — close( (PyBatch)arg1) -> bool :
- `clear(...)` — clear( (PyBatch)arg1 [, (bool)confirm=True]) -> bool :
- `save(...)` — save( (PyBatch)arg1) -> object :
- `append_to_setup(...)` — append_to_setup( (PyBatch)arg1, (PyBatchIteration)batch_iteration) -> bool :
- `append_to_batch(...)` — append_to_batch( (PyBatch)arg1, (PyBatchIteration)batch_iteration) -> bool :
- `open_as_batch_group(...)` — open_as_batch_group( (PyBatch)arg1 [, (bool)confirm=True]) -> bool :
- `replace_setup(...)` — replace_setup( (PyBatch)arg1, (PyBatchIteration)batch_iteration [, (bool)confirm=True]) -> bool :
- `create_reel(...)` — create_reel( (PyBatch)arg1, (str)name) -> object :
- `create_shelf_reel(...)` — create_shelf_reel( (PyBatch)arg1, (str)name) -> object :
- `clear_colour(...)` — clear_colour( (PyBatch)arg1) -> None :
- `go_to(...)` — go_to( (PyBatch)arg1) -> bool :
- `load_setup(...)` — load_setup( (PyBatch)arg1, (str)setup_path) -> bool :
- `clear_setup(...)` — clear_setup( (PyBatch)arg1) -> bool :
- `iterate(...)` — iterate( (PyBatch)arg1 [, (int)index=-1]) -> object :
- `save_current_iteration(...)` — save_current_iteration( (PyBatch)arg1) -> object :
- `render(...)` — render( (PyBatch)arg1 [, (str)render_option='Foreground' [, (bool)generate_proxies=False [, (bool)include_history=False]]]) -> bool :

### class [PyBatchIteration](classes/PyBatchIteration.md)

Class derived from PyArchiveEntry. This class represents a Batch Iteration.

#### Methods
- `iteration_number(...)` — None( (flame.PyBatchIteration)arg1) -> int
- `open_as_batch_group(...)` — open_as_batch_group( (PyBatchIteration)arg1 [, (bool)confirm=True]) -> bool :

### class [PyBrowser](classes/PyBrowser.md)

This class represents the file browser.

#### Methods
- `show(...)` — show( (PyBrowser)arg1, (str)default_path [, (object)extension='' [, (bool)select_directory=False [, (bool)multi_selection=False [, (object)include_resolution=False [, (str)title='Load']]]]]) -> None :
- `selection(...)` — None( (flame.PyBrowser)arg1) -> object
- `sequence_mode(...)` — None( (flame.PyBrowser)arg1) -> bool
- `width(...)` — None( (flame.PyBrowser)arg1) -> object
- `height(...)` — None( (flame.PyBrowser)arg1) -> object
- `scaling_presets_value(...)` — None( (flame.PyBrowser)arg1) -> object
- `bit_depth(...)` — None( (flame.PyBrowser)arg1) -> object
- `frame_ratio(...)` — None( (flame.PyBrowser)arg1) -> object
- `scan_mode(...)` — None( (flame.PyBrowser)arg1) -> str
- `colour_space(...)` — None( (flame.PyBrowser)arg1) -> str
- `resize_mode(...)` — None( (flame.PyBrowser)arg1) -> str
- `resize_filter(...)` — None( (flame.PyBrowser)arg1) -> str
- `resolution(...)` — None( (flame.PyBrowser)arg1) -> str

### class [PyClip](classes/PyClip.md)

CLass derived from PyArchiveEntry. This class represents a Clip.

#### Methods
- `frame_rate(...)` — None( (flame.PyClip)arg1) -> object
- `duration(...)` — None( (flame.PyClip)arg1) -> object
- `versions(...)` — None( (flame.PyClip)arg1) -> list
- `audio_tracks(...)` — None( (flame.PyClip)arg1) -> list
- `markers(...)` — None( (flame.PyClip)arg1) -> list
- `subtitles(...)` — None( (flame.PyClip)arg1) -> list
- `width(...)` — None( (flame.PyClip)arg1) -> int
- `height(...)` — None( (flame.PyClip)arg1) -> int
- `bit_depth(...)` — None( (flame.PyClip)arg1) -> int
- `ratio(...)` — None( (flame.PyClip)arg1) -> float
- `scan_mode(...)` — None( (flame.PyClip)arg1) -> str
- `colour_primaries(...)` — None( (flame.PyClip)arg1) -> int
- `transfer_characteristics(...)` — None( (flame.PyClip)arg1) -> int
- `matrix_coefficients(...)` — None( (flame.PyClip)arg1) -> int
- `proxy_resolution(...)` — None( (flame.PyClip)arg1) -> object
- `has_deliverables(...)` — None( (flame.PyClip)arg1) -> bool
- `has_history(...)` — None( (flame.PyClip)arg1) -> bool
- `unlinked(...)` — None( (flame.PyClip)arg1) -> str
- `creation_date(...)` — None( (flame.PyClip)arg1) -> str
- `archive_date(...)` — None( (flame.PyClip)arg1) -> str
- `archive_error(...)` — None( (flame.PyClip)arg1) -> str
- `essence_uid(...)` — None( (flame.PyClip)arg1) -> str
- `source_uid(...)` — None( (flame.PyClip)arg1) -> str
- `original_source_uid(...)` — None( (flame.PyClip)arg1) -> str
- `sample_rate(...)` — None( (flame.PyClip)arg1) -> str
- `cached(...)` — None( (flame.PyClip)arg1) -> str
- `start_frame(...)` — None( (flame.PyClip)arg1) -> int
- `open_as_sequence(...)` — open_as_sequence( (PyClip)arg1) -> object :
- `open_container(...)` — open_container( (PyClip)arg1) -> bool :
- `close_container(...)` — close_container( (PyClip)arg1) -> None :
- `reformat(...)` — reformat( (PyClip)arg1 [, (int)width=0 [, (int)height=0 [, (float)ratio=0.0 [, (int)bit_depth=0 [, (str)scan_mode='' [, (str)frame_rate='' [, (str)resize_mode='Letterbox']]]]]]]) -> None :
- `create_marker(...)` — create_marker( (PyClip)arg1, (object)location) -> object :
- `change_dominance(...)` — change_dominance( (PyClip)arg1, (str)scan_mode) -> None :
- `cache_media(...)` — cache_media( (PyClip)arg1 [, (str)mode='current']) -> bool :
- `flush_cache_media(...)` — flush_cache_media( (PyClip)arg1 [, (str)mode='current']) -> bool :
- `clear_cache_media(...)` — clear_cache_media( (PyClip)arg1 [, (str)mode='current']) -> bool :
- `render(...)` — render( (PyClip)arg1 [, (str)render_mode='All' [, (str)render_option='Foreground' [, (str)render_quality='Full Resolution' [, (str)effect_type='' [, (str)effect_caching_mode='Current' [, (bool)include_handles=False]]]]]]) -> bool :
- `flush_renders(...)` — flush_renders( (PyClip)arg1) -> None :
- `clear_renders(...)` — clear_renders( (PyClip)arg1) -> None :
- `is_rendered(...)` — is_rendered( (PyClip)arg1 [, (bool)top_only=False [, (str)render_quality='Full Resolution']]) -> bool :
- `save(...)` — save( (PyClip)arg1) -> bool :
- `cut(...)` — cut( (PyClip)arg1, (PyTime)cut_time) -> None :
- `get_colour_space(...)` — get_colour_space( (PyClip)arg1 [, (PyTime)time=None]) -> str :
- `change_start_frame(...)` — change_start_frame( (PyClip)arg1, (int)start_frame [, (bool)use_segment_connections=True]) -> None :
- `get_metadata(...)` — get_metadata( (PyClip)arg1 [, (str)key='' [, (PyTime)time=None]]) -> object :

### class [PyClipNode](classes/PyClipNode.md)

Class derived from PyNode. This class represents a Clip node.

#### Methods
- `clip(...)` — None( (flame.PyClipNode)arg1) -> object
- `version_uids(...)` — None( (flame.PyClipNode)arg1) -> list
- `version_uid(...)` — None( (flame.PyClipNode)arg1) -> object
- `set_version_uid(...)` — set_version_uid( (PyClipNode)arg1, (str)version_uid) -> bool :
- `set_metadata_value(...)` — set_metadata_value( (PyNode)arg1 [, (str)socket_name='Default' [, (str)key='' [, (object)value=None]]]) -> None :
- `set_metadata_discarded(...)` — set_metadata_discarded( (PyNode)arg1 [, (str)socket_name='Default' [, (str)key='' [, (bool)discarded=True]]]) -> None :
- `set_metadata_key(...)` — set_metadata_key( (PyNode)arg1 [, (str)socket_name='Default' [, (str)key='' [, (object)name=None]]]) -> None :

### class [PyClrMgmtNode](classes/PyClrMgmtNode.md)

Object representing a Colour Mgmt node.

#### Methods
- `set_context_variable(...)` — set_context_variable( (PyClrMgmtNode)arg1, (str)name, (str)value) -> None :
- `get_context_variables(...)` — get_context_variables( (PyClrMgmtNode)arg1) -> dict :
- `reset_context_variables(...)` — reset_context_variables( (PyClrMgmtNode)arg1) -> None :
- `import_transform(...)` — import_transform( (PyClrMgmtNode)arg1, (str)file_path) -> None :

### class [PyCoCameraAnalysis](classes/PyCoCameraAnalysis.md)

Class derived from PyCoNode. This class represents the camera analysis node in the Action schematic.

#### Methods
- `resetAnalysis(...)` — resetAnalysis( (PyCoCameraAnalysis)arg1) -> bool :
- `analyseRange(...)` — analyseRange( (PyCoCameraAnalysis)arg1, (object)arg2, (object)start) -> bool :

### class [PyCoCompass](classes/PyCoCompass.md)

Class derived from PyCoNode. This class represents the compass node in the Action schematic.

#### Methods
- `nodes(...)` — None( (flame.PyCoCompass)arg1) -> list

### class [PyCoNode](classes/PyCoNode.md)

Class derived from PyFlameObject. This class represents an Action node in the Action schematic.

#### Methods
- `assign_media(...)` — assign_media( (PyCoNode)arg1, (object)media_name) -> bool :
- `cache_range(...)` — cache_range( (PyCoNode)arg1, (object)arg2, (object)start) -> bool :
- `add_reference(...)` — add_reference( (PyCoNode)arg1, (object)frame) -> bool :
- `parents(...)` — parents( (PyCoNode)arg1 [, (str)link_type='Default']) -> list :
- `children(...)` — children( (PyCoNode)arg1 [, (str)link_type='Default']) -> list :
- `type(...)` — None( (flame.PyCoNode)arg1) -> str

### class [PyColourMgtTimelineFX](classes/PyColourMgtTimelineFX.md)

Object representing a Colour Mgmt Timeline FX.

#### Methods
- `set_context_variable(...)` — set_context_variable( (PyColourMgtTimelineFX)arg1, (str)name, (str)value) -> None :
- `get_context_variables(...)` — get_context_variables( (PyColourMgtTimelineFX)arg1) -> dict :
- `import_transform(...)` — import_transform( (PyColourMgtTimelineFX)arg1, (str)file_path) -> None :
- `reset_context_variables(...)` — reset_context_variables( (PyColourMgtTimelineFX)arg1) -> None :

### class [PyCompassNode](classes/PyCompassNode.md)

Class derived from PyNode. This class represents a Compass node.

#### Methods
- `nodes(...)` — None( (flame.PyCompassNode)arg1) -> list

### class [PyDesktop](classes/PyDesktop.md)

Class derived from PyArchiveEntry. This class represents a Desktop.

#### Methods
- `children(...)` — None( (flame.PyDesktop)arg1) -> list
- `batch_groups(...)` — None( (flame.PyDesktop)arg1) -> list
- `reel_groups(...)` — None( (flame.PyDesktop)arg1) -> list
- `create_reel_group(...)` — create_reel_group( (PyDesktop)arg1, (str)name) -> object :
- `save(...)` — save( (PyDesktop)arg1) -> bool :
- `create_batch_group(...)` — create_batch_group( (PyDesktop)arg1, (str)name [, (object)nb_reels=None [, (object)nb_shelf_reels=None [, (list)reels=[] [, (list)shelf_reels=[] [, (int)start_frame=1 [, (object)duration=None]]]]]]) -> object :
- `clear(...)` — clear( (PyDesktop)arg1) -> bool :

### class [PyExporter](classes/PyExporter.md)

Object holding export settings.

#### Methods
- `use_top_video_track(...)` — None( (flame.PyExporter)arg1) -> bool
- `export_between_marks(...)` — None( (flame.PyExporter)arg1) -> bool
- `foreground(...)` — None( (flame.PyExporter)arg1) -> bool
- `include_subtitles(...)` — None( (flame.PyExporter)arg1) -> bool
- `export_subtitles_as_files(...)` — None( (flame.PyExporter)arg1) -> bool
- `export_all_subtitles(...)` — None( (flame.PyExporter)arg1) -> bool
- `warn_on_unlinked(...)` — None( (flame.PyExporter)arg1) -> bool
- `warn_on_unrendered(...)` — None( (flame.PyExporter)arg1) -> bool
- `warn_on_pending_render(...)` — None( (flame.PyExporter)arg1) -> bool
- `warn_on_no_media(...)` — None( (flame.PyExporter)arg1) -> bool
- `warn_on_mixed_colour_space(...)` — None( (flame.PyExporter)arg1) -> bool
- `warn_on_reimport_unsupported(...)` — None( (flame.PyExporter)arg1) -> bool
- `keep_timeline_fx_renders(...)` — None( (flame.PyExporter)arg1) -> bool
- `get_presets_base_dir(...)` — get_presets_base_dir( (PyExporter.PresetVisibility)preset_visibility) -> str :
- `get_presets_dir(...)` — get_presets_dir( (PyExporter.PresetVisibility)preset_visibility, (PyExporter.PresetType)preset_type) -> str :
- `export(...)` — export( (PyExporter)arg1, (object)sources, (str)preset_path, (str)output_directory [, (PyExporter.BackgroundJobSettings)background_job_settings=None [, (object)hooks=None [, (object)hooks_user_data=None]]]) -> None :
- `BackgroundJobSettings(...)` — Object holding background export job settings. These settings refer to the Backburner job, server and manager.
- `PresetType(...)` — int([x]) -> integer
- `Image_Sequence(...)` — 
- `Audio(...)` — 
- `Movie(...)` — 
- `Sequence_Publish(...)` — 
- `Distribution_Package(...)` — 
- `PresetVisibility(...)` — int([x]) -> integer
- `User(...)` — 
- `Project(...)` — 
- `Shared(...)` — 
- `Autodesk(...)` — 
- `Flow_Production_Tracking(...)` — 
- `Shotgun(...)` — 

### class [PyFlameObject](classes/PyFlameObject.md)

The basic type of all accessible Flame objects from the python API.

#### Methods
- `attributes(...)` — None( (flame.PyFlameObject)arg1) -> list
- `parent(...)` — None( (flame.PyFlameObject)arg1) -> object

### class [PyFolder](classes/PyFolder.md)

Class derived from PyArchiveEntry. This class represents a Folder.

#### Methods
- `children(...)` — None( (flame.PyFolder)arg1) -> list
- `folders(...)` — None( (flame.PyFolder)arg1) -> list
- `batch_iterations(...)` — None( (flame.PyFolder)arg1) -> list
- `desktops(...)` — None( (flame.PyFolder)arg1) -> list
- `reel_groups(...)` — None( (flame.PyFolder)arg1) -> list
- `reels(...)` — None( (flame.PyFolder)arg1) -> list
- `sequences(...)` — None( (flame.PyFolder)arg1) -> list
- `clips(...)` — None( (flame.PyFolder)arg1) -> list
- `batch_groups(...)` — None( (flame.PyFolder)arg1) -> list
- `clear(...)` — clear( (PyFolder)arg1 [, (bool)confirm=True]) -> bool :
- `create_reel_group(...)` — create_reel_group( (PyFolder)arg1, (str)name) -> object :
- `create_reel(...)` — create_reel( (PyFolder)arg1, (str)name) -> object :
- `create_folder(...)` — create_folder( (PyFolder)arg1, (str)name) -> object :
- `create_sequence(...)` — create_sequence( (PyFolder)arg1 [, (str)name='Untitled Sequence' [, (int)video_tracks=1 [, (bool)video_stereo=False [, (object)width=None [, (object)height=None [, (object)ratio=None [, (object)bit_depth=None [, (object)scan_mode=None [, (object)frame_rate=None [, (object)start_at=00:00:00+00 [, (object)duration=00:00:00+01 [, (int)audio_tracks=1 [, (bool)audio_stereo=True]]]]]]]]]]]]]) -> object :

### class [PyGMaskTracerNode](classes/PyGMaskTracerNode.md)

Class derived from PyActionFamilyNode. Represents a GMask Tracer node object.

#### Methods
- `import_fbx(...)` — import_fbx( (PyActionFamilyNode)arg1, (str)file_path [, (bool)lights=True [, (bool)cameras=True [, (bool)models=True [, (bool)normals=True [, (bool)mesh_animations=True [, (bool)keep_frame_rate=True [, (bool)bake_animation=False [, (bool)object_properties=True [, (bool)auto_fit=False [, (float)unit_to_pixels=10.0 [, (bool)create_media=True [, (bool)is_udim=False [, (bool)relink_material=True [, (str)input_colour_space='']]]]]]]]]]]]]]) -> list :
- `export_fbx(...)` — export_fbx( (PyActionFamilyNode)arg1, (str)file_path [, (bool)only_selected_nodes=False [, (float)pixel_to_units=0.10000000149011612 [, (str)frame_rate='23.976 fps' [, (bool)bake_animation=False [, (bool)export_axes=True [, (bool)export_point_locators=False [, (bool)combine_material=True [, (bool)duplicate_material=False]]]]]]]]) -> bool :
- `read_fbx(...)` — read_fbx( (PyActionFamilyNode)arg1, (str)file_path [, (bool)lights=True [, (bool)cameras=True [, (bool)models=True [, (bool)normals=True [, (bool)mesh_animations=True [, (bool)keep_frame_rate=True [, (bool)bake_animation=False [, (bool)object_properties=True [, (bool)auto_fit=False [, (float)unit_to_pixels=10.0 [, (bool)is_udim=False [, (bool)relink_material=True [, (str)input_colour_space='']]]]]]]]]]]]]) -> object :
- `import_abc(...)` — import_abc( (PyActionFamilyNode)arg1, (str)file_path [, (bool)lights=True [, (bool)cameras=True [, (bool)models=True [, (bool)normals=True [, (bool)mesh_animations=True [, (str)frame_rate='23.976 fps' [, (bool)auto_fit=False [, (float)unit_to_pixels=10.0 [, (bool)consolidate_geometry=True [, (bool)create_object_group=False]]]]]]]]]]) -> list :
- `read_abc(...)` — read_abc( (PyActionFamilyNode)arg1, (str)file_path [, (bool)lights=True [, (bool)cameras=True [, (bool)models=True [, (bool)normals=True [, (bool)mesh_animations=True [, (str)frame_rate='23.976 fps' [, (bool)auto_fit=False [, (float)unit_to_pixels=10.0 [, (bool)consolidate_geometry=True [, (bool)create_object_group=False]]]]]]]]]]) -> object :
- `import_psd(...)` — import_psd( (PyActionFamilyNode)arg1, (str)file_path [, (str)input_colour_space='']) -> list :
- `enable_output(...)` — enable_output( (PyActionFamilyNode)arg1, (str)output_type) -> bool :
- `disable_output(...)` — disable_output( (PyActionFamilyNode)arg1, (str)output_type) -> bool :
- `output_types(...)` — None( (flame.PyGMaskTracerNode)arg1) -> list

### class [PyHDRNode](classes/PyHDRNode.md)

Object representing a HDR node.

#### Methods
- `analysis_status(...)` — None( (flame.PyHDRNode)arg1) -> object
- `analyze(...)` — analyze( (PyHDRNode)arg1 [, (str)analyze_mode='Current Shot']) -> None :
- `keep_analysis(...)` — keep_analysis( (PyHDRNode)arg1) -> None :
- `reset_analysis(...)` — reset_analysis( (PyHDRNode)arg1) -> None :
- `interpolate_trims(...)` — interpolate_trims( (PyHDRNode)arg1) -> None :
- `reset_trims(...)` — reset_trims( (PyHDRNode)arg1) -> None :
- `export_DolbyVision_xml(...)` — export_DolbyVision_xml( (PyHDRNode)arg1, (str)file_name [, (str)comment='']) -> None :
- `import_DolbyVision_xml(...)` — import_DolbyVision_xml( (PyHDRNode)arg1, (str)file_name [, (str)mode='Include Frame Based Transitions Trims' [, (int)shot_idx=0]]) -> None :
- `mastering_display_ids(...)` — None( (flame.PyHDRNode)arg1) -> list
- `target_display_ids(...)` — None( (flame.PyHDRNode)arg1) -> list
- `mastering_display_info(...)` — None( (flame.PyHDRNode)arg1) -> object
- `target_display_info(...)` — None( (flame.PyHDRNode)arg1) -> object
- `has_trim(...)` — has_trim( (PyHDRNode)arg1, (int)target_display_id) -> bool :
- `l2_from_l8(...)` — l2_from_l8( (PyHDRNode)arg1) -> object :

### class [PyHDRTimelineFX](classes/PyHDRTimelineFX.md)

Object representing a HDR Timeline FX.

#### Methods
- `analysis_status(...)` — None( (flame.PyHDRTimelineFX)arg1) -> object
- `analyze(...)` — analyze( (PyHDRTimelineFX)arg1 [, (str)analyze_mode='Current Shot']) -> None :
- `keep_analysis(...)` — keep_analysis( (PyHDRTimelineFX)arg1) -> None :
- `reset_analysis(...)` — reset_analysis( (PyHDRTimelineFX)arg1) -> None :
- `interpolate_trims(...)` — interpolate_trims( (PyHDRTimelineFX)arg1, (str)arg2) -> None :
- `reset_trims(...)` — reset_trims( (PyHDRTimelineFX)arg1) -> None :
- `export_DolbyVision_xml(...)` — export_DolbyVision_xml( (PyHDRTimelineFX)arg1, (str)file_name [, (bool)shot_only=False [, (str)comment='']]) -> None :
- `import_DolbyVision_xml(...)` — import_DolbyVision_xml( (PyHDRTimelineFX)arg1, (str)file_name [, (str)mode='Include Frame Based Transitions Trims' [, (int)shot_idx=0]]) -> None :
- `mastering_display_ids(...)` — None( (flame.PyHDRTimelineFX)arg1) -> list
- `target_display_ids(...)` — None( (flame.PyHDRTimelineFX)arg1) -> list
- `mastering_display_info(...)` — None( (flame.PyHDRTimelineFX)arg1) -> object
- `target_display_info(...)` — None( (flame.PyHDRTimelineFX)arg1) -> object
- `has_trim(...)` — has_trim( (PyHDRTimelineFX)arg1, (int)target_display_id) -> bool :
- `l2_from_l8(...)` — l2_from_l8( (PyHDRTimelineFX)arg1) -> object :

### class [PyImageNode](classes/PyImageNode.md)

Class derived from PyActionFamilyNode. Represents an Image node object.

#### Methods
- `media_nodes(...)` — None( (flame.PyImageNode)arg1) -> list
- `add_media(...)` — add_media( (PyActionFamilyNode)arg1) -> object :

### class [PyLensDistortionNode](classes/PyLensDistortionNode.md)

Object representing a Lens Distortion node.

#### Methods
- `import_lens_distortion(...)` — import_lens_distortion( (PyLensDistortionNode)arg1, (str)filename) -> None :
- `calculate(...)` — calculate( (PyLensDistortionNode)arg1) -> None :

### class [PyLibrary](classes/PyLibrary.md)

Class derived from PyArchiveEntry. This class represents a Library.

#### Methods
- `children(...)` — None( (flame.PyLibrary)arg1) -> list
- `folders(...)` — None( (flame.PyLibrary)arg1) -> list
- `batch_iterations(...)` — None( (flame.PyLibrary)arg1) -> list
- `desktops(...)` — None( (flame.PyLibrary)arg1) -> list
- `reel_groups(...)` — None( (flame.PyLibrary)arg1) -> list
- `reels(...)` — None( (flame.PyLibrary)arg1) -> list
- `sequences(...)` — None( (flame.PyLibrary)arg1) -> list
- `clips(...)` — None( (flame.PyLibrary)arg1) -> list
- `batch_groups(...)` — None( (flame.PyLibrary)arg1) -> list
- `opened(...)` — None( (flame.PyLibrary)arg1) -> bool
- `open(...)` — open( (PyLibrary)arg1) -> bool :
- `close(...)` — close( (PyLibrary)arg1) -> bool :
- `clear(...)` — clear( (PyLibrary)arg1 [, (bool)confirm=True]) -> bool :
- `acquire_exclusive_access(...)` — acquire_exclusive_access( (PyLibrary)arg1) -> bool :
- `release_exclusive_access(...)` — release_exclusive_access( (PyLibrary)arg1) -> bool :
- `create_reel_group(...)` — create_reel_group( (PyLibrary)arg1, (str)name) -> object :
- `create_reel(...)` — create_reel( (PyLibrary)arg1, (str)name) -> object :
- `create_folder(...)` — create_folder( (PyLibrary)arg1, (str)name) -> object :
- `create_sequence(...)` — create_sequence( (PyLibrary)arg1 [, (str)name='Untitled Sequence' [, (int)video_tracks=1 [, (bool)video_stereo=False [, (object)width=None [, (object)height=None [, (object)ratio=None [, (object)bit_depth=None [, (object)scan_mode=None [, (object)frame_rate=None [, (object)start_at=00:00:00+00 [, (object)duration=00:00:00+01 [, (int)audio_tracks=1 [, (bool)audio_stereo=True]]]]]]]]]]]]]) -> object :

### class [PyMarker](classes/PyMarker.md)

Object representing a Marker.

#### Methods
- `has_annotations(...)` — None( (flame.PyMarker)arg1) -> bool
- `clear_annotations(...)` — clear_annotations( (PyMarker)arg1) -> None :
- `sync_connected_segments(...)` — sync_connected_segments( (PyMarker)arg1) -> None :

### class [PyMediaHub](classes/PyMediaHub.md)

This class represents the MediaHub.

#### Methods
- `files(...)` — None( (flame.PyMediaHub)arg1) -> flame.PyMediaHubFilesTab
- `archives(...)` — None( (flame.PyMediaHub)arg1) -> flame.PyMediaHubTab

### class [PyMediaHubFilesEntry](classes/PyMediaHubFilesEntry.md)

Object representing a clip in the MediaHub Files tabs

#### Methods
- `path(...)` — None( (flame.PyMediaHubFilesEntry)arg1) -> str

### class [PyMediaHubFilesFolder](classes/PyMediaHubFilesFolder.md)

Object representing a folder in the MediaHub Files tabs

#### Methods
- `path(...)` — None( (flame.PyMediaHubFilesFolder)arg1) -> str

### class [PyMediaHubFilesTab](classes/PyMediaHubFilesTab.md)

This class represents the MediaHub Files tab.

#### Methods
- `options(...)` — None( (flame.PyMediaHubFilesTab)arg1) -> flame.PyMediaHubFilesTabOptions

### class [PyMediaHubFilesTabOptions](classes/PyMediaHubFilesTabOptions.md)

This class represents the MediaHub Files tab options.

#### Methods
- `multi_channel_mode(...)` — None( (flame.PyMediaHubFilesTabOptions)arg1) -> str
- `sequence_mode(...)` — None( (flame.PyMediaHubFilesTabOptions)arg1) -> bool
- `cache_mode(...)` — None( (flame.PyMediaHubFilesTabOptions)arg1) -> bool
- `proxies_mode(...)` — None( (flame.PyMediaHubFilesTabOptions)arg1) -> bool
- `cache_and_proxies_all_versions(...)` — None( (flame.PyMediaHubFilesTabOptions)arg1) -> bool
- `resize_mode(...)` — None( (flame.PyMediaHubFilesTabOptions)arg1) -> str
- `resize_filter(...)` — None( (flame.PyMediaHubFilesTabOptions)arg1) -> str
- `resolution(...)` — None( (flame.PyMediaHubFilesTabOptions)arg1) -> str
- `width(...)` — None( (flame.PyMediaHubFilesTabOptions)arg1) -> object
- `height(...)` — None( (flame.PyMediaHubFilesTabOptions)arg1) -> object
- `scaling_presets_value(...)` — None( (flame.PyMediaHubFilesTabOptions)arg1) -> object
- `frame_ratio(...)` — None( (flame.PyMediaHubFilesTabOptions)arg1) -> object
- `bit_depth(...)` — None( (flame.PyMediaHubFilesTabOptions)arg1) -> object
- `scan_mode(...)` — None( (flame.PyMediaHubFilesTabOptions)arg1) -> str
- `pixel_ratio(...)` — None( (flame.PyMediaHubFilesTabOptions)arg1) -> object
- `colour_mgmt_mode(...)` — None( (flame.PyMediaHubFilesTabOptions)arg1) -> str
- `colour_mgmt_view(...)` — None( (flame.PyMediaHubFilesTabOptions)arg1) -> str
- `tagged_colour_space(...)` — None( (flame.PyMediaHubFilesTabOptions)arg1) -> str
- `colour_mgmt_display(...)` — None( (flame.PyMediaHubFilesTabOptions)arg1) -> str
- `colour_mgmt_working_space(...)` — None( (flame.PyMediaHubFilesTabOptions)arg1) -> str
- `colour_mgmt_invert(...)` — None( (flame.PyMediaHubFilesTabOptions)arg1) -> bool
- `import_transform(...)` — import_transform( (PyMediaHubFilesTabOptions)arg1, (str)file_path) -> None :
- `set_tagged_colour_space(...)` — set_tagged_colour_space( (PyMediaHubFilesTabOptions)arg1, (str)colour_space) -> None :

### class [PyMediaHubProjectsEntry](classes/PyMediaHubProjectsEntry.md)

Object representing a clip in the MediaHub Projects tabs

#### Methods
- `uid(...)` — None( (flame.PyMediaHubProjectsEntry)arg1) -> str
- `path(...)` — None( (flame.PyMediaHubProjectsEntry)arg1) -> str

### class [PyMediaHubProjectsFolder](classes/PyMediaHubProjectsFolder.md)

Object representing a folder in the MediaHub Projects tabs

#### Methods
- `uid(...)` — None( (flame.PyMediaHubProjectsFolder)arg1) -> str
- `path(...)` — None( (flame.PyMediaHubProjectsFolder)arg1) -> str

### class [PyMediaHubTab](classes/PyMediaHubTab.md)

This class represents a MediaHub tab.

#### Methods
- `get_path(...)` — get_path( (PyMediaHubTab)arg1) -> str :
- `set_path(...)` — set_path( (PyMediaHubTab)arg1, (str)arg2 [, (bool)allow_partial_success=False]) -> bool :

### class [PyMediaPanel](classes/PyMediaPanel.md)

This class represents the media panel.

#### Methods
- `selected_entries(...)` — None( (flame.PyMediaPanel)arg1) -> object
- `visible(...)` — None( (flame.PyMediaPanel)arg1) -> bool
- `full_height(...)` — None( (flame.PyMediaPanel)arg1) -> bool
- `full_width(...)` — None( (flame.PyMediaPanel)arg1) -> bool
- `dual(...)` — None( (flame.PyMediaPanel)arg1) -> bool
- `move(...)` — move( (PyMediaPanel)arg1, (object)source_entries, (object)destination [, (str)duplicate_action='add']) -> object :
- `copy(...)` — copy( (PyMediaPanel)arg1, (object)source_entries, (object)destination [, (str)duplicate_action='add']) -> object :

### class [PyMessages](classes/PyMessages.md)

Module handling message bar in application UI.

#### Methods
- `show_in_console(...)` — show_in_console( (PyMessages)arg1, (str)message [, (str)type='info' [, (int)duration=-1]]) -> None :
- `clear_console(...)` — clear_console( (PyMessages)arg1) -> None :
- `show_in_dialog(...)` — show_in_dialog( (PyMessages)arg1, (str)title, (str)message, (str)type, (list)buttons [, (str)cancel_button='']) -> str :

### class [PyMetadataNode](classes/PyMetadataNode.md)

Class derived from PyNode. This class represents a Metadata node.

#### Methods
- `set_metadata_value(...)` — set_metadata_value( (PyNode)arg1 [, (str)socket_name='Default' [, (str)key='' [, (object)value=None]]]) -> None :
- `set_metadata_discarded(...)` — set_metadata_discarded( (PyNode)arg1 [, (str)socket_name='Default' [, (str)key='' [, (bool)discarded=True]]]) -> None :
- `set_metadata_key(...)` — set_metadata_key( (PyNode)arg1 [, (str)socket_name='Default' [, (str)key='' [, (object)name=None]]]) -> None :
- `load_node_setup(...)` — load_node_setup( (PyMetadataNode)arg1, (str)file_name [, (bool)edited_keys=True [, (bool)discarded_keys=True [, (bool)added_keys=True [, (bool)replaced_keys=True [, (bool)update_tokens=True]]]]]) -> bool :

### class [PyMetadataTimelineFX](classes/PyMetadataTimelineFX.md)

Object representing a Metadata Timeline FX.

#### Methods
- `get_metadata(...)` — get_metadata( (PyMetadataTimelineFX)arg1 [, (str)key='' [, (int)frame=1]]) -> object :
- `set_metadata_value(...)` — set_metadata_value( (PyMetadataTimelineFX)arg1, (str)key [, (object)value=None]) -> None :
- `set_metadata_discarded(...)` — set_metadata_discarded( (PyMetadataTimelineFX)arg1 [, (str)key='' [, (bool)discarded=True]]) -> None :
- `set_metadata_key(...)` — set_metadata_key( (PyMetadataTimelineFX)arg1 [, (str)key='' [, (object)name=None]]) -> None :
- `load_setup(...)` — load_setup( (PyMetadataTimelineFX)arg1, (str)file_name [, (bool)edited_keys=True [, (bool)discarded_keys=True [, (bool)added_keys=True [, (bool)update_tokens=True]]]]) -> bool :

### class [PyMetadataValue](classes/PyMetadataValue.md)

This class holds the metadata of a specific data type.

#### Methods
- `get_value(...)` — get_value( (PyMetadataValue)arg1) -> object :
- `set_value(...)` — set_value( (PyMetadataValue)arg1, (object)value) -> None :
- `type(...)` — None( (flame.PyMetadataValue)arg1) -> str

### class [PyMorphNode](classes/PyMorphNode.md)

Object representing a Morph node.

#### Methods
- `set_mix_to_range(...)` — set_mix_to_range( (PyMorphNode)arg1) -> None :

### class [PyNode](classes/PyNode.md)

Object representing a Node.

#### Methods
- `sockets(...)` — None( (flame.PyNode)arg1) -> dict
- `input_sockets(...)` — None( (flame.PyNode)arg1) -> list
- `output_sockets(...)` — None( (flame.PyNode)arg1) -> list
- `load_node_setup(...)` — load_node_setup( (PyNode)arg1, (str)file_name) -> bool :
- `save_node_setup(...)` — save_node_setup( (PyNode)arg1, (str)file_name) -> bool :
- `delete(...)` — delete( (PyFlameObject)arg1 [, (bool)confirm=True]) -> bool :
- `duplicate(...)` — duplicate( (PyNode)arg1 [, (bool)keep_node_connections=False]) -> object :
- `set_context(...)` — set_context( (PyNode)arg1, (int)index [, (str)socket_name='Default']) -> bool :
- `clear_schematic_colour(...)` — clear_schematic_colour( (PyNode)arg1) -> None :
- `get_metadata(...)` — get_metadata( (PyNode)arg1 [, (str)socket_name='Default' [, (str)key='' [, (object)frame=None]]]) -> object :
- `cache_range(...)` — cache_range( (PyNode)arg1 [, (object)start=None [, (object)end=None]]) -> int :
- `output_channel_as_metadata_key(...)` — output_channel_as_metadata_key( (PyNode)arg1, (str)channel_name [, (bool)enable=True]) -> None :

### class [PyOFXNode](classes/PyOFXNode.md)

Object representing a OpenFX node.

#### Methods
- `change_plugin(...)` — change_plugin( (PyOFXNode)arg1, (str)plugin_name) -> bool :

### class [PyPaintNode](classes/PyPaintNode.md)

Object representing a Paint node.

#### Methods
- `add_source(...)` — add_source( (PyPaintNode)arg1) -> object :

### class [PyProject](classes/PyProject.md)

Object representing a Project.

#### Methods
- `name(...)` — None( (flame.PyProject)arg1) -> str
- `nickname(...)` — None( (flame.PyProject)arg1) -> str
- `description(...)` — None( (flame.PyProject)arg1) -> str
- `project_name(...)` — None( (flame.PyProject)arg1) -> str
- `workspaces_count(...)` — None( (flame.PyProject)arg1) -> int
- `current_workspace(...)` — None( (flame.PyProject)arg1) -> object
- `shared_libraries(...)` — None( (flame.PyProject)arg1) -> list
- `project_folder(...)` — None( (flame.PyProject)arg1) -> str
- `setups_folder(...)` — None( (flame.PyProject)arg1) -> str
- `media_folder(...)` — None( (flame.PyProject)arg1) -> str
- `create_shared_library(...)` — create_shared_library( (PyProject)arg1, (str)name) -> object :
- `refresh_shared_libraries(...)` — refresh_shared_libraries( (PyProject)arg1) -> bool :
- `reload_ocio_config(...)` — reload_ocio_config( (PyProject)arg1 [, (bool)reset_colour_policy=False]) -> bool :
- `export_ocio_config(...)` — export_ocio_config( (PyProject)arg1, (str)config_name [, (str)destination_folder='' [, (bool)overwrite_existing=False [, (bool)export_as_locked=False [, (bool)generate_ocioz=False]]]]) -> bool :
- `set_context_variable(...)` — set_context_variable( (PyProject)arg1, (str)name, (str)value) -> None :
- `get_context_variables(...)` — get_context_variables( (PyProject)arg1) -> dict :
- `reset_context_variables(...)` — reset_context_variables( (PyProject)arg1) -> None :

### class [PyProjectSelector](classes/PyProjectSelector.md)

Object representing the Project manager.

#### Methods
- `current_project(...)` — None( (flame.PyProjectSelector)arg1) -> object

### class [PyReadFileNode](classes/PyReadFileNode.md)

Class derived from PyNode. This class represents a ReadFile node.

### class [PyReel](classes/PyReel.md)

Object representing a Reel.

#### Methods
- `children(...)` — None( (flame.PyReel)arg1) -> list
- `sequences(...)` — None( (flame.PyReel)arg1) -> list
- `clips(...)` — None( (flame.PyReel)arg1) -> list
- `type(...)` — None( (flame.PyReel)arg1) -> object
- `clear(...)` — clear( (PyReel)arg1 [, (bool)confirm=True]) -> bool :
- `create_sequence(...)` — create_sequence( (PyReel)arg1 [, (str)name='Untitled Sequence' [, (int)video_tracks=1 [, (bool)video_stereo=False [, (object)width=None [, (object)height=None [, (object)ratio=None [, (object)bit_depth=None [, (object)scan_mode=None [, (object)frame_rate=None [, (object)start_at=00:00:00+00 [, (object)duration=00:00:00+01 [, (int)audio_tracks=1 [, (bool)audio_stereo=True]]]]]]]]]]]]]) -> object :
- `save(...)` — save( (PyReel)arg1) -> bool :

### class [PyReelGroup](classes/PyReelGroup.md)

Object representing a Reel Group.

#### Methods
- `children(...)` — None( (flame.PyReelGroup)arg1) -> list
- `reels(...)` — None( (flame.PyReelGroup)arg1) -> list
- `clear(...)` — clear( (PyReelGroup)arg1 [, (bool)confirm=True]) -> bool :
- `create_reel(...)` — create_reel( (PyReelGroup)arg1, (str)name [, (bool)sequence=False]) -> object :
- `save(...)` — save( (PyReelGroup)arg1) -> bool :

### class [PyRenderNode](classes/PyRenderNode.md)

Class derived from PyNode. This class represents a Render node.

#### Methods
- `channels(...)` — None( (flame.PyRenderNode)arg1) -> list
- `set_channel_name(...)` — set_channel_name( (PyRenderNode)arg1, (object)channel, (object)name) -> None :
- `set_metadata_value(...)` — set_metadata_value( (PyNode)arg1 [, (str)socket_name='Default' [, (str)key='' [, (object)value=None [, (bool)is_dynamic=False]]]]) -> None :
- `set_metadata_discarded(...)` — set_metadata_discarded( (PyNode)arg1 [, (str)socket_name='Default' [, (str)key='' [, (bool)discarded=True]]]) -> None :
- `set_metadata_key(...)` — set_metadata_key( (PyNode)arg1 [, (str)socket_name='Default' [, (str)key='' [, (object)name=None]]]) -> None :

### class [PyResolution](classes/PyResolution.md)

Object representing a resolution

#### Methods
- `resolution(...)` — None( (flame.PyResolution)arg1) -> str
- `width(...)` — None( (flame.PyResolution)arg1) -> int
- `height(...)` — None( (flame.PyResolution)arg1) -> int
- `frame_ratio(...)` — None( (flame.PyResolution)arg1) -> float
- `scan_mode(...)` — None( (flame.PyResolution)arg1) -> str
- `bit_depth(...)` — None( (flame.PyResolution)arg1) -> int

### class [PySearch](classes/PySearch.md)

This class represents the search.

#### Methods
- `use_weight(...)` — None( (flame.PySearch)arg1) -> bool
- `set_tool_favorite(...)` — set_tool_favorite( (PySearch)arg1, (str)arg2, (str)name, (bool)type) -> None :
- `set_tool_hidden(...)` — set_tool_hidden( (PySearch)arg1, (str)arg2, (str)name, (bool)type) -> None :
- `set_tool_weight(...)` — set_tool_weight( (PySearch)arg1, (str)arg2, (str)name, (int)type) -> None :
- `search_results(...)` — search_results( (PySearch)arg1 [, (str)search_str='*' [, (str)tab='Tools']]) -> list :
- `activate_search_result(...)` — activate_search_result( (PySearch)arg1, (str)name, (str)type [, (str)tab='Tools']) -> None :

### class [PySegment](classes/PySegment.md)

Object representing a Segment.

#### Methods
- `source_name(...)` — None( (flame.PySegment)arg1) -> str
- `source_in(...)` — None( (flame.PySegment)arg1) -> object
- `source_out(...)` — None( (flame.PySegment)arg1) -> object
- `source_duration(...)` — None( (flame.PySegment)arg1) -> object
- `source_width(...)` — None( (flame.PySegment)arg1) -> int
- `source_height(...)` — None( (flame.PySegment)arg1) -> int
- `source_bit_depth(...)` — None( (flame.PySegment)arg1) -> int
- `source_ratio(...)` — None( (flame.PySegment)arg1) -> float
- `source_scan_mode(...)` — None( (flame.PySegment)arg1) -> str
- `source_frame_rate(...)` — None( (flame.PySegment)arg1) -> str
- `source_cached(...)` — None( (flame.PySegment)arg1) -> str
- `source_has_history(...)` — None( (flame.PySegment)arg1) -> bool
- `source_unlinked(...)` — None( (flame.PySegment)arg1) -> str
- `source_sample_rate(...)` — None( (flame.PySegment)arg1) -> str
- `source_audio_track(...)` — None( (flame.PySegment)arg1) -> int
- `source_essence_uid(...)` — None( (flame.PySegment)arg1) -> str
- `source_uid(...)` — None( (flame.PySegment)arg1) -> str
- `original_source_uid(...)` — None( (flame.PySegment)arg1) -> str
- `source_colour_primaries(...)` — None( (flame.PySegment)arg1) -> int
- `source_transfer_characteristics(...)` — None( (flame.PySegment)arg1) -> int
- `source_matrix_coefficients(...)` — None( (flame.PySegment)arg1) -> int
- `tape_name(...)` — None( (flame.PySegment)arg1) -> str
- `record_in(...)` — None( (flame.PySegment)arg1) -> object
- `record_out(...)` — None( (flame.PySegment)arg1) -> object
- `record_duration(...)` — None( (flame.PySegment)arg1) -> object
- `start_frame(...)` — None( (flame.PySegment)arg1) -> int
- `file_path(...)` — None( (flame.PySegment)arg1) -> str
- `markers(...)` — None( (flame.PySegment)arg1) -> list
- `effect_types(...)` — None( (flame.PySegment)arg1) -> list
- `effects(...)` — None( (flame.PySegment)arg1) -> list
- `groups(...)` — None( (flame.PySegment)arg1) -> list
- `type(...)` — None( (flame.PySegment)arg1) -> str
- `head(...)` — None( (flame.PySegment)arg1) -> object
- `tail(...)` — None( (flame.PySegment)arg1) -> object
- `rgb_channel(...)` — None( (flame.PySegment)arg1) -> str
- `matte_channel(...)` — None( (flame.PySegment)arg1) -> str
- `rgb_channels(...)` — None( (flame.PySegment)arg1) -> list
- `matte_channels(...)` — None( (flame.PySegment)arg1) -> list
- `version_uid(...)` — None( (flame.PySegment)arg1) -> str
- `version_uids(...)` — None( (flame.PySegment)arg1) -> list
- `matte_mode(...)` — None( (flame.PySegment)arg1) -> str
- `container_clip(...)` — None( (flame.PySegment)arg1) -> object
- `create_effect(...)` — create_effect( (PySegment)arg1, (str)effect_type [, (str)after_effect_type='']) -> object :
- `create_marker(...)` — create_marker( (PySegment)arg1, (object)location) -> object :
- `create_connection(...)` — create_connection( (PySegment)arg1) -> None :
- `remove_connection(...)` — remove_connection( (PySegment)arg1) -> None :
- `sync_connected_segments(...)` — sync_connected_segments( (PySegment)arg1) -> None :
- `connected_segments(...)` — connected_segments( (PySegment)arg1 [, (str)scoping='all reels']) -> object :
- `duplicate_source(...)` — duplicate_source( (PySegment)arg1) -> None :
- `shared_source_segments(...)` — shared_source_segments( (PySegment)arg1) -> object :
- `copy_to_media_panel(...)` — copy_to_media_panel( (PySegment)arg1, (PyArchiveEntry)destination [, (str)duplicate_action='add']) -> object :
- `trim_head(...)` — trim_head( (PySegment)arg1, (int)offset [, (bool)ripple=False [, (bool)sync=False [, (str)keyframes_move_mode='Shift']]]) -> bool :
- `trim_tail(...)` — trim_tail( (PySegment)arg1, (int)offset [, (bool)ripple=False [, (bool)sync=False [, (str)keyframes_move_mode='Shift']]]) -> bool :
- `slip(...)` — slip( (PySegment)arg1, (int)offset [, (bool)sync=False [, (str)keyframes_move_mode='Shift']]) -> bool :
- `slide_keyframes(...)` — slide_keyframes( (PySegment)arg1, (int)offset [, (bool)sync=False]) -> bool :
- `set_gap_colour(...)` — set_gap_colour( (PySegment)arg1 [, (float)r=0.0 [, (float)g=0.0 [, (float)b=0.0]]]) -> None :
- `set_gap_bars(...)` — set_gap_bars( (PySegment)arg1 [, (str)type='smpte' [, (bool)full_luminance=False [, (float)softness=0.0]]]) -> object :
- `smart_replace(...)` — smart_replace( (PySegment)arg1, (PyClip)source_clip) -> None :
- `smart_replace_media(...)` — smart_replace_media( (PySegment)arg1, (PyClip)source_clip) -> None :
- `match(...)` — match( (PySegment)arg1, (PyArchiveEntry)destination [, (bool)preserve_handle=False [, (bool)use_sequence_info=True [, (bool)include_nested_content=False [, (bool)include_timeline_fx=False]]]]) -> object :
- `clear_colour(...)` — clear_colour( (PySegment)arg1) -> None :
- `set_rgb_channel(...)` — set_rgb_channel( (PySegment)arg1 [, (str)channel_name='' [, (int)channel_index=-1 [, (str)scope='Follow Preferences']]]) -> bool :
- `set_matte_channel(...)` — set_matte_channel( (PySegment)arg1 [, (str)channel_name='' [, (int)channel_index=-1 [, (str)scope='Follow Preferences' [, (str)matte_mode='Custom Matte']]]]) -> bool :
- `set_version_uid(...)` — set_version_uid( (PySegment)arg1, (str)version_uid [, (str)scope='Follow Source Sharing']) -> bool :
- `get_colour_space(...)` — get_colour_space( (PySegment)arg1 [, (PyTime)time=None]) -> str :
- `create_unlinked_segment(...)` — create_unlinked_segment( (PySegment)arg1 [, (str)source_name='' [, (str)tape_name='' [, (object)start_time=0 [, (object)source_duration=0 [, (object)head=0 [, (str)file_path='' [, (int)source_audio_track=1 [, (int)width=0 [, (int)height=0 [, (float)ratio=0.0 [, (int)bit_depth=0 [, (str)scan_mode='Same As Sequence' [, (str)frame_rate='Same As Sequence' [, (object)timewarp_speed=None]]]]]]]]]]]]]]) -> None :
- `change_start_frame(...)` — change_start_frame( (PySegment)arg1, (int)start_frame [, (bool)use_segment_connections=True]) -> None :
- `get_metadata(...)` — get_metadata( (PySegment)arg1 [, (str)key='' [, (PyTime)time=None]]) -> object :

### class [PySequence](classes/PySequence.md)

Object representing a Sequence.

#### Methods
- `open(...)` — open( (PySequence)arg1) -> bool :
- `create_container(...)` — create_container( (PySequence)arg1) -> object :
- `create_version(...)` — create_version( (PySequence)arg1 [, (bool)stereo=False]) -> object :
- `create_audio(...)` — create_audio( (PySequence)arg1 [, (bool)stereo=False]) -> object :
- `create_subtitle(...)` — create_subtitle( (PySequence)arg1) -> object :
- `import_subtitles_file(...)` — import_subtitles_file( (PySequence)arg1, (str)file_name [, (object)file_type=None [, (bool)align_first_event_to_clip_start=False [, (object)convert_from_frame_rate=None]]]) -> object :
- `create_group(...)` — create_group( (PySequence)arg1, (str)name) -> object :
- `insert(...)` — insert( (PySequence)arg1, (PyClip)source_clip [, (PyTime)insert_time=None [, (PyTrack)destination_track=None]]) -> bool :
- `overwrite(...)` — overwrite( (PySequence)arg1, (PyClip)source_clip [, (PyTime)overwrite_time=None [, (PyTrack)destination_track=None]]) -> bool :
- `copy_selection_to_media_panel(...)` — copy_selection_to_media_panel( (PySequence)arg1, (PyArchiveEntry)destination [, (str)duplicate_action='add']) -> object :
- `extract_selection_to_media_panel(...)` — extract_selection_to_media_panel( (PySequence)arg1 [, (PyArchiveEntry)destination=None [, (str)duplicate_action='add']]) -> object :
- `lift_selection_to_media_panel(...)` — lift_selection_to_media_panel( (PySequence)arg1 [, (PyArchiveEntry)destination=None [, (str)duplicate_action='add']]) -> object :
- `groups(...)` — None( (flame.PySequence)arg1) -> list

### class [PySequenceGroup](classes/PySequenceGroup.md)

Object representing a Group in a Sequence.

#### Methods
- `segments(...)` — None( (flame.PySequenceGroup)arg1) -> list
- `add(...)` — add( (PySequenceGroup)arg1, (object)segments) -> None :
- `remove(...)` — remove( (PySequenceGroup)arg1, (object)segments) -> None :

### class [PySubtitleTrack](classes/PySubtitleTrack.md)

Object representing a Subtitle Track.

#### Methods
- `export_as_srt_file(...)` — export_as_srt_file( (PySubtitleTrack)arg1, (str)file_name [, (bool)character_based_attributes=True [, (bool)export_colours=False [, (str)exclude_colour='' [, (bool)use_original_colours=False [, (bool)use_original_alignment=False [, (bool)export_alignments=False [, (str)alignment_type='an' [, (str)exclude_alignment='' [, (str)start_timecode='Same as Clip']]]]]]]]]) -> None :

### class [PyTime](classes/PyTime.md)

Object representing a time unit

#### Methods
- `frame(...)` — None( (flame.PyTime)arg1) -> int
- `relative_frame(...)` — None( (flame.PyTime)arg1) -> int
- `timecode(...)` — None( (flame.PyTime)arg1) -> str
- `frame_rate(...)` — None( (flame.PyTime)arg1) -> object

### class [PyTimeline](classes/PyTimeline.md)

This class represents the Timeline.

#### Methods
- `clip(...)` — None( (flame.PyTimeline)arg1) -> object
- `current_segment(...)` — None( (flame.PyTimeline)arg1) -> object
- `current_marker(...)` — None( (flame.PyTimeline)arg1) -> object
- `current_effect(...)` — None( (flame.PyTimeline)arg1) -> object
- `current_transition(...)` — None( (flame.PyTimeline)arg1) -> object
- `type(...)` — None( (flame.PyTimeline)arg1) -> str

### class [PyTimelineFX](classes/PyTimelineFX.md)

Object representing a Timeline FX.

#### Methods
- `type(...)` — None( (flame.PyTimelineFX)arg1) -> object
- `has_maps_cache_media(...)` — None( (flame.PyTimelineFX)arg1) -> bool
- `load_setup(...)` — load_setup( (PyTimelineFX)arg1, (str)file_name) -> bool :
- `save_setup(...)` — save_setup( (PyTimelineFX)arg1, (str)file_name) -> bool :
- `flush_maps_cache_media(...)` — flush_maps_cache_media( (PyTimelineFX)arg1) -> bool :
- `clear_maps_cache_media(...)` — clear_maps_cache_media( (PyTimelineFX)arg1) -> bool :
- `sync_connected_segments(...)` — sync_connected_segments( (PyTimelineFX)arg1) -> None :
- `slide_keyframes(...)` — slide_keyframes( (PyTimelineFX)arg1, (float)offset) -> None :
- `output_channel_as_metadata_key(...)` — output_channel_as_metadata_key( (PyTimelineFX)arg1, (str)channel_name [, (bool)enable=True]) -> None :

### class [PyTimewarpNode](classes/PyTimewarpNode.md)

Object representing a Timewarp node.

#### Methods
- `get_speed(...)` — get_speed( (PyTimewarpNode)arg1, (float)frame) -> float :
- `set_speed(...)` — set_speed( (PyTimewarpNode)arg1, (float)frame, (float)new_speed) -> None :
- `set_timing(...)` — set_timing( (PyTimewarpNode)arg1, (float)frame, (float)new_timing) -> None :
- `get_timing(...)` — get_timing( (PyTimewarpNode)arg1, (float)frame) -> float :
- `get_duration_timing(...)` — get_duration_timing( (PyTimewarpNode)arg1, (float)frame) -> float :
- `get_speed_timing(...)` — get_speed_timing( (PyTimewarpNode)arg1, (float)frame) -> float :

### class [PyTimewarpTimelineFX](classes/PyTimewarpTimelineFX.md)

Object representing a Timewarp node.

#### Methods
- `get_speed(...)` — get_speed( (PyTimewarpTimelineFX)arg1, (float)frame) -> float :
- `set_speed(...)` — set_speed( (PyTimewarpTimelineFX)arg1, (float)frame, (float)new_speed) -> None :
- `set_timing(...)` — set_timing( (PyTimewarpTimelineFX)arg1, (float)frame, (float)new_timing) -> None :
- `get_timing(...)` — get_timing( (PyTimewarpTimelineFX)arg1, (float)frame) -> float :
- `get_duration_timing(...)` — get_duration_timing( (PyTimewarpTimelineFX)arg1, (float)frame) -> float :
- `get_speed_timing(...)` — get_speed_timing( (PyTimewarpTimelineFX)arg1, (float)frame) -> float :

### class [PyTrack](classes/PyTrack.md)

Object representing a Track.

#### Methods
- `segments(...)` — None( (flame.PyTrack)arg1) -> list
- `transitions(...)` — None( (flame.PyTrack)arg1) -> list
- `copy_to_media_panel(...)` — copy_to_media_panel( (PyTrack)arg1, (PyArchiveEntry)destination [, (str)duplicate_action='add']) -> object :
- `cut(...)` — cut( (PyTrack)arg1, (PyTime)cut_time [, (bool)sync=False]) -> None :
- `insert_transition(...)` — insert_transition( (PyTrack)arg1, (PyTime)record_time, (str)type [, (int)duration=10 [, (str)alignment='Centred' [, (int)in_offset=0 [, (bool)sync=False]]]]) -> object :

### class [PyTransition](classes/PyTransition.md)

Object representing a Transition.

#### Methods
- `type(...)` — None( (flame.PyTransition)arg1) -> str
- `record_time(...)` — None( (flame.PyTransition)arg1) -> object
- `in_offset(...)` — None( (flame.PyTransition)arg1) -> int
- `set_transition(...)` — set_transition( (PyTransition)arg1, (str)type [, (int)duration=10 [, (str)alignment='Centred' [, (int)in_offset=0]]]) -> object :
- `slide(...)` — slide( (PyTransition)arg1, (int)offset [, (bool)sync=False]) -> bool :
- `set_dissolve_to_from_colour(...)` — set_dissolve_to_from_colour( (PyTransition)arg1 [, (float)r=0.0 [, (float)g=0.0 [, (float)b=0.0]]]) -> None :
- `set_fade_to_from_silence(...)` — set_fade_to_from_silence( (PyTransition)arg1) -> None :

### class [PyTypeFX](classes/PyTypeFX.md)

Object representing a Type Timeline FX.

#### Methods
- `layers(...)` — None( (flame.PyTypeFX)arg1) -> list
- `add_layer(...)` — add_layer( (PyTypeFX)arg1 [, (str)layer_type='Centre']) -> object :
- `append_type_setup(...)` — append_type_setup( (PyTypeFX)arg1, (str)file_name) -> bool :

### class [PyTypeLayer](classes/PyTypeLayer.md)

Object representing a Type Layer.

#### Methods
- `type(...)` — None( (flame.PyTypeLayer)arg1) -> object

### class [PyTypeNode](classes/PyTypeNode.md)

Object representing a Type node.

#### Methods
- `layers(...)` — None( (flame.PyTypeNode)arg1) -> list
- `add_layer(...)` — add_layer( (PyTypeNode)arg1 [, (str)layer_type='Centre']) -> object :
- `append_type_setup(...)` — append_type_setup( (PyTypeNode)arg1, (str)file_name) -> bool :

### class [PyUser](classes/PyUser.md)

Object representing a User.

#### Methods
- `name(...)` — None( (flame.PyUser)arg1) -> str
- `nickname(...)` — None( (flame.PyUser)arg1) -> str
- `shortcuts_profile(...)` — None( (flame.PyUser)arg1) -> str

### class [PyUsers](classes/PyUsers.md)

Object representing the User manager.

#### Methods
- `current_user(...)` — None( (flame.PyUsers)arg1) -> object

### class [PyVersion](classes/PyVersion.md)

Object representing a Version.

#### Methods
- `tracks(...)` — None( (flame.PyVersion)arg1) -> list
- `stereo(...)` — None( (flame.PyVersion)arg1) -> bool
- `copy_to_media_panel(...)` — copy_to_media_panel( (PyVersion)arg1, (PyArchiveEntry)destination [, (str)duplicate_action='add']) -> object :
- `create_track(...)` — create_track( (PyVersion)arg1 [, (int)track_index=-1 [, (bool)hdr=False]]) -> object :
- `import_DolbyVision_xml(...)` — import_DolbyVision_xml( (PyVersion)arg1, (str)file_name [, (str)mode='Include Frame Based Transitions Trims' [, (int)track_index=-1]]) -> object :

### class [PyWorkspace](classes/PyWorkspace.md)

Object representing a Workspace.

#### Methods
- `desktop(...)` — None( (flame.PyWorkspace)arg1) -> object
- `libraries(...)` — None( (flame.PyWorkspace)arg1) -> list
- `create_library(...)` — create_library( (PyWorkspace)arg1, (str)name) -> object :
- `replace_desktop(...)` — replace_desktop( (PyWorkspace)arg1, (PyDesktop)desktop) -> bool :
- `set_desktop_reels(...)` — set_desktop_reels( (PyWorkspace)arg1 [, (object)group=None]) -> bool :
- `set_freeform(...)` — set_freeform( (PyWorkspace)arg1 [, (object)reel=None]) -> bool :

### class [PyWriteFileNode](classes/PyWriteFileNode.md)

Class derived from PyRenderNode. This class represents a WriteFile node.

#### Methods
- `get_resolved_media_path(...)` — get_resolved_media_path( (PyWriteFileNode)arg1 [, (bool)show_extension=True [, (bool)translate_path=True [, (object)frame=None]]]) -> object :

## Functions
- [clear_graphics_memory](functions/clear_graphics_memory.md) — `clear_graphics_memory(...)` — clear_graphics_memory() -> None : 
- [clear_unreferenced_cache](functions/clear_unreferenced_cache.md) — `clear_unreferenced_cache(...)` — clear_unreferenced_cache([  (bool)all_projects=False]) -> None : 
- [delete](functions/delete.md) — `delete(...)` — delete( (PyFlameObject)object [, (bool)confirm=True]) -> bool : 
- [duplicate](functions/duplicate.md) — `duplicate(...)` — duplicate( (PyFlameObject)object [, (bool)keep_node_connections=False]) -> object : 
- [duplicate_many](functions/duplicate_many.md) — `duplicate_many(...)` — duplicate_many( (list)object_list [, (bool)keep_node_connections=False]) -> list : 
- [execute_command](functions/execute_command.md) — `execute_command(...)` — execute_command( (str)command [, (bool)blocking=True [, (bool)shell=False [, (bool)capture_stdout=False [, (bool)capture_stderr=False]]]]) -> tuple : 
- [execute_shortcut](functions/execute_shortcut.md) — `execute_shortcut(...)` — execute_shortcut( (str)description [, (bool)update_list=True]) -> bool : 
- [exit](functions/exit.md) — `exit(...)` — exit() -> None : 
- [find_by_name](functions/find_by_name.md) — `find_by_name(...)` — find_by_name( (str)name [, (object)parent=None]) -> list : 
- [find_by_uid](functions/find_by_uid.md) — `find_by_uid(...)` — find_by_uid( (str)uid) -> object : 
- [find_by_wiretap_node_id](functions/find_by_wiretap_node_id.md) — `find_by_wiretap_node_id(...)` — find_by_wiretap_node_id( (str)node_id) -> object : 
- [flush_graphics_memory](functions/flush_graphics_memory.md) — `flush_graphics_memory(...)` — flush_graphics_memory() -> None : 
- [get_current_tab](functions/get_current_tab.md) — `get_current_tab(...)` — get_current_tab() -> str : 
- [get_home_directory](functions/get_home_directory.md) — `get_home_directory(...)` — get_home_directory() -> str : 
- [get_init_cfg_path](functions/get_init_cfg_path.md) — `get_init_cfg_path(...)` — get_init_cfg_path() -> str : 
- [get_version](functions/get_version.md) — `get_version(...)` — get_version() -> str : 
- [get_version_major](functions/get_version_major.md) — `get_version_major(...)` — get_version_major() -> str : 
- [get_version_minor](functions/get_version_minor.md) — `get_version_minor(...)` — get_version_minor() -> str : 
- [get_version_patch](functions/get_version_patch.md) — `get_version_patch(...)` — get_version_patch() -> str : 
- [get_version_stamp](functions/get_version_stamp.md) — `get_version_stamp(...)` — get_version_stamp() -> str : 
- [go_to](functions/go_to.md) — `go_to(...)` — go_to( (str)tab) -> bool : 
- [import_clips](functions/import_clips.md) — `import_clips(...)` — import_clips( (object)path [, (object)destination=None]) -> list : 
- [schedule_idle_event](functions/schedule_idle_event.md) — `schedule_idle_event(...)` — schedule_idle_event( (object)function [, (int)delay=0]) -> None : 
- [set_current_tab](functions/set_current_tab.md) — `set_current_tab(...)` — set_current_tab( (str)arg1) -> bool : 
- [set_render_option](functions/set_render_option.md) — `set_render_option(...)` — set_render_option( (str)render_option [, (str)render_context='']) -> bool : 

## Constants / Attributes
- [batch](constants/batch.md)
- [browser](constants/browser.md)
- [media_panel](constants/media_panel.md)
- [mediahub](constants/mediahub.md)
- [messages](constants/messages.md)
- [project](constants/project.md)
- [projects](constants/projects.md)
- [timeline](constants/timeline.md)
- [users](constants/users.md)

