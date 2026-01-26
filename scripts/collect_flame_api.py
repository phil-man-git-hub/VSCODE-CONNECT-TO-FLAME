#!/usr/bin/env python3
"""Collect API metadata from a running Flame listener via the execute endpoint.

This script sends a small introspection payload to the listener which inspects
specified modules (default: 'flame') and prints a JSON blob with:
 - module name
 - functions: name, signature, doc (first line)
 - classes: name, doc (first line), methods (name, signature, doc)
 - constants: name

Usage:
  python scripts/collect_flame_api.py --host 127.0.0.1 --port 5555 --modules flame

Output: prints JSON to stdout.
"""

import argparse
import json
import socket

PAYLOAD_TEMPLATE = r"""
import json, inspect
mods = __MODULES__
result = {}
for mod_name in mods:
    try:
        m = __import__(mod_name)
    except Exception as e:
        result[mod_name] = {'error': repr(e)}
        continue
    info = {'functions': [], 'classes': [], 'constants': []}
    for name, member in inspect.getmembers(m):
        if name.startswith('_'):
            continue
        try:
            if inspect.isfunction(member) or inspect.ismethod(member):
                try:
                    sig = str(inspect.signature(member))
                except Exception:
                    sig = '(...)'
                doc_full = inspect.getdoc(member) or ''
                # Attempt to capture source when possible (C-implemented objects will fail)
                src = None
                try:
                    src = inspect.getsource(member)
                except Exception:
                    src = None
                info['functions'].append({'name': name, 'signature': sig, 'doc': doc_full, 'source': src})
            elif inspect.isclass(member):
                cls_doc_full = inspect.getdoc(member) or ''
                cls = {'name': name, 'doc': cls_doc_full, 'methods': []}
                for mname, mobj in inspect.getmembers(member):
                    if mname.startswith('_'):
                        continue
                    try:
                        if inspect.isfunction(mobj) or inspect.ismethod(mobj):
                            try:
                                msig = str(inspect.signature(mobj))
                            except Exception:
                                msig = '(...)'
                            mdoc_full = inspect.getdoc(mobj) or ''
                            msrc = None
                            try:
                                msrc = inspect.getsource(mobj)
                            except Exception:
                                msrc = None
                            cls['methods'].append({'name': mname, 'signature': msig, 'doc': mdoc_full, 'source': msrc})
                    except Exception:
                        continue
                info['classes'].append(cls)
            else:
                # heuristically treat as constant/attribute
                info['constants'].append(name)
        except Exception:
            continue
    result[mod_name] = info
print(json.dumps(result))
"""


def send_execute(host, port, code, timeout=10):
    payload = {'command': 'execute', 'id': 'collect_api', 'code': code}
    with socket.create_connection((host, port), timeout=5) as s:
        s.settimeout(timeout)
        s.sendall(json.dumps(payload).encode('utf-8'))
        data = b''
        while True:
            try:
                chunk = s.recv(4096)
            except Exception:
                break
            if not chunk:
                break
            data += chunk
    # The listener returns JSON response object with stdout containing our json.
    try:
        resp = json.loads(data.decode('utf-8'))
        stdout = resp.get('stdout', '')
        # The payload printed a JSON string; load it
        return json.loads(stdout)
    except Exception as e:
        raise RuntimeError(f'Failed to parse response: {e}; raw={data!r}')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='127.0.0.1')
    parser.add_argument('--port', type=int, default=5555)
    parser.add_argument('--modules', nargs='*', default=['flame'])
    args = parser.parse_args()
    # Inject module list safely into the payload
    code = PAYLOAD_TEMPLATE.replace('__MODULES__', repr(args.modules))
    result = send_execute(args.host, args.port, code)
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
