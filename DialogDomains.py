from gui_py.DialogDomain import Ui_Dialog
from DialogDomainAdd import DialogDomainAdd
from PyQt5.QtWidgets import QDialog, QWidget, QApplication
from knowledge import Knowledge

class DialogDomain(QDialog):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.knowledge = Knowledge()

        self.ui.buttonAdd.clicked.connect(self.click_buttonAdd)
        self.ui.buttonEdit.clicked.connect(self.click_buttonEdit)
        self.ui.buttonDelete.clicked.connect(self.click_buttonDelete)

    def click_buttonAdd(self):
        ui = DialogDomainAdd()
        if ui.exec_() == QDialog.Accepted:
            self.knowledge.addDomain(ui.gather_domain())
            print(self.knowledge.domains)

    def click_buttonEdit(self):
        pass

    def click_buttonDelete(self):
        pass

    
import sys
app = QApplication(sys.argv)
myapp = DialogDomain()
myapp.show()
sys.exit(app.exec_())