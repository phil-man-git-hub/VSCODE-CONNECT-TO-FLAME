import { FlameClient } from '../client';
import * as vscode from 'vscode';

export async function connect(client: FlameClient, host?: string, port?: number) {
  const output = vscode.window.createOutputChannel('Flame');
  output.show(true);
  output.appendLine('Connecting to Flame...');
  try {
    await client.connect(host, port);
    output.appendLine(`Connected to Flame at ${host || '127.0.0.1'}:${port || 5555}`);
    vscode.window.showInformationMessage('Connected to Flame (dev).');
  } catch (e) {
    output.appendLine(`Connect error: ${e}`);
    vscode.window.showErrorMessage(`Failed to connect: ${e}`);
  }
}
