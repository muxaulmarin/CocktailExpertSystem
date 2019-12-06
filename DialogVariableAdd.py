from gui_py.DialogVariableAdd import Ui_Dialog
from PyQt5.QtWidgets import QDialog, QWidget, QApplication
from knowledge import Knowledge

class DialogDomainAdd(QDialog):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.knowledge = Knowledge()

        self.ui.testButton.clicked.connect(self.click_buttonTest)
        self.ui.Domains.currentTextChanged.connect(self.refreshDomainValues)

    def click_buttonTest(self):
        print(self.knowledge)

    def addDomainsToComboBox(self):
        for i in self.knowledge['domains']:
            self.ui.Domains.addItem(self.knowledge['domains'][i]['name'])

    def refreshDomainValues(self):
        for num_domain in self.knowledge['domains']:
            if self.knowledge['domains'][num_domain]['name'] == self.ui.Domains.currentText():
                values = self.knowledge['domains'][num_domain]['values']
        for value in values:
            self.ui.listWidget.addItem(str(value))

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    myapp = DialogDomainAdd()
    myapp.show()
    sys.exit(app.exec_())