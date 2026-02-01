"""Library Inspector"""
import flame, json
def library():
    sel = flame.media_panel.get_selected_objects() if hasattr(flame.media_panel, "get_selected_objects") else []
    selection = [o for o in sel if "Library" in str(type(o))]
    lib = selection[0] if selection else None
    if not lib:
        return {"error": "No Library selected"}
    return {"name": str(lib.name), "shared": getattr(lib, "is_shared", False)}
if __name__ == "__main__":
    print(json.dumps(library(), indent=2))
