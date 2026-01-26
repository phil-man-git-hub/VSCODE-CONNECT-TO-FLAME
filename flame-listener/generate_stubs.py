"""Basic stub generator for Flame types

Run this inside a Flame Python environment to produce `.pyi` files. This is a
best-effort generator that enumerates attributes and writes simple stubs.

Improvements:
 - `--out-dir` to control where `.pyi` files are written (default: current dir)
 - `--quiet` to suppress stdout
 - Emitted stubs include `from typing import Any` for validity
"""

import inspect
import importlib
import os
import argparse
import sys

MODULES = ['flame']


def generate_stubs_for_module(mod_name: str, out_dir: str, quiet: bool = False) -> bool:
    try:
        mod = importlib.import_module(mod_name)
    except Exception as e:
        if not quiet:
            print(f"Could not import {mod_name}: {e}")
        return False

    out_lines = ["from typing import Any\n\n", f"# Stubs for {mod_name}\n"]

    def fmt_signature(obj):
        try:
            sig = inspect.signature(obj)
        except Exception:
            return '(...) -> Any'
        parts = []
        for p in sig.parameters.values():
            name = p.name
            if p.kind == inspect.Parameter.VAR_POSITIONAL:
                parts.append(f"*{name}: Any")
            elif p.kind == inspect.Parameter.VAR_KEYWORD:
                parts.append(f"**{name}: Any")
            else:
                default = ' = ...' if p.default is not inspect._empty else ''
                parts.append(f"{name}: Any{default}")
        return f"({', '.join(parts)}) -> Any"

    for name in dir(mod):
        if name.startswith('_'):
            continue
        try:
            attr = getattr(mod, name)
            if inspect.isclass(attr):
                out_lines.append(f"class {name}:\n")
                # include simple docstring
                doc = (inspect.getdoc(attr) or '').splitlines()[0] if inspect.getdoc(attr) else ''
                if doc:
                    out_lines.append(f"    \"\"\"{doc}\"\"\"\n")
                # list methods
                try:
                    for mname, mobj in inspect.getmembers(attr):
                        if mname.startswith('_'):
                            continue
                        if inspect.isfunction(mobj) or inspect.ismethod(mobj):
                            msig = fmt_signature(mobj)
                            mdoc = (inspect.getdoc(mobj) or '').splitlines()[0] if inspect.getdoc(mobj) else ''
                            if mdoc:
                                out_lines.append(f"    # {mdoc}\n")
                            out_lines.append(f"    def {mname}{msig}: ...\n")
                except Exception:
                    pass
                out_lines.append("\n")
            elif inspect.isfunction(attr) or inspect.ismodule(attr):
                sig = fmt_signature(attr)
                doc = (inspect.getdoc(attr) or '').splitlines()[0] if inspect.getdoc(attr) else ''
                if doc:
                    out_lines.append(f"# {doc}\n")
                out_lines.append(f"def {name}{sig}: ...\n")
            else:
                out_lines.append(f"{name}: Any\n")
        except Exception:
            # best-effort: skip problematic attributes
            continue

    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"{mod_name}.pyi")
    try:
        with open(out_path, 'w') as f:
            f.writelines(out_lines)
        if not quiet:
            print(f"Wrote {out_path}")
        return True
    except Exception as e:
        if not quiet:
            print(f"Failed to write {out_path}: {e}")
        return False


if __name__ == '__main__':
    p = argparse.ArgumentParser(description='Generate basic .pyi stubs for Flame modules')
    p.add_argument('--out-dir', '-o', default='.', help='Output directory for .pyi files')
    p.add_argument('--quiet', action='store_true', help='Suppress non-error output')
    p.add_argument('--modules', '-m', nargs='*', help='Module names to generate stubs for (defaults to flame)')
    args = p.parse_args()

    mods = args.modules if args.modules else MODULES
    success = True
    for m in mods:
        ok = generate_stubs_for_module(m, args.out_dir, quiet=args.quiet)
        success = success and ok
    sys.exit(0 if success else 1)
