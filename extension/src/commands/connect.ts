import { FlameClient } from '../client';
import * as vscode from 'vscode';

export async function connect(client: FlameClient) {
  const output = vscode.window.createOutputChannel('Flame');
  output.show(true);
  output.appendLine('Connecting to Flame...');
  try {
    await client.connect();
    output.appendLine('Connected to Flame (dev)');
    vscode.window.showInformationMessage('Connected to Flame (dev).');
  } catch (e) {
    output.appendLine(`Connect error: ${e}`);
    vscode.window.showErrorMessage(`Failed to connect: ${e}`);
  }
}
