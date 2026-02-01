"""Desktop Inspector"""
import flame, json
def desktop():
    ws = flame.project.current_project.current_workspace
    d = ws.desktop if ws else None
    if not d:
        return {"error": "No Desktop active"}
    return {"name": str(d.name), "reel_groups": len(d.reel_groups)}
if __name__ == "__main__":
    print(json.dumps(desktop(), indent=2))
