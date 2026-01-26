#!/usr/bin/env python3
"""Generate or populate docs/api/constants/*.md with runtime constant values.

Usage:
  python scripts/generate_constant_docs.py [--apply] [--dir docs/api/constants]

By default the script runs in dry-run mode and prints proposed updates. Use --apply to write changes.
"""
import argparse
import glob
import importlib
import os
import sys

TEMPLATE = """# Constant: {name}

**Module**: `flame`

{description}

---

**Type:** `{type}`

**Example value:**

```python
import flame
print(flame.{name})  # -> {value}
```

**Example usage:**

```python
# Example: use the constant where Flame APIs expect this identifier
# some_api.call(flame.{name})
```

**See also:**

- `docs/api/constants/` index

**Notes:**
- Values are collected at runtime and may vary between Flame versions or environments.
- Run this script with --apply to populate actual runtime values.
"""


def get_flame_module():
    try:
        return importlib.import_module('flame')
    except Exception:
        return None


def format_value(v):
    try:
        return repr(v)
    except Exception:
        return '<unrepresentable>'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--apply', action='store_true', help='Write updates to files')
    parser.add_argument('--dir', default='docs/api/constants', help='Directory with constant md files')
    args = parser.parse_args()

    flame = get_flame_module()
    if flame is None:
        print('Warning: `flame` module not importable. Files will be populated with placeholders.', file=sys.stderr)

    md_files = sorted(glob.glob(os.path.join(args.dir, '*.md')))
    if not md_files:
        print('No constant md files found in', args.dir)
        return 0

    for fn in md_files:
        name = os.path.splitext(os.path.basename(fn))[0]
        value = None
        value_type = 'unknown'
        if flame is not None:
            try:
                if hasattr(flame, name):
                    value = getattr(flame, name)
                    value_type = type(value).__name__
                else:
                    # Try attributes in uppercase or with prefix
                    alt = name.upper()
                    if hasattr(flame, alt):
                        value = getattr(flame, alt)
                        value_type = type(value).__name__
            except Exception:
                value = '<error accessing value>'
                value_type = 'error'

        value_repr = format_value(value) if value is not None else '<not available>'
        description = f"A Flame constant identified by the name `{name}`. The exact meaning and runtime value are determined at execution time."
        content = TEMPLATE.format(name=name, description=description, type=value_type, value=value_repr)

        if args.apply:
            with open(fn, 'w', encoding='utf-8') as f:
                f.write(content)
            print('Updated', fn)
        else:
            print('---', fn)
            print(content)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
