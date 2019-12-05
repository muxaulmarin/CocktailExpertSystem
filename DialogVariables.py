from gui_py.DialogVariables import Ui_Dialog
from DialogVariableAdd import DialogDomainAdd
from PyQt5.QtWidgets import QDialog, QWidget, QApplication
from knowledge import Knowledge

class DialogVariables(QDialog):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.knowledge = Knowledge()

        self.ui.buttonAdd.clicked.connect(self.showDialogVariableAdd)

    def showDialogVariableAdd(self):
        Window_DialogVariableAdd = DialogDomainAdd()
        if Window_DialogVariableAdd.exec_() == QDialog.Accepted:
            print(1)
        else:
            print(0)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    myapp = DialogVariables()
    myapp.show()
    sys.exit(app.exec_())