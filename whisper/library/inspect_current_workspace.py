"""Workspace Inspector"""
import flame, json
def workspace():
    ws = flame.project.current_project.current_workspace
    if not ws:
        return {"error": "No Workspace active"}
    return {"name": str(ws.name), "libraries": len(ws.libraries)}
if __name__ == "__main__":
    print(json.dumps(workspace(), indent=2))
