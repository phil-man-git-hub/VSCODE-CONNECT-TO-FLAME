# Defines for the flame Module

Defines can be set for objects supported in the Python API. These shortcuts allow quick access to commonly used objects within the current context.

**Source:** Autodesk Flame Family 2026 Help | Defines for the flame Module

> **Note:** `flame.project` was changed to `flame.projects` in the 2020.1 Update version. Both syntaxes are supported, but `flame.projects` is preferred.

## Global Objects

| Object | Define |
|---|---|
| **PyProject** | `flame.projects.current_project` |
| **PyWorkspace** | `flame.projects.current_project.current_workspace`<br>OR<br>`PyProject.current_workspace` |
| **PyDesktop** | `flame.projects.current_project.current_workspace.desktop`<br>OR<br>`PyWorkspace.desktop` |
| **PyBatch** | `flame.projects.current_project.current_workspace.desktop.batch_groups[#]`<br>OR<br>`flame.batch` (current batch) |

## Batch Elements

| Object | Define |
|---|---|
| **PyNode** | `flame.batch.nodes[#]`<br>`flame.batch.current_node`<br>`flame.batch.get_node("name")`<br>`flame.batch.create_node("type")` |
| **PyBatchIteration** | `flame.batch.batch_iterations[#]` |

## Media Hierarchy

| Object | Define |
|---|---|
| **PyReelGroup** | `flame.projects.current_project.libraries[#].reel_groups[#]`<br>`flame.projects.current_project.current_workspace.desktop.reel_groups[#]` |
| **PyReel** | `flame.projects.current_project.current_workspace.libraries[#].reel_groups[#].reels[#]`<br>`flame.projects.current_project.current_workspace.desktop.reel_groups[#].reels[#]` |
| **PyLibrary** | `flame.projects.current_project.current_workspace.libraries[#]` |
| **PyFolder** | `flame.projects.current_project.current_workspace.libraries[#].folders[#]` |
| **PyClip** | `flame.projects.current_project.current_workspace.libraries[#].clips[#]`<br>`flame.projects.current_project.current_workspace.desktop.reel_groups[#].reels[#].clips[#]` |
| **PySequence** | `flame.projects.current_project.current_workspace.libraries[#].sequences[#]`<br>`flame.projects.current_project.current_workspace.desktop.reel_groups[#].reels[#].sequences[#]` |

## Sequence Structure

| Object | Define |
|---|---|
| **PyVersion** | `PySequence.versions[#]` |
| **PyTrack** | `PyReel.sequences[#].versions[#].tracks[#]` |
| **PySegment** | `PyReel.sequences[#].versions[#].tracks[#].segments[#]` |
| **PyTimelineFX** | `PyReel.sequences[#].versions[#].tracks[#].segments[#].effects[#]` |
| **PyMarker** | `PyReel.sequences[#].versions[#].tracks[#].segments[#].markers[#]`<br>`PyReel.sequences[#].markers[#]` |
| **PyAudioTrack** | `PyReel.sequences[#].audio_tracks[#]` |
