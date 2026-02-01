"""Clip Inspector"""
import flame, json
def clip():
    sel = flame.media_panel.get_selected_objects() if hasattr(flame.media_panel, "get_selected_objects") else []
    selection = [o for o in sel if "Clip" in str(type(o))]
    c = selection[0] if selection else None
    if not c:
        return {"error": "No Clip selected"}
    return {"name": str(c.name), "width": getattr(c, "width", 0), "height": getattr(c, "height", 0)}
if __name__ == "__main__":
    print(json.dumps(clip(), indent=2))
