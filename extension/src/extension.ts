import * as vscode from 'vscode';
import { FlameClient } from './client';
import { runInFlame } from './commands/runInFlame';
import { loadFlameProjectConfig, getAuthToken } from './config';

let client: FlameClient | null = null;

export function activate(context: vscode.ExtensionContext) {
  client = new FlameClient();
  const connectCmd = vscode.commands.registerCommand('flame.connect', async () => {
    const cfg = await loadFlameProjectConfig();
    const host = cfg.listener?.host || '127.0.0.1';
    const port = cfg.listener?.port || 5555;
    const token = await getAuthToken();
    if (token) client?.setAuthToken(token);
    await client?.connect(host, port);
    vscode.window.showInformationMessage(`Connected to Flame at ${host}:${port}`);
  });
  const runCmd = vscode.commands.registerCommand('flame.runInFlame', async () => {
    const editor = vscode.window.activeTextEditor;
    if (!editor) {
      vscode.window.showErrorMessage('No active editor');
      return;
    }
    const code = editor.document.getText(editor.selection.isEmpty ? undefined : editor.selection);
    await runInFlame(client!, code);
  });
  context.subscriptions.push(connectCmd, runCmd);
}

export function deactivate() {
  // cleanup
}
