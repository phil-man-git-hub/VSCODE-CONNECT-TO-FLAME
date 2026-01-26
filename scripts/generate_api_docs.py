#!/usr/bin/env python3
"""Convert JSON API dumps into Markdown documentation for MkDocs.

Usage:
  python scripts/generate_api_docs.py --report-dir reports/api_dump/LATEST_TIMESTAMP
"""

import argparse
import json
import shutil
from pathlib import Path

# Paths
REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS_API_ROOT = REPO_ROOT / 'docs' / 'api'

def clean_api_docs():
    """Remove existing generated API docs to ensure a clean slate."""
    for subdir in ['classes', 'functions', 'constants']:
        path = DOCS_API_ROOT / subdir
        if path.exists():
            shutil.rmtree(path)
        path.mkdir(parents=True, exist_ok=True)

def load_index(report_dir: Path):
    index_path = report_dir / 'index.json'
    if not index_path.exists():
        raise FileNotFoundError(f"Index not found at {index_path}")
    with open(index_path, 'r') as f:
        return json.load(f)

def format_docstring(doc: str) -> str:
    """Clean up docstrings for Markdown."""
    if not doc:
        return ""
    # Convert indentation to blockquotes or code blocks if needed?
    # For now, just ensuring it doesn't break tables
    return doc.replace('\n', '\n\n')

def generate_class_md(data: dict) -> str:
    name = data['name']
    md = [f"# Class: {name}\n"]
    
    md.append(f"**Module**: `{data.get('module', 'flame')}`\n")

    # Inheritance
    inheritance = data.get('inheritance', [])
    if inheritance:
        # Linkify parents if possible (assuming they exist in the same doc set)
        parents = []
        for p in inheritance:
            if p.startswith('Py'):
                parents.append(f"[{p}]({p}.md)")
            else:
                parents.append(p)
        if len(parents) > 1: # Skip self if listed
             md.append(f"**Inherits from**: {', '.join(parents[1:])}\n")

    # Docstring
    if data.get('doc'):
        md.append("## Description")
        md.append(format_docstring(data['doc']))
        md.append("\n")

    # Properties
    props = data.get('properties', [])
    if props:
        md.append("## Properties")
        md.append("| Name | Description |")
        md.append("| --- | --- |")
        for p in props:
            p_name = p['name']
            p_doc = p.get('doc', '').replace('\n', ' ').strip()
            md.append(f"| `{p_name}` | {p_doc} |")
        md.append("\n")

    # Methods
    methods = data.get('methods', [])
    if methods:
        md.append("## Methods")
        for m in methods:
            m_name = m['name']
            m_sig = m.get('signature', '()')
            m_doc = m.get('doc', '')
            
            md.append(f"### `{m_name}`")
            md.append(f"```python\n{m_name}{m_sig}\n```")
            if m_doc:
                md.append(f"{format_docstring(m_doc)}\n")
            md.append("---\n")

    return "\n".join(md)

def generate_function_md(data: dict) -> str:
    name = data['name']
    md = [f"# Function: {name}\n"]
    md.append(f"**Module**: `{data.get('module', 'flame')}`\n")
    
    # Signature reconstruction (approximate)
    # The crawl capture might put signature in doc or separate field depending on object type
    # For global functions captured as 'builtin', signature might be empty
    
    md.append("## Description")
    if data.get('doc'):
        md.append(format_docstring(data['doc']))
    
    return "\n".join(md)

def generate_object_md(data: dict) -> str:
    """For singleton instances like 'project' or 'batch'."""
    name = data['name']
    obj_type = data['type']
    
    md = [f"# Object: {name}\n"]
    md.append(f"**Type**: [`{obj_type}`](../classes/{obj_type}.md)\n")
    
    if data.get('doc'):
        md.append("## Description")
        md.append(format_docstring(data['doc']))
        
    return "\n".join(md)

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

    print(f"Generating docs from: {report_dir}")
    clean_api_docs()
    
    index = load_index(report_dir)
    
    # Categorize
    classes = []
    functions = []
    objects = []

    for item in index['items']:
        file_path = report_dir / item['file']
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        name = data['name']
        
        # Determine category
        if name.startswith('Py'):
            category = 'classes'
            content = generate_class_md(data)
            classes.append(name)
        elif name[0].islower() and data['type'] == 'builtin_function_or_method':
            category = 'functions'
            content = generate_function_md(data)
            functions.append(name)
        else:
            category = 'objects' # e.g. 'batch', 'project' (instances)
            content = generate_object_md(data)
            objects.append(name)

        # Write file
        # We put objects in the root of api/ or classes/? Let's put singleton objects in classes for now or root
        # Logic: Py* -> classes/, functions -> functions/, others -> objects/
        
        if category == 'objects':
            out_path = DOCS_API_ROOT / f"{name}.md" # Root level for global objects
        else:
            out_path = DOCS_API_ROOT / category / f"{name}.md"
            
        with open(out_path, 'w') as f:
            f.write(content)

    print(f"Generated {len(classes)} classes, {len(functions)} functions, {len(objects)} global objects.")
    
    # Generate Index/Nav helper if needed (Optional) 
    # For now, we rely on MkDocs identifying the files.

if __name__ == '__main__':
    main()