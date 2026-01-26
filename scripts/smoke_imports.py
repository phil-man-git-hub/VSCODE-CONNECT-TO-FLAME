#!/usr/bin/env python3
import importlib
import traceback

def get_version(mod):
    for attr in ('__version__', 'version', 'VERSION'):
        v = getattr(mod, attr, None)
        if v:
            return v
    # special-case QtCore
    try:
        if mod.__name__ == 'PySide6':
            from PySide6 import QtCore
            return getattr(QtCore, '__version__', None)
    except Exception:
        pass
    return None

checks = [
    ('PySide6', ['PySide6']),
    ('OpenColorIO', ['OpenColorIO', 'opencolorio', 'PyOpenColorIO']),
    ('OpenImageIO', ['OpenImageIO', 'OpenImageIO as OIIO']),
    ('OpenTimelineIO', ['opentimelineio', 'OpenTimelineIO']),
    ('debugpy', ['debugpy']),
    ('pytest', ['pytest']),
    ('numpy', ['numpy']),
]

for display, candidates in checks:
    imported = False
    for name in candidates:
        modname = name.split(' as ')[0]
        try:
            m = importlib.import_module(modname)
            ver = get_version(m)
            print(f"{display}: imported via '{modname}'; version={ver}; file={getattr(m, '__file__', '')}")
            imported = True
            break
        except Exception as e:
            print(f"{display}: attempt to import '{modname}' failed: {e}")
            # optionally print traceback for debugging
            # traceback.print_exc()
    if not imported:
        print(f"{display}: NOT INSTALLED")
