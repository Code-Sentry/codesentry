const vscode = require('vscode');
const CodeSentryProvider = require('./views/CodeSentryProvider');
const { registerCommands } = require('./commands');

function activate(context) {
    // Registrar TreeView
    const treeDataProvider = new CodeSentryProvider();
    const view = vscode.window.createTreeView('codesentryView', {
        treeDataProvider
    });
    context.subscriptions.push(view);

    // Registrar Comandos
    registerCommands(context);
}

function deactivate() {}

module.exports = {
    activate,
    deactivate
};