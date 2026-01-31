import * as vscode from 'vscode';
import { FlameClient } from '../client';
import { v4 as uuidv4 } from 'uuid';

export async function testConnection(client: FlameClient) {
  const output = vscode.window.createOutputChannel('Flame');
  output.show(true);
  const id = uuidv4();
  try {
    const resp = await client.sendAndWait({ command: 'ping', id }, 3000);
    output.appendLine(`ping response: stdout=${resp.stdout || ''} stderr=${resp.stderr || ''}`);
    vscode.window.showInformationMessage('Ping sent to Flame (see Flame output)');
  } catch (e) {
    output.appendLine(`ping error: ${e}`);
    vscode.window.showErrorMessage(`Ping failed: ${e}`);
  }
}
