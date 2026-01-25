const net = require('net');

const HOST = process.env.FLAME_HOST || '127.0.0.1';
const PORT = process.env.FLAME_PORT ? Number(process.env.FLAME_PORT) : 5555;
const TOKEN = process.env.FLAME_TOKEN;

const CODE = `print('hello from extension demo')\ntry:\n    import flame\n    print('project:', getattr(flame.project, 'current_project', None))\nexcept Exception:\n    print('Flame module not available')`;

function run() {
  const client = net.createConnection({ host: HOST, port: PORT }, () => {
    const id = 'demo-' + Date.now();
    const payload = { command: 'execute', id, code: CODE };
    if (TOKEN) payload.token = TOKEN;
    client.write(JSON.stringify(payload) + '\n');
  });

  let buf = '';
  client.on('data', (chunk) => {
    buf += chunk.toString('utf-8');
    let idx;
    while ((idx = buf.indexOf('\n')) !== -1) {
      const line = buf.slice(0, idx).trim();
      buf = buf.slice(idx + 1);
      if (!line) continue;
      try {
        const msg = JSON.parse(line);
        console.log('--- Flame Output ---');
        console.log('stdout:\n' + (msg.stdout || ''));
        if (msg.stderr) console.log('stderr:\n' + msg.stderr);
        if (msg.exception) console.log('exception:\n' + msg.exception);
        client.end();
        return;
      } catch (e) {
        console.error('Failed to parse message:', e);
      }
    }
  });

  client.on('error', (err) => {
    console.error('Connection error:', err.message);
  });
}

run();
