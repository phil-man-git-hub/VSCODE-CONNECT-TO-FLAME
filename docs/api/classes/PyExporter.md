# Class: PyExporter

**Module**: `flame`

Object holding export settings.

## Methods
### Properties
- `use_top_video_track(...)` — None( (flame.PyExporter)arg1) -> bool 
None( (flame.PyExporter)arg1) -> bool

- `export_between_marks(...)` — None( (flame.PyExporter)arg1) -> bool 
None( (flame.PyExporter)arg1) -> bool

- `foreground(...)` — None( (flame.PyExporter)arg1) -> bool 
None( (flame.PyExporter)arg1) -> bool

- `include_subtitles(...)` — None( (flame.PyExporter)arg1) -> bool 
None( (flame.PyExporter)arg1) -> bool

- `export_subtitles_as_files(...)` — None( (flame.PyExporter)arg1) -> bool 
None( (flame.PyExporter)arg1) -> bool

- `export_all_subtitles(...)` — None( (flame.PyExporter)arg1) -> bool 
None( (flame.PyExporter)arg1) -> bool

- `warn_on_unlinked(...)` — None( (flame.PyExporter)arg1) -> bool 
None( (flame.PyExporter)arg1) -> bool

- `warn_on_unrendered(...)` — None( (flame.PyExporter)arg1) -> bool 
None( (flame.PyExporter)arg1) -> bool

- `warn_on_pending_render(...)` — None( (flame.PyExporter)arg1) -> bool 
None( (flame.PyExporter)arg1) -> bool

- `warn_on_no_media(...)` — None( (flame.PyExporter)arg1) -> bool 
None( (flame.PyExporter)arg1) -> bool

- `warn_on_mixed_colour_space(...)` — None( (flame.PyExporter)arg1) -> bool 
None( (flame.PyExporter)arg1) -> bool

- `warn_on_reimport_unsupported(...)` — None( (flame.PyExporter)arg1) -> bool 
None( (flame.PyExporter)arg1) -> bool

- `keep_timeline_fx_renders(...)` — None( (flame.PyExporter)arg1) -> bool 
None( (flame.PyExporter)arg1) -> bool


### Static methods
- `get_presets_base_dir(...)` — get_presets_base_dir( (PyExporter.PresetVisibility)preset_visibility) -> str : 
get_presets_base_dir( (PyExporter.PresetVisibility)preset_visibility) -> str :
    Get a presets base directory.

- `get_presets_dir(...)` — get_presets_dir( (PyExporter.PresetVisibility)preset_visibility, (PyExporter.PresetType)preset_type) -> str : 
get_presets_dir( (PyExporter.PresetVisibility)preset_visibility, (PyExporter.PresetType)preset_type) -> str :
    Get a presets directory.


### Built-in methods
- `export(...)` — export( (PyExporter)arg1, (object)sources, (str)preset_path, (str)output_directory [, (PyExporter.BackgroundJobSettings)background_job_settings=None [, (object)hooks=None [, (object)hooks_user_data=None]]]) -> None : 
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


### Callable attributes
- `BackgroundJobSettings(...)` — Object holding background export job settings. These settings refer to the Backburner job, server and manager. 
Object holding background export job settings. These settings refer to the Backburner job, server and manager.

- `PresetType(...)` — int([x]) -> integer 
int([x]) -> integer
int(x, base=10) -> integer

Convert a number or string to an integer, or return 0 if no arguments
are given.  If x is a number, return x.__int__().  For floating-point
numbers, this truncates towards zero.

If x is not a number or if base is given, then x must be a string,
bytes, or bytearray instance representing an integer literal in the
given base.  The literal can be preceded by '+' or '-' and be surrounded
by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
Base 0 means to interpret the base from the string as an integer literal.
>>> int('0b100', base=0)
4

- `PresetVisibility(...)` — int([x]) -> integer 
int([x]) -> integer
int(x, base=10) -> integer

Convert a number or string to an integer, or return 0 if no arguments
are given.  If x is a number, return x.__int__().  For floating-point
numbers, this truncates towards zero.

If x is not a number or if base is given, then x must be a string,
bytes, or bytearray instance representing an integer literal in the
given base.  The literal can be preceded by '+' or '-' and be surrounded
by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
Base 0 means to interpret the base from the string as an integer literal.
>>> int('0b100', base=0)
4


### Attributes
- `Image_Sequence(...)` — 
- `Audio(...)` — 
- `Movie(...)` — 
- `Sequence_Publish(...)` — 
- `Distribution_Package(...)` — 
- `User(...)` — 
- `Project(...)` — 
- `Shared(...)` — 
- `Autodesk(...)` — 
- `Flow_Production_Tracking(...)` — 
- `Shotgun(...)` — 

