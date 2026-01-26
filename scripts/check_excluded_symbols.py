import socket
import json

HOST = '127.0.0.1'
PORT = 5555

DISCOVERY_PAYLOAD = """
import flame
import json
# Get all attributes of the flame module, excluding private ones
members = [m for m in dir(flame) if not m.startswith('__')]
print(json.dumps(members))
"""

payload = {
    "command": "execute",
    "id": "discovery_check",
    "code": DISCOVERY_PAYLOAD
}

def check_excluded():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(5)
        s.connect((HOST, PORT))
        s.sendall((json.dumps(payload) + "\n").encode('utf-8'))
        
        buffer = ""
        while True:
            chunk = s.recv(4096).decode('utf-8')
            if not chunk: break
            buffer += chunk
            if "\n" in buffer: break
            
        response = json.loads(buffer.strip())
        members = json.loads(response['stdout'])
        
        targets = [m for m in members if m.startswith('Py') or m in ['flame', 'batch', 'project', 'projects']]
        excluded = sorted(list(set(members) - set(targets)))
        
        print(f"Total Discovered: {len(members)}")
        print(f"Targeted: {len(targets)}")
        print(f"Excluded ({len(excluded)}):")
        for x in excluded:
            print(f" - {x}")

if __name__ == "__main__":
    check_excluded()
