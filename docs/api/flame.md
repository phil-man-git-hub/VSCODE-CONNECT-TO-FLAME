# Module: flame

## Classes
### class PyActionFamilyNode

Class derived from PyNode. Represents an Action Family node object.

### class PyActionNode

Class derived from PyActionFamilyNode. Represents an Action node object.

### class PyArchiveEntry

Class derived from PyFlameObject. Base class for any object displayed in the Media Panel.

### class PyAttribute

### class PyAudioTrack

Object representing an Audio Track.

### class PyBatch

Class derived from PyFlameObject. This class represents a Batch Group.

### class PyBatchIteration

Class derived from PyArchiveEntry. This class represents a Batch Iteration.

### class PyBrowser

This class represents the file browser.

### class PyClip

CLass derived from PyArchiveEntry. This class represents a Clip.

### class PyClipNode

Class derived from PyNode. This class represents a Clip node.

### class PyClrMgmtNode

Object representing a Colour Mgmt node.

### class PyCoCameraAnalysis

Class derived from PyCoNode. This class represents the camera analysis node in the Action schematic.

### class PyCoCompass

Class derived from PyCoNode. This class represents the compass node in the Action schematic.

### class PyCoNode

Class derived from PyFlameObject. This class represents an Action node in the Action schematic.

### class PyColourMgtTimelineFX

Object representing a Colour Mgmt Timeline FX.

### class PyCompassNode

Class derived from PyNode. This class represents a Compass node.

### class PyDesktop

Class derived from PyArchiveEntry. This class represents a Desktop.

### class PyExporter

Object holding export settings.

### class PyFlameObject

The basic type of all accessible Flame objects from the python API.

### class PyFolder

Class derived from PyArchiveEntry. This class represents a Folder.

### class PyGMaskTracerNode

Class derived from PyActionFamilyNode. Represents a GMask Tracer node object.

### class PyHDRNode

Object representing a HDR node.

### class PyHDRTimelineFX

Object representing a HDR Timeline FX.

### class PyImageNode

Class derived from PyActionFamilyNode. Represents an Image node object.

### class PyLensDistortionNode

Object representing a Lens Distortion node.

### class PyLibrary

Class derived from PyArchiveEntry. This class represents a Library.

### class PyMarker

Object representing a Marker.

### class PyMediaHub

This class represents the MediaHub.

### class PyMediaHubFilesEntry

Object representing a clip in the MediaHub Files tabs

### class PyMediaHubFilesFolder

Object representing a folder in the MediaHub Files tabs

### class PyMediaHubFilesTab

This class represents the MediaHub Files tab.

### class PyMediaHubFilesTabOptions

This class represents the MediaHub Files tab options.

### class PyMediaHubProjectsEntry

Object representing a clip in the MediaHub Projects tabs

### class PyMediaHubProjectsFolder

Object representing a folder in the MediaHub Projects tabs

### class PyMediaHubTab

This class represents a MediaHub tab.

### class PyMediaPanel

This class represents the media panel.

### class PyMessages

Module handling message bar in application UI.

### class PyMetadataNode

Class derived from PyNode. This class represents a Metadata node.

### class PyMetadataTimelineFX

Object representing a Metadata Timeline FX.

### class PyMetadataValue

This class holds the metadata of a specific data type.

### class PyMorphNode

Object representing a Morph node.

### class PyNode

Object representing a Node.

### class PyOFXNode

Object representing a OpenFX node.

### class PyPaintNode

Object representing a Paint node.

### class PyProject

Object representing a Project.

### class PyProjectSelector

Object representing the Project manager.

### class PyReadFileNode

Class derived from PyNode. This class represents a ReadFile node.

### class PyReel

Object representing a Reel.

### class PyReelGroup

Object representing a Reel Group.

### class PyRenderNode

Class derived from PyNode. This class represents a Render node.

### class PyResolution

Object representing a resolution

PyResolution()
PyResolution(width, height, bit_depth, frame_ratio, scan_format)

### class PySearch

This class represents the search.

### class PySegment

Object representing a Segment.

### class PySequence

Object representing a Sequence.

### class PySequenceGroup

Object representing a Group in a Sequence.

### class PySubtitleTrack

Object representing a Subtitle Track.

### class PyTime

Object representing a time unit

PyTime(timecode, frame_rate)
PyTime(relative_frame)
PyTime(absolute_frame, frame_rate)

### class PyTimeline

This class represents the Timeline.

### class PyTimelineFX

Object representing a Timeline FX.

### class PyTimewarpNode

Object representing a Timewarp node.

### class PyTimewarpTimelineFX

Object representing a Timewarp node.

### class PyTrack

Object representing a Track.

### class PyTransition

Object representing a Transition.

### class PyTypeFX

Object representing a Type Timeline FX.

### class PyTypeLayer

Object representing a Type Layer.

### class PyTypeNode

Object representing a Type node.

### class PyUser

Object representing a User.

### class PyUsers

Object representing the User manager.

### class PyVersion

Object representing a Version.

### class PyWorkspace

Object representing a Workspace.

### class PyWriteFileNode

Class derived from PyRenderNode. This class represents a WriteFile node.

## Constants / Attributes
batch, browser, clear_graphics_memory, clear_unreferenced_cache, delete, duplicate, duplicate_many, execute_command, execute_shortcut, exit, find_by_name, find_by_uid, find_by_wiretap_node_id, flush_graphics_memory, get_current_tab, get_home_directory, get_init_cfg_path, get_version, get_version_major, get_version_minor, get_version_patch, get_version_stamp, go_to, import_clips, media_panel, mediahub, messages, project, projects, schedule_idle_event, set_current_tab, set_render_option, timeline, users
