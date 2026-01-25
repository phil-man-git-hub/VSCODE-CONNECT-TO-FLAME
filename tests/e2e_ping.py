import socket, json, sys

HOST = '127.0.0.1'
PORT = 5555

def send_ping():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        payload = {'command': 'ping', 'id': 'e2e-test'}
        s.sendall(json.dumps(payload).encode('utf-8'))
        # Read response
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
    sys.exit(send_ping())
