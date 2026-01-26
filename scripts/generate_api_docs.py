#!/usr/bin/env python3
"""Generate Markdown documentation and JSON index from a collected API JSON blob.

This script calls `collect_flame_api.py` (which queries the running Flame listener)
and writes:
 - docs/api/<module>.md (Markdown with functions/classes/constants)
 - docs/api/index.json (summary index mapping symbol -> module/type/snippet)

Usage:
  python scripts/generate_api_docs.py --out docs/api --host 127.0.0.1 --port 5555
"""

import argparse
import json
import os
import subprocess
from pathlib import Path


def render_module_md(module_name, data):
    lines = [f"# Module: {module_name}\n"]
    lines.append('\n')
    if 'error' in data:
        lines.append(f"**Error importing module**: {data['error']}\n")
        return ''.join(lines)
    if data.get('classes'):
        lines.append('## Classes\n')
        for c in data['classes']:
            # Link to per-class page
            lines.append(f"### class [{c['name']}](classes/{c['name']}.md)\n\n")
            if c.get('doc'):
                # short doc snippet
                snippet = (c['doc'].splitlines()[0] + '\n\n') if c.get('doc') else ''
                lines.append(snippet)
            if c.get('methods'):
                lines.append('#### Methods\n')
                for m in c['methods']:
                    k = m.get('kind')
                    kind_label = f" ({k})" if k else ''
                    doc_snip = (m.get('doc','').splitlines()[0] + ' ') if m.get('doc') else ''
                    lines.append(f"- `{m['name']}{m['signature']}`{kind_label} — {doc_snip}\n")
                lines.append('\n')
    if data.get('functions'):
        lines.append('## Functions\n')
        for f in data['functions']:
            rt = f.get('return', '') or ''
            if not rt:
                # try to detect annot
                rt = f.get('annotations', {}).get('return', '') if f.get('annotations') else ''
            rt_str = f" -> {rt}" if rt else ''
            doc_snip = (f['doc'].splitlines()[0] + ' ') if f.get('doc') else ''
            # Link to per-function page
            lines.append(f"- [{f['name']}](functions/{f['name']}.md) — `{f['name']}{f['signature']}{rt_str}` — {doc_snip}\n")
        lines.append('\n')
    if data.get('probes'):
        lines.append('## Probe results (safe calls)\n')
        for pname, pval in data['probes'].items():
            if pval is None:
                lines.append(f"- `{pname}`: (no result)\n")
            elif 'error' in pval:
                lines.append(f"- `{pname}`: ERROR - {pval['error']}\n")
            else:
                lines.append(f"- `{pname}`: {pval.get('type','?')} — {pval.get('repr','')}\n")
        lines.append('\n')
    if data.get('constants'):
        lines.append('## Constants / Attributes\n')
        for a in data['constants']:
            # Link to per-constant page
            lines.append(f"- [{a}](constants/{a}.md)\n")
        lines.append('\n')
    return ''.join(lines)


def render_class_md(module_name, cls):
    lines = [f"# Class: {cls['name']}\n\n", f"**Module**: `{module_name}`\n\n"]
    if cls.get('doc'):
        lines.append(cls['doc'] + '\n\n')
    if cls.get('methods'):
        lines.append('## Methods\n')
        methods = cls['methods']
        # Group by kind for clearer presentation
        groups = {}
        for m in methods:
            kind = m.get('kind', 'function')
            groups.setdefault(kind, []).append(m)
        kind_order = ['property', 'classmethod', 'staticmethod', 'builtin', 'method_descriptor', 'callable', 'function', 'attribute']
        kind_titles = {
            'property': 'Properties',
            'classmethod': 'Class methods',
            'staticmethod': 'Static methods',
            'builtin': 'Built-in methods',
            'method_descriptor': 'Method descriptors',
            'callable': 'Callable attributes',
            'function': 'Functions',
            'attribute': 'Attributes',
        }
        for k in kind_order:
            ms = groups.get(k, [])
            if not ms:
                continue
            lines.append(f"### {kind_titles.get(k, k.title())}\n")
            for m in ms:
                sig = m.get('signature','')
                # Pretty signature block
                lines.append(f"- `{m['name']}` — `{sig}`\n")
                lines.append('```python\n')
                lines.append(f"def {m['name']}{sig}\n")
                lines.append('```\n')
                # Parameter list (best-effort parsing)
                param_block = ''
                if sig and sig not in ('(...)','()') and '(' in sig and ')' in sig:
                    params = sig[sig.find('(')+1:sig.rfind(')')].strip()
                    if params:
                        pnames = [p.strip().split('=')[0].split(':')[0].strip() for p in params.split(',')]
                        lines.append('**Parameters**:\n')
                        for pn in pnames:
                            lines.append(f"- `{pn}`\n")
                # Docstring
                if m.get('doc'):
                    lines.append('\n')
                    lines.append(m['doc'].strip() + '\n\n')
            lines.append('\n')
    return ''.join(lines)


