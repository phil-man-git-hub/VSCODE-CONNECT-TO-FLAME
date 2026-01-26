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
            lines.append(f"### class {c['name']}\n\n")
            if c.get('doc'):
                lines.append(f"{c['doc']}\n\n")
            if c.get('methods'):
                lines.append('#### Methods\n')
                for m in c['methods']:
                    lines.append(f"- `{m['name']}{m['signature']}` — {m['doc']}\n")
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
            lines.append(f"- `{f['name']}{f['signature']}{rt_str}` — {doc_snip}{' ' if doc_snip else ''}\n")
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
        sample = ', '.join(data['constants'][:200])
        lines.append(sample + '\n')
    return ''.join(lines)


def build_index(api_json):
    index = {}
    for module, data in api_json.items():
        if 'error' in data:
            continue
        for f in data.get('functions', []):
            index[f['name']] = {'module': module, 'type': 'function', 'signature': f['signature'], 'doc': f['doc']}
        for c in data.get('classes', []):
            index[c['name']] = {'module': module, 'type': 'class', 'doc': c.get('doc','')}
            for m in c.get('methods', []):
                index[f"{c['name']}.{m['name']}"] = {'module': module, 'type': 'method', 'signature': m['signature'], 'doc': m['doc']}
        for a in data.get('constants', []):
            index[a] = {'module': module, 'type': 'attribute'}
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

    # Run the collector
    cmd = ['python3', 'scripts/collect_flame_api.py', '--host', args.host, '--port', str(args.port), '--modules'] + args.modules
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        print('Collector failed:', proc.stderr)
        return
    api_json = json.loads(proc.stdout)

    # Write per-module Markdown
    for module, data in api_json.items():
        md = render_module_md(module, data)
        md_path = out_dir / f"{module}.md"
        md_path.write_text(md)
        print('Wrote', md_path)

    # Write index.json
    index = build_index(api_json)
    idx_path = out_dir / 'index.json'
    idx_path.write_text(json.dumps(index, indent=2))
    print('Wrote', idx_path)


if __name__ == '__main__':
    main()
