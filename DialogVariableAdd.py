from gui_py.DialogVariableAdd import Ui_Dialog
from PyQt5.QtWidgets import QDialog, QWidget, QApplication
from knowledge import Knowledge
from DialogDomainAdd import DialogDomainAdd

class DialogVariableAdd(QDialog):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.knowledge = Knowledge()

        self.ui.Domains.currentTextChanged.connect(self.refreshDomainValues)
        self.ui.VarCategory.currentTextChanged.connect(self.refreshBlock)
        self.ui.textQuestion.setReadOnly(True)

        self.ui.buttonEdit.clicked.connect(self.click_buttonEdit)
        self.ui.buttonDelete.clicked.connect(self.click_buttonDelete)

    def addDomainsToComboBox(self):
        self.ui.Domains.addItems(self.knowledge['domains'].keys())

    def refreshBlock(self):
        if self.ui.VarCategory.currentText() == 'Выводимая':
            self.ui.textQuestion.setReadOnly(True)
        else:
            self.ui.textQuestion.setReadOnly(False)

    def refreshDomainValues(self):
        self.ui.listWidget.clear()
        for value in self.knowledge['domains'][self.ui.Domains.currentText()]:
            self.ui.listWidget.addItem(str(value))

    def gather_variable(self):
        domain = self.ui.Domains.currentText()
        values = self.knowledge['domains'][domain]
        var_name = self.ui.VarName.text()
        question = self.ui.textQuestion.toPlainText()
        return domain, values, var_name, question

    def click_buttonEdit(self):
        name = self.ui.Domains.currentText()
        values = self.knowledge['domains'][name]
        ui = DialogDomainAdd()
        ui.ui.domainName.setText(name)
        ui.ui.domainList.addItems(values)
        if ui.exec_() == QDialog.Accepted:
            self.knowledge['domains'][name] = [str(ui.ui.domainList.item(i).text()) for i in range(ui.ui.domainList.count())]
            self.refreshDomainValues()
        else:
            pass

    def click_buttonDelete(self):
        pass


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    myapp = DialogVariableAdd()
    myapp.show()
    sys.exit(app.exec_())