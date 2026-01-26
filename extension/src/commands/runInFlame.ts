import * as vscode from 'vscode';
import { FlameClient } from '../client';
import { v4 as uuidv4 } from 'uuid';

export async function runInFlame(client: FlameClient, code: string) {
  const id = uuidv4();
  const payload = { command: 'execute', id, code };
  const output = vscode.window.createOutputChannel('Flame');
  output.show(true);
  try {
    const resp = await client.sendAndWait(payload, 10000);
    output.appendLine(`stdout:\n${resp.stdout || ''}`);
    if (resp.stderr) output.appendLine(`stderr:\n${resp.stderr}`);
    if (resp.exception) output.appendLine(`exception:\n${resp.exception}`);
    vscode.window.showInformationMessage('Code executed in Flame (see Flame output)');
  } catch (e) {
    vscode.window.showErrorMessage(`Failed to send code: ${e}`);
  }
}
