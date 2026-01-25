import * as vscode from 'vscode';
import { FlameClient } from './client';
import { runInFlame } from './commands/runInFlame';

let client: FlameClient | null = null;

export function activate(context: vscode.ExtensionContext) {
  client = new FlameClient();
  const connectCmd = vscode.commands.registerCommand('flame.connect', async () => {
    await client?.connect();
    vscode.window.showInformationMessage('Connected to Flame (dev).');
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
