
# Class: PyProjectSelector

**Module**: `flame`

## Inheritance & Hierarchy
* **Base Class:** PyFlameObject
* **Context:** Used for project management and selection in the Flame environment.

## Functional Role & Context
* **Functional Role:** Provides access to the Project Manager, allowing selection and querying of the current project.
* **Context:** Used for automating project selection and management tasks.

## Description
The `PyProjectSelector` is a read-only accessor for the Project Manager; it provides the current active `PyProject` object (if any) and acts as a gateway to project-specific automation.

---

**Note:** Project creation/loading is not performed via this selector; it is primarily used to query the active project and obtain a `PyProject` instance.

**Example:**

```python
proj_selector = flame.project_selector
current_proj = proj_selector.current_project
if current_proj:
    flame.messages.info(f"Active project: {current_proj.name}")
else:
    flame.messages.warning('No project currently open')
```

## Methods
### Properties
- `current_project(...)` — None( (flame.PyProjectSelector)arg1) -> object 
None( (flame.PyProjectSelector)arg1) -> object


