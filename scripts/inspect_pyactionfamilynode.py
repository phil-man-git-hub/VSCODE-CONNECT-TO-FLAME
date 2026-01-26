import socket
import json

HOST = '127.0.0.1'
PORT = 5555

inspection_code = """
import flame
import inspect

cls = flame.PyActionFamilyNode
members = dir(cls)
data = {
    'name': cls.__name__,
    'doc': cls.__doc__,
    'properties': [],
    'methods': []
}

for name in members:
    if name.startswith('__'):
        continue
    attr = getattr(cls, name)
    if isinstance(attr, property) or not callable(attr): 
        # Boost.python often exposes properties as weird descriptors, 
        # but 'not callable' is a decent heuristic for data/properties in this context
        data['properties'].append(name)
    else:
        # It is likely a method
        doc = getattr(attr, '__doc__', '')
        data['methods'].append({'name': name, 'doc': doc})

import json
print(json.dumps(data, indent=2))
"""

payload = {
    "command": "execute",
    "id": "inspect_PyActionFamilyNode",
    "code": inspection_code
}

def inspect_flame_class():
    print(f"Connecting to {HOST}:{PORT}...")
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
            print(f"EXCEPTION: {response.get('exception')}")
            print(f"STDERR: {response.get('stderr')}")
        else:
            print(response.get('stdout'))

if __name__ == "__main__":
    inspect_flame_class()
