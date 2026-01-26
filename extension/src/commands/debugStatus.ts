import * as vscode from 'vscode';
import { FlameClient } from '../client';

export async function debugStatus(client: FlameClient) {
  const out = vscode.window.createOutputChannel('Flame');
  out.show(true);
  try {
    const s = client.getStatus();
    out.appendLine(`Status: connected=${s.connected} host=${s.host} port=${s.port} token=${s.token_present ? 'yes' : 'no'} buffer_len=${s.buffer_len}`);
    vscode.window.showInformationMessage('Flame status written to Flame output');
  } catch (e) {
    out.appendLine(`debugStatus error: ${e}`);
    vscode.window.showErrorMessage(`Failed to get status: ${e}`);
  }
}
