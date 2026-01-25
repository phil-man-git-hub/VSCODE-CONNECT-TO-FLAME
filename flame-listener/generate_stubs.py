"""Basic stub generator for Flame types

Run this inside a Flame Python environment to produce `.pyi` files. This is a
best-effort generator that enumerates attributes and writes simple stubs.
"""

import inspect
import importlib

MODULES = ['flame']

for mod_name in MODULES:
    try:
        mod = importlib.import_module(mod_name)
    except Exception:
        print(f"Could not import {mod_name}")
        continue
    out_lines = [f"# Stubs for {mod_name}\n"]
    for name in dir(mod):
        if name.startswith('_'):
            continue
        try:
            attr = getattr(mod, name)
            if inspect.isclass(attr):
                out_lines.append(f"class {name}: ...\n")
            elif inspect.isfunction(attr) or inspect.ismodule(attr):
                out_lines.append(f"def {name}(*args, **kwargs): ...\n")
            else:
                out_lines.append(f"{name}: Any\n")
        except Exception:
            continue
    with open(f"{mod_name}.pyi", 'w') as f:
        f.writelines(out_lines)
    print(f"Wrote {mod_name}.pyi")