def render_function_md(module_name, fn):
    lines = [f"# Function: {fn['name']}\n\n", f"**Module**: `{module_name}`\n\n"]
    sig = fn.get('signature','')
    lines.append(f"**Signature**: `{fn['name']}{sig}`\n\n")
    if fn.get('doc'):
        lines.append(fn['doc'] + '\n\n')
    if fn.get('annotations'):
        lines.append('**Annotations**:\n')
        for k, v in fn.get('annotations',{}).items():
            lines.append(f"- `{k}`: `{v}`\n")
        lines.append('\n')
    if fn.get('return'):
        lines.append(f"**Return (probe / annotation)**: `{fn.get('return')}`\n\n")
    return ''.join(lines)


def render_constant_md(module_name, name):
    lines = [f"# Constant: {name}\n\n", f"**Module**: `{module_name}`\n\n"]
    lines.append('Documentation for constants is collected from runtime introspection when available.\n')
    return ''.join(lines)


def build_index(api_json):
    index = {}
    for module, data in api_json.items():
        if 'error' in data:
            continue
        for f in data.get('functions', []):
            index[f['name']] = {'module': module, 'type': 'function', 'signature': f['signature'], 'doc': f.get('doc',''), 'page': f"functions/{f['name']}.md"}
        for c in data.get('classes', []):
            index[c['name']] = {'module': module, 'type': 'class', 'doc': c.get('doc',''), 'page': f"classes/{c['name']}.md"}
            for m in c.get('methods', []):
                index[f"{c['name']}.{m['name']}"] = {'module': module, 'type': 'method', 'signature': m['signature'], 'doc': m.get('doc','')}
        for a in data.get('constants', []):
            index[a] = {'module': module, 'type': 'attribute', 'page': f"constants/{a}.md"}
    return index


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='127.0.0.1')
    parser.add_argument('--port', type=int, default=5555)
    parser.add_argument('--out', default='docs/api')
    parser.add_argument('--modules', nargs='*', default=['flame'])
    args = parser.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / 'classes').mkdir(parents=True, exist_ok=True)
    (out_dir / 'functions').mkdir(parents=True, exist_ok=True)
    (out_dir / 'constants').mkdir(parents=True, exist_ok=True)

    # Run the collector
    cmd = ['python3', 'scripts/collect_flame_api.py', '--host', args.host, '--port', str(args.port), '--modules'] + args.modules
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        print('Collector failed:', proc.stderr)
        return
    api_json = json.loads(proc.stdout)

    # Write per-module Markdown and per-symbol pages
    for module, data in api_json.items():
        md = render_module_md(module, data)
        md_path = out_dir / f"{module}.md"
        md_path.write_text(md)
        print('Wrote', md_path)

        # Per-class pages
        for c in data.get('classes', []):
            cls_md = render_class_md(module, c)
            cls_path = out_dir / 'classes' / f"{c['name']}.md"
            cls_path.write_text(cls_md)
            print('Wrote', cls_path)

        # Per-function pages
        for f in data.get('functions', []):
            fn_md = render_function_md(module, f)
            fn_path = out_dir / 'functions' / f"{f['name']}.md"
            fn_path.write_text(fn_md)
            print('Wrote', fn_path)

        # Per-constant pages
        for a in data.get('constants', []):
            a_md = render_constant_md(module, a)
            a_path = out_dir / 'constants' / f"{a}.md"
            a_path.write_text(a_md)
            print('Wrote', a_path)

    # Write index.json
    index = build_index(api_json)
    idx_path = out_dir / 'index.json'
    idx_path.write_text(json.dumps(index, indent=2))
    print('Wrote', idx_path)


if __name__ == '__main__':
    main()
