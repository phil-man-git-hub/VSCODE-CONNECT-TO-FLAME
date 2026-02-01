"""Batch Group Inspector"""
import flame, json
def batchgroup():
    sel = flame.media_panel.get_selected_objects() if hasattr(flame.media_panel, "get_selected_objects") else []
    selection = [o for o in sel if "BatchGroup" in str(type(o))]
    bg = selection[0] if selection else None
    if not bg:
        return {"error": "No Batch Group found"}
    return {"name": str(bg.name), "iteration": str(getattr(bg, "iteration", "1"))}
if __name__ == "__main__":
    print(json.dumps(batchgroup(), indent=2))
