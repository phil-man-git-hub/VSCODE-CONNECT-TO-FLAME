import * as net from 'net';

export class FlameClient {
  private socket: net.Socket | null = null;
  private host: string = '127.0.0.1';
  private port: number = 5555;
  private token: string | null = null;

  async connect(host?: string, port?: number) {
    if (host) this.host = host;
    if (port) this.port = port;
    return new Promise<void>((resolve, reject) => {
      this.socket = net.createConnection({ host: this.host, port: this.port }, () => resolve());
      this.socket!.on('error', (err) => reject(err));
    });
  }

  setAuthToken(token: string) {
    this.token = token;
  }

  send(payload: any) {
    if (!this.socket) throw new Error('Not connected');
    if (this.token) payload.token = this.token;
    this.socket.write(JSON.stringify(payload));
  }

  close() {
    this.socket?.end();
    this.socket = null;
  }
}
