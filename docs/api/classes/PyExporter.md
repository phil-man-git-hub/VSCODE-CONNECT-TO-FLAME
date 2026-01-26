# Class: PyExporter

**Module**: `flame`

**Inherits from**: instance, object

## Description
Object holding export settings.


## Properties
| Name | Description |
| --- | --- |
| `Audio` |  |
| `Autodesk` |  |
| `Distribution_Package` |  |
| `Flow_Production_Tracking` |  |
| `Image_Sequence` |  |
| `Movie` |  |
| `Project` |  |
| `Sequence_Publish` |  |
| `Shared` |  |
| `Shotgun` |  |
| `User` |  |
| `export_all_subtitles` | Set export option 'All Subtitles Tracks'. |
| `export_between_marks` | Set export option 'Export between marks'. |
| `export_subtitles_as_files` | Set subtitles export option 'Export As Files. |
| `foreground` | Set export option 'Foreground export'. |
| `include_subtitles` | Set export option 'Include Subtitles'. |
| `keep_timeline_fx_renders` | Set export option 'Keep Timeline FX Renders'. |
| `use_top_video_track` | Set export option 'Use top video track'. |
| `warn_on_mixed_colour_space` | Set export option 'Warn on mixed colour space'. |
| `warn_on_no_media` | Set export option 'Warn on no media'. |
| `warn_on_pending_render` | Set export option 'Warn on pending render'. |
| `warn_on_reimport_unsupported` | Set export option 'Warn on reimport unsupported'. |
| `warn_on_unlinked` | Set export option 'Warn on unlinked'. |
| `warn_on_unrendered` | Set export option 'Warn on unrendered'. |


## Methods
### `BackgroundJobSettings`
```python
BackgroundJobSettings
```
Object holding background export job settings. These settings refer to the Backburner job, server and manager.

---

### `PresetType`
```python
PresetType
```
---

### `PresetVisibility`
```python
PresetVisibility
```
---

### `export`
```python
export
```


export( (PyExporter)arg1, (object)sources, (str)preset_path, (str)output_directory [, (PyExporter.BackgroundJobSettings)background_job_settings=None [, (object)hooks=None [, (object)hooks_user_data=None]]]) -> None :

    Perform export.

    Keyword arguments:

    sources -- Flame clip object, a Flame container object or a list of either first. If a container is passed, a multi-export will be done and structure will be respected as much as possible.

    preset_path -- Absolute path to the export preset to use.

    output_directory -- Absolute path to the output directory root.

    background_job_settings -- Settings of background job(s) created if any.

    hooks -- Export python hooks override. If passed, regular export python hooks implemented in exportHooks.py will be bypassed for this export and methods in the passed object with matching name will be called.

        Instance of object passed should implement the following signature:

    

            class PythonHookOverride(object):

                def preExport(self, info, userData, *args, **kwargs)

                    pass

    

                def postExport(self, info, userData, *args, **kwargs):

                    pass

    

                def preExportSequence(self, info, userData, *args, **kwargs):

                    pass

    

                def postExportSequence(self, info, userData, *args, **kwargs):

                    pass

    

                def preExportAsset(self, info, userData, *args, **kwargs):

                    pass

    

                def postExportAsset(self, info, userData, *args, **kwargs):

                    pass

    

                def exportOverwriteFile(self, path, *args, **kwargs):

                    return "ask" # or "overwrite"

    

    hooks_user_data -- User data object passed to the export python hooks. This object can be modified by the PythonHookOverride methods but cannot be re-assigned

---

### `get_presets_base_dir`
```python
get_presets_base_dir
```


get_presets_base_dir( (PyExporter.PresetVisibility)preset_visibility) -> str :

    Get a presets base directory.

---

### `get_presets_dir`
```python
get_presets_dir
```


get_presets_dir( (PyExporter.PresetVisibility)preset_visibility, (PyExporter.PresetType)preset_type) -> str :

    Get a presets directory.

---
