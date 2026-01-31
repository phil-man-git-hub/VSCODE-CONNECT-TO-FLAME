const { FlameClient } = require('./out/client');
(async () => {
  const client = new FlameClient();
  try {
    console.log('Connecting to mock server on 127.0.0.1:5556...');
    await client.connect('127.0.0.1', 5556);
    console.log('Connected');
    const id = 't-' + Date.now();
    const resp = await client.sendAndWait({ command: 'ping', id }, 3000);
    console.log('Response:', resp);
    client.close();
  } catch (e) {
    console.error('Error:', e);
    client.close();
    process.exit(1);
  }
})();