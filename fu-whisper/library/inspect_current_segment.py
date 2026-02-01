"""Segment Inspector"""
import flame, json
def segment():
    sel = flame.media_panel.get_selected_objects() if hasattr(flame.media_panel, "get_selected_objects") else []
    selection = [o for o in sel if "Segment" in str(type(o))]
    seg = selection[0] if selection else None
    if not seg:
        return {"error": "No Segment selected"}
    return {"name": str(seg.name), "source": str(getattr(seg, "source_name", "None"))}
if __name__ == "__main__":
    print(json.dumps(segment(), indent=2))
