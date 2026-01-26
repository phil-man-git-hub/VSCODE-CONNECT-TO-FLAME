import socket, json, sys

HOST = '127.0.0.1'
PORT = 5555

CODE = """
print('hello from flame')
try:
    import flame
    print('project:', getattr(flame.project, 'current_project', None))
except Exception:
    print('Flame module not available')
"""


def send_exec():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        payload = {'command': 'execute', 'id': 'e2e-exec', 'code': CODE}
        s.sendall(json.dumps(payload).encode('utf-8'))
        data = b''
        while True:
            chunk = s.recv(4096)
            if not chunk:
                break
            data += chunk
            try:
                resp = json.loads(data.decode('utf-8'))
                print('RESP:', resp)
                return 0
            except json.JSONDecodeError:
                continue
    return 1

if __name__ == '__main__':
    sys.exit(send_exec())
