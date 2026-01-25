import { FlameClient } from '../client';
import * as vscode from 'vscode';

export async function connect(client: FlameClient) {
  try {
    await client.connect();
    vscode.window.showInformationMessage('Connected to Flame (dev).');
  } catch (e) {
    vscode.window.showErrorMessage(`Failed to connect: ${e}`);
  }
}
