
# Class: PyCoCameraAnalysis

**Module**: `flame`

## Inheritance & Hierarchy
* **Base class:** `PyCoNode` (inherits from `PyNode` → `PyFlameObject`)
* **Functional Role:** Camera analysis node in the schematic, used for analyzing camera movement and parameters.

## Description
Represents a camera analysis node, providing tools for analyzing and extracting camera data in the node graph.

---


## Methods
### Built-in methods
- `resetAnalysis(...)` — resetAnalysis( (PyCoCameraAnalysis)arg1) -> bool : 
resetAnalysis( (PyCoCameraAnalysis)arg1) -> bool :
    Reset the current analysis.

### Example
```python
# Example: Run camera analysis for a frame range
# Assume 'cam_node' is a PyCoCameraAnalysis node object
start_frame = 100
end_frame = 200
success = cam_node.analyseRange(start_frame, end_frame)
if success:
    print('Camera analysis completed')
else:
    print('Analysis failed or returned no results')
```
- `analyseRange(...)` — analyseRange( (PyCoCameraAnalysis)arg1, (object)arg2, (object)start) -> bool : 
analyseRange( (PyCoCameraAnalysis)arg1, (object)arg2, (object)start) -> bool :
    Run the analysis for the given frame range using the first frame as a reference if none has been already set.


