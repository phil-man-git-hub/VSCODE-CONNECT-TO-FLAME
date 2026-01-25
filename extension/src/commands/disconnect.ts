import { FlameClient } from '../client';
import * as vscode from 'vscode';

export function disconnect(client: FlameClient) {
  client.close();
  vscode.window.showInformationMessage('Disconnected from Flame (dev).');
}
