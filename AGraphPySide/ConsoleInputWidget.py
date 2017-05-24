from PySide import QtCore, QtGui

class ConsoleInput(QtGui.QLineEdit):
    def __init__(self, parent, graph):
        super(ConsoleInput, self).__init__(parent)
        self.graph = graph
        self.returnPressed.connect(self.OnReturnPressed)
        self.model = QtGui.QStringListModel()
        self.cmd_list = ["renameNode", "setPropertiesVisible", "setNodeBoxVisible", "setConsoleVisible", "plot", "setVerticalScrollBar", "setHorizontalScrollBar", "setScrollbars", "help", "createNode", "save", "load", "comment", "killNode", "setAttr", "connectAttr", "disconectAttr", "select", "move", "pluginWizard"]
        self.executedCommands = [i for i in self.graph.registeredCommands.iterkeys()] + self.cmd_list
        self.builtinCommands = self.cmd_list
        self.completer = QtGui.QCompleter(self)
        self.model.setStringList(self.executedCommands)
        self.completer.setModel(self.model)
        self.completer.setCompletionMode(self.completer.PopupCompletion)
        self.completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.setCompleter(self.completer)
        font = QtGui.QFont("Consolas", 9, QtGui.QFont.Bold, False)
        self.setFont(font)

    def OnReturnPressed(self):
        line = self.text()
        if line not in self.executedCommands:
            self.executedCommands.append(line)
        self.model.setStringList(self.executedCommands)
        self.graph.executeCommand(line)
        self.clear()