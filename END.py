from gui_py.End import Ui_Dialog
from PyQt5.QtWidgets import QDialog, QWidget, QApplication, QTableWidgetItem, QAbstractItemView, QDialogButtonBox

from knowledge import Knowledge

class End(QDialog):
    def __init__(self, answer, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.button(QDialogButtonBox.Ok).setText('Спасибо!')
        self.ui.buttonBox.button(QDialogButtonBox.Cancel).setText('Большое спасибо')
        self.ui.label.setText(answer)