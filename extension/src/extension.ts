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
    // Use shared connect command to provide consistent logging in Flame output
    const { connect } = await import('./commands/connect');
    await connect(client!, host, port);
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

  const startDebugCmd = vscode.commands.registerCommand('flame.startDebug', async () => {
    const id = 'start-debug-' + Date.now();
    try {
      const resp = await client!.sendAndWait({ command: 'start_debug_server', id, port: 5678 }, 10000);
      vscode.window.showInformationMessage(`${resp.stdout || resp.stderr}`);
    } catch (e) {
      vscode.window.showErrorMessage(`Failed to start debug server: ${e}`);
    }
  });

  const testConnCmd = vscode.commands.registerCommand('flame.testConnection', async () => {
    const { testConnection } = await import('./commands/testConnection');
    await testConnection(client!);
  });

  context.subscriptions.push(connectCmd, runCmd, startDebugCmd, testConnCmd);
}

export function deactivate() {
  // cleanup
}
