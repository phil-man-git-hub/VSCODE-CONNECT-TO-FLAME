# Example script to run in Flame
try:
    import flame
    print(flame.project.current_project.name)
except Exception:
    print('Flame module not available; this is an example.')
