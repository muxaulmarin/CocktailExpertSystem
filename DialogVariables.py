from gui_py.DialogVariables import Ui_Dialog
from PyQt5.QtWidgets import QDialog, QWidget, QApplication
from knowledge import Knowledge

class DialogVariables(QDialog):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.knowledge = Knowledge()