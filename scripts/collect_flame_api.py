#!/usr/bin/env python3
"""Systematically query the Flame API and generate detailed JSON reports.

Strategy:
1. Discovery: Get a list of all symbols in the `flame` module.
2. Introspection: For each symbol (focusing on classes), send a dedicated 
   inspection payload to the listener to extract docstrings, methods, and properties.
3. Reporting: Save individual JSON files and an aggregate index.

Usage:
  python scripts/collect_flame_api.py --limit 10   # Test run
  python scripts/collect_flame_api.py --all        # Full crawl
"""

import argparse
import json
import socket
import os
import time
from datetime import datetime
from pathlib import Path

HOST = '127.0.0.1'
PORT = 5555
REPORT_BASE = Path('reports/api_dump')

# Payload to discover all members of the flame module
DISCOVERY_PAYLOAD = """
import flame
import json
# Get all attributes of the flame module, excluding private ones
members = [m for m in dir(flame) if not m.startswith('__')]
print(json.dumps(members))
"""

# Payload template to inspect a specific class/object
INSPECTION_PAYLOAD_TEMPLATE = """
import flame
import inspect
import json

target_name = "{target_name}"
try:
    obj = getattr(flame, target_name)
    
    data = {{
        "name": target_name,
        "type": type(obj).__name__,
        "doc": getattr(obj, "__doc__", ""),
        "module": getattr(obj, "__module__", "flame"),
        "properties": [],
        "methods": [],
        "inheritance": [c.__name__ for c in inspect.getmro(obj)] if inspect.isclass(obj) else []
    }}

    if inspect.isclass(obj):
        for name in dir(obj):
            if name.startswith("__"):
                continue
            
            try:
                # Use getattr_static if available (Py3) to avoid property execution, 
                # but fallback to getattr for Boost.Python compatibility if needed.
                # For Flame API (Boost), direct getattr is usually required to see the proxy type.
                attr = getattr(obj, name)
                
                member_info = {{
                    "name": name,
                    "doc": getattr(attr, "__doc__", "") or ""
                }}

                if isinstance(attr, property) or not callable(attr):
                    # It's likely a property or attribute
                    data["properties"].append(member_info)
                else:
                    # It's a method
                    member_info["signature"] = "" # Boost often hides this, but we'll try
                    try:
                        member_info["signature"] = str(inspect.signature(attr))
                    except (ValueError, TypeError):
                        pass
                    data["methods"].append(member_info)

            except Exception as e:
                # If accessing the attribute fails, log it briefly
                data["properties"].append({{"name": name, "error": str(e)}})

    print(json.dumps(data))

except Exception as e:
    print(json.dumps({{"name": target_name, "error": str(e)}}))
"""

def send_payload(code, description):
    """Send code to the listener and return the parsed JSON stdout."""
    payload = {
        "command": "execute",
        "id": f"crawl_{{int(time.time()*1000)}}",
        "code": code
    }
    
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(10)
            s.connect((HOST, PORT))
            s.sendall((json.dumps(payload) + "\n").encode('utf-8'))
            
            buffer = ""
            while True:
                chunk = s.recv(4096).decode('utf-8')
                if not chunk:
                    break
                buffer += chunk
                if "\n" in buffer:
                    break
            
            response = json.loads(buffer.strip())
            
            if response.get('exception'):
                print(f"Error inspecting {description}: {response.get('exception')}")
                print(f"Stderr: {response.get('stderr')}")
                return None
            
            out = response.get('stdout', '').strip()
            if not out:
                return None
            
            try:
                return json.loads(out)
            except json.JSONDecodeError:
                print(f"Invalid JSON from {description}: {out[:100]}...")
                return None
                
    except Exception as e:
        print(f"Connection error during {description}: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Crawl Flame API")
    parser.add_argument('--limit', type=int, help="Limit number of items to inspect (for testing)")
    parser.add_argument('--all', action='store_true', help="Inspect standard Py* classes and core managers")
    parser.add_argument('--include-all', action='store_true', help="Inspect every single discovered symbol (100+)")
    args = parser.parse_args()

    if not args.all and not args.include_all and args.limit is None:
        args.limit = 5
        print("Defaulting to limit=5. Use --all or --include-all for larger crawls.")

    # 1. Setup Report Directory
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_dir = REPORT_BASE / timestamp
    report_dir.mkdir(parents=True, exist_ok=True)
    print(f"Report Directory: {report_dir}")

    # 2. Discovery Phase
    print("Phase 1: Discovery...")
    members = send_payload(DISCOVERY_PAYLOAD, "Discovery")
    if not members:
        print("Discovery failed. Aborting.")
        return

    print(f"Discovered {len(members)} symbols.")
    
    # Filter symbols
    if args.include_all:
        targets = members
    else:
        # Default behavior: focus on classes and core objects
        targets = [m for m in members if m.startswith('Py') or m in ['flame', 'batch', 'project', 'projects']]
    
    # If limit is set
    if args.limit:
        targets = targets[:args.limit]
    
    print(f"Targeting {len(targets)} symbols for detailed inspection.")

    # 3. Introspection Phase
    results = []
    for i, target in enumerate(targets):
        print(f"[{i+1}/{len(targets)}] Inspecting: {target}")
        code = INSPECTION_PAYLOAD_TEMPLATE.format(target_name=target)
        data = send_payload(code, target)
        
        if data:
            # Save individual file
            file_path = report_dir / f"{target}.json"
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=2)
            
            # Add summary to results for index
            results.append({
                "name": data.get("name"),
                "type": data.get("type"),
                "file": str(file_path.name)
            })
        
        # Be gentle on the socket/server
        time.sleep(0.05)

    # 4. Index Generation
    index_data = {
        "timestamp": timestamp,
        "count": len(results),
        "items": results
    }
    with open(report_dir / "index.json", 'w') as f:
        json.dump(index_data, f, indent=2)

    print(f"Done. Reports saved to {report_dir}")

if __name__ == "__main__":
    main()