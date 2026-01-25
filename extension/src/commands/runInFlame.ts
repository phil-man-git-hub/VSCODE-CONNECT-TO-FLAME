import * as vscode from 'vscode';
import { FlameClient } from '../client';
import { v4 as uuidv4 } from 'uuid';

export async function runInFlame(client: FlameClient, code: string) {
  const id = uuidv4();
  const payload = { command: 'execute', id, code };
  try {
    client.send(payload);
    vscode.window.showInformationMessage('Sent code to Flame (dev).');
  } catch (e) {
    vscode.window.showErrorMessage(`Failed to send code: ${e}`);
  }
}
