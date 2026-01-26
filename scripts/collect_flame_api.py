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
SAFE_PREFIXES = ('get_', 'is_', 'has_', 'list_', 'find_', 'ping', 'version', 'get')
MAX_REPR_LEN = 500
DO_PROBES = __DO_PROBES__
for mod_name in mods:
    try:
        m = __import__(mod_name)
    except Exception as e:
        result[mod_name] = {'error': repr(e)}
        continue
    info = {'functions': [], 'classes': [], 'constants': []}
    if DO_PROBES:
        info['probes'] = {}
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
                # Safe probe: call no-arg simple getters/ping functions
                if DO_PROBES:
                    try:
                        sigobj = inspect.signature(member)
                        has_required = False
                        for p in sigobj.parameters.values():
                            if p.default is inspect._empty and p.kind in (inspect.Parameter.POSITIONAL_ONLY, inspect.Parameter.POSITIONAL_OR_KEYWORD):
                                has_required = True
                                break
                        if (not has_required) and any(name.startswith(pref) for pref in SAFE_PREFIXES):
                            try:
                                v = member()
                                info['probes'][name] = {'type': type(v).__name__, 'repr': repr(v)[:MAX_REPR_LEN]}
                            except Exception as e:
                                info['probes'][name] = {'error': repr(e)}
                    except Exception:
                        pass
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


def is_safe_callable(name: str, sig):
    """Decide conservatively whether it's safe to call a function/method with no args.

    Rules:
      - Only call if there are no required parameters.
      - Name must start with a safe prefix (get_, is_, has_, list_, find_, ping, version)
    """
    safe_prefixes = ('get_', 'is_', 'has_', 'list_', 'find_', 'ping', 'version', 'get')
    # no required parameters
    for p in sig.parameters.values():
        if p.default is inspect._empty and p.kind in (inspect.Parameter.POSITIONAL_ONLY, inspect.Parameter.POSITIONAL_OR_KEYWORD):
            return False
    return any(name.startswith(pref) for pref in safe_prefixes)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='127.0.0.1')
    parser.add_argument('--port', type=int, default=5555)
    parser.add_argument('--modules', nargs='*', default=['flame'])
    parser.add_argument('--probe-safe', action='store_true', help='Attempt safe probes to infer return types for no-arg functions')
    args = parser.parse_args()
    # Inject module list and probe flag safely into the payload
    code = PAYLOAD_TEMPLATE.replace('__MODULES__', repr(args.modules)).replace('__DO_PROBES__', 'True' if args.probe_safe else 'False')
    result = send_execute(args.host, args.port, code)

    # If probe-safe is requested, attempt to call selected safe functions to infer return types
    if args.probe_safe:
        for mod_name, data in result.items():
            for f in data.get('functions', []):
                try:
                    name = f['name']
                    sig = f.get('signature', '')
                    # parse signature locally to decide (we don't have inspect.Signature here), do light heuristic
                    if '(' in sig and ')' in sig:
                        params = sig[sig.find('(')+1:sig.find(')')].strip()
                    else:
                        params = ''
                    no_required = (params == '')
                    if no_required and is_safe_callable(name, __import__('inspect').signature if False else __import__('inspect').Signature):
                        # We can't call into Flame here; skip actual probe in this runner. The probe option is implemented for future remote probes.
                        f['probe_return'] = None
                except Exception:
                    continue

    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
