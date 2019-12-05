from gui_py.DialogVariableAdd import Ui_Dialog
from PyQt5.QtWidgets import QDialog, QWidget, QApplication

class DialogDomainAdd(QDialog):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    myapp = DialogDomainAdd()
    myapp.show()
    sys.exit(app.exec_())