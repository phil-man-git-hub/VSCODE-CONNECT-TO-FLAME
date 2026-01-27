#!/usr/bin/env python3
"""Generate Python type stubs (.pyi) from JSON API reports.

This script parses the detailed JSON introspection reports and produces
a consolidated flame.pyi file for IDE autocompletion and type checking.
"""

import argparse
import json
import re
from pathlib import Path

# Paths
REPO_ROOT = Path(__file__).resolve().parents[1]
STUBS_DIR = REPO_ROOT / 'stubs'

def load_index(report_dir: Path):
    index_path = report_dir / 'index.json'
    if not index_path.exists():
        raise FileNotFoundError(f"Index not found at {index_path}")
    with open(index_path, 'r') as f:
        return json.load(f)

def parse_signature(doc: str, name: str):
    """
    Attempts to extract a clean Python signature from Flame's docstrings.
    Example: 'append_setup( (PyBatch)arg1, (str)setup_path [, (bool)confirm=True]) -> bool :'
    """
    if not doc:
        return "(self, *args, **kwargs) -> Any"
    
    # Look for the signature line: name( ... ) -> type :
    pattern = rf"{name}\s*\((.*?)\)\s*->\s*([^:]+)"
    match = re.search(pattern, doc)
    
    if not match:
        return "(self, *args, **kwargs) -> Any"
    
    raw_args = match.group(1).strip()
    ret_type = match.group(2).strip()
    
    # Basic cleanup of Flame's pseudo-type notation: (PyBatch)arg1 -> arg1
    # We'll keep it simple for now and just return Any for types to ensure validity
    # but try to preserve the parameter names.
    
    if not raw_args:
        return "() -> " + ret_type
    
    # Split args, handle the '[, ...]' notation
    args_list = []
    # Simplified splitting - just getting the arg names if possible
    # e.g. (str)setup_path -> setup_path
    clean_args = re.sub(r'\(([^)]+)\)', '', raw_args) # remove types
    clean_args = clean_args.replace('[', '').replace(']', '') # remove optional brackets
    
    parts = [p.strip() for p in clean_args.split(',') if p.strip()]
    
    final_params = []
    for i, p in enumerate(parts):
        # Handle 'arg1' which is usually 'self' in class methods
        if p == 'arg1' and i == 0:
            final_params.append("self")
        else:
            # If it has a default value like 'confirm=True'
            if '=' in p:
                final_params.append(p)
            else:
                final_params.append(f"{p}: Any")
                
    return f"({', '.join(final_params)}) -> Any"

def generate_stubs(report_dir: Path):
    index = load_index(report_dir)
    out_lines = [
        "from typing import Any, List, Dict, Optional, Tuple, Union\n",
        "\n",
        "# Auto-generated stubs for Autodesk Flame API\n",
        "\n"
    ]
    
    # Collect all items
    items = []
    for entry in index['items']:
        with open(report_dir / entry['file'], 'r') as f:
            items.append(json.load(f))
            
    # Sort: Classes first, then functions, then objects
    classes = [i for i in items if i.get('type') == 'class' or i['name'].startswith('Py')]
    functions = [i for i in items if i.get('type') == 'builtin_function_or_method' or (not i['name'].startswith('Py') and 'methods' not in i)]
    singletons = [i for i in items if i not in classes and i not in functions]
    
    # Classes
    for cls in classes:
        name = cls['name']
        base = "object"
        inheritance = cls.get('inheritance', [])
        if len(inheritance) > 1:
            # inheritance[0] is usually the class itself, [1] is the parent
            parent = inheritance[1]
            if parent not in ('instance', 'object'):
                base = parent
        
        out_lines.append(f"class {name}({base}):\n")
        doc = cls.get('doc', '').splitlines()[0] if cls.get('doc') else ''
        if doc:
            out_lines.append(f'    """{doc}"""\n')
        
        # Properties
        for prop in cls.get('properties', []):
            p_name = prop['name']
            p_doc = prop.get('doc', '').replace('\n', ' ').strip()
            if p_doc:
                out_lines.append(f"    # {p_doc}\n")
            out_lines.append(f"    {p_name}: Any = ...\n")
            
        # Methods
        for method in cls.get('methods', []):
            m_name = method['name']
            m_doc = method.get('doc', '')
            # Attempt to get a better signature if it's in the doc
            sig = parse_signature(m_doc, m_name)
            
            # Simple docstring
            m_short_doc = m_doc.strip().splitlines()[0] if m_doc.strip() else ''
            if m_short_doc:
                out_lines.append(f"    # {m_short_doc}\n")
            out_lines.append(f"    def {m_name}{sig}: ...\n")
        
        if not cls.get('properties') and not cls.get('methods'):
            out_lines.append("    ...\n")
        out_lines.append("\n")

    # Global Functions
    out_lines.append("# Global Functions\n")
    for func in functions:
        name = func['name']
        f_doc = func.get('doc', '')
        sig = parse_signature(f_doc, name).replace('self, ', '').replace('self', '')
        if sig == '() -> Any':
            sig = '(*args, **kwargs) -> Any'
            
        out_lines.append(f"def {name}{sig}: ...\n")
        
    out_lines.append("\n")

    # Singleton Instances/Objects
    out_lines.append("# Global Objects (Singletons)\n")
    for obj in singletons:
        name = obj['name']
        obj_type = obj.get('type', 'Any')
        out_lines.append(f"{name}: {obj_type} = ...\n")

    STUBS_DIR.mkdir(exist_ok=True)
    out_path = STUBS_DIR / 'flame.pyi'
    with open(out_path, 'w') as f:
        f.writelines(out_lines)
    print(f"Generated stubs at {out_path}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--report-dir', type=Path, help="Path to the JSON report directory")
    parser.add_argument('--latest', action='store_true', help="Automatically use the latest report")
    args = parser.parse_args()

    if args.latest:
        dumps = sorted(list((REPO_ROOT / 'reports/api_dump').glob('*')))
        if not dumps:
            print("No reports found.")
            return
        report_dir = dumps[-1]
    elif args.report_dir:
        report_dir = args.report_dir
    else:
        print("Please specify --report-dir or --latest")
        return

    generate_stubs(report_dir)

if __name__ == '__main__':
    main()