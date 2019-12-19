from gui_py.DialogSolution import Ui_Dialog
from PyQt5.QtWidgets import QDialog, QWidget, QApplication, QTableWidgetItem, QAbstractItemView, QDialogButtonBox


class DialogSolution(QDialog):
    def __init__(self, log, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.log = log
        self.addLogs()

    def addLogs(self):
        for row in self.log:
            self.ui.listWidget.addItem(' '.join(row))