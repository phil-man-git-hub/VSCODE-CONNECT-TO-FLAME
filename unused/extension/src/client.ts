import * as net from 'net';
import { EventEmitter } from 'events';

export class FlameClient extends EventEmitter {
  private socket: net.Socket | null = null;
  private host: string = '127.0.0.1';
  private port: number = 5555;
  private token: string | null = null;
  private buffer: string = '';

  // Utility for debugging: return connection status details
  getStatus() {
    return {
      connected: !!this.socket,
      host: this.host,
      port: this.port,
      token_present: !!this.token,
      buffer_len: this.buffer.length,
    };
  }

  constructor() {
    super();
  }

  async connect(host?: string, port?: number) {
    if (host) this.host = host;
    if (port) this.port = port;
    return new Promise<void>((resolve, reject) => {
      this.socket = net.createConnection({ host: this.host, port: this.port }, () => resolve());
      this.socket!.on('error', (err) => reject(err));
      this.socket!.on('data', (chunk: Buffer) => this.onData(chunk));
    });
  }

  setAuthToken(token: string) {
    this.token = token;
  }

  private onData(chunk: Buffer) {
    this.buffer += chunk.toString('utf-8');
    // Messages are newline terminated JSON
    let idx: number;
    while ((idx = this.buffer.indexOf('\n')) !== -1) {
      const line = this.buffer.slice(0, idx).trim();
      this.buffer = this.buffer.slice(idx + 1);
      if (!line) continue;
      try {
        const msg = JSON.parse(line);
        this.emit('response', msg);
      } catch (e) {
        // Ignore unparsable lines
      }
    }
  }

  send(payload: any) {
    if (!this.socket) throw new Error('Not connected');
    if (this.token) payload.token = this.token;
    this.socket.write(JSON.stringify(payload) + '\n');
  }

  sendAndWait(payload: any, timeout = 5000): Promise<any> {
    return new Promise((resolve, reject) => {
      const id = payload.id;
      const onResp = (msg: any) => {
        if (msg && msg.id === id) {
          this.removeListener('response', onResp);
          clearTimeout(timer);
          resolve(msg);
        }
      };
      const timer = setTimeout(() => {
        this.removeListener('response', onResp);
        reject(new Error('timeout waiting for response'));
      }, timeout);
      this.on('response', onResp);
      try {
        this.send(payload);
      } catch (e) {
        clearTimeout(timer);
        this.removeListener('response', onResp);
        reject(e);
      }
    });
  }

  close() {
    this.socket?.end();
    this.socket = null;
    this.buffer = '';
  }
}
