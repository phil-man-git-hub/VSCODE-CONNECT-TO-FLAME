import socket
import json
import time
import pytest

HOST = '127.0.0.1'
PORT = 5555

test_code = """
import flame
import threading

try:
    p1 = flame.project.current_project.name
    print(f"flame.project.current_project.name: {p1}")
except Exception as e:
    print(f"flame.project.current_project.name: FAILED ({e})")

try:
    p2 = flame.projects.current_project.name
    print(f"flame.projects.current_project.name: {p2}")
except Exception as e:
    print(f"flame.projects.current_project.name: FAILED ({e})")

print(f"Current Thread: {threading.current_thread().name}")
"""

payload = {
    "command": "execute",
    "id": "thread_test",
    "code": test_code
}

def test_connection():
    print(f"Connecting to {HOST}:{PORT}...")
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
            print("Response received:")
            print(f"STDOUT: {response.get('stdout')}")
            print(f"STDERR: {response.get('stderr')}")
            print(f"EXCEPTION: {response.get('exception')}")
    except Exception as e:
        pytest.skip(f"Listener not available: {e}")

if __name__ == "__main__":
    test_connection()
