"""Inspect Flame / dev venv for common runtime packages.

Usage:
- Run locally in dev venv: `python examples/inspect_flame_env.py`
- Run inside Flame via `Flame: Run in Flame` or place this script in Flame's Python and run.

This prints import name, version (when available), and module file path.
"""
import importlib
import traceback

checks = [
    ('PySide6', ['PySide6']),
    ('PyOpenColorIO (OpenColorIO)', ['PyOpenColorIO', 'OpenColorIO', 'opencolorio']),
    ('OpenImageIO', ['OpenImageIO']),
    ('OpenTimelineIO', ['opentimelineio', 'OpenTimelineIO']),
    ('debugpy', ['debugpy']),
    ('numpy', ['numpy']),
]


def get_version(m):
    for attr in ('__version__', 'version', 'VERSION'):
        v = getattr(m, attr, None)
        if v:
            return v
    # special-case PySide6
    if getattr(m, '__name__', '').startswith('PySide6'):
        try:
            from PySide6 import QtCore
            return getattr(QtCore, '__version__', None)
        except Exception:
            pass
    return None


for display, candidates in checks:
    imported = False
    for name in candidates:
        try:
            mod = importlib.import_module(name)
            ver = get_version(mod)
            print(f"{display}: imported via '{name}'; version={ver}; file={getattr(mod, '__file__', None)}")
            imported = True
            break
        except Exception as e:
            # print a short message, but keep trying fallback names
            # traceback.print_exc()
            continue
    if not imported:
        print(f"{display}: NOT INSTALLED (attempted: {candidates})")
