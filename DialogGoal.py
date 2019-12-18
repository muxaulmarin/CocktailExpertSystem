from gui_py.DialogGoal import Ui_Dialog
from PyQt5.QtWidgets import QDialog, QWidget

from knowledge import Knowledge

class DialogGoal(QDialog):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.knowledge = Knowledge()

    def RefreshComboBox(self):
        for var in self.knowledge.variables:
            self.ui.comboBox.addItem(var)

    def click_buttonOK(self):
        print(self.ui.comboBox.currentText())
        return self.ui.comboBox.currentText()
