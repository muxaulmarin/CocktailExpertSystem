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

    def addDomainsToComboBox(self):
        self.ui.Domains.addItems(self.knowledge.domains.keys())

    def refreshBlock(self):
        if self.ui.VarCategory.currentText() == 'Выводимая':
            self.ui.textQuestion.setReadOnly(True)
        else:
            self.ui.textQuestion.setReadOnly(False)

    def refreshDomainValues(self):
        self.ui.listWidget.clear()
        try:
            for value in self.knowledge.domains[self.ui.Domains.currentText()]:
                self.ui.listWidget.addItem(str(value))
        except KeyError:
            pass

    def click_buttonOK(self):
        domain = self.ui.Domains.currentText()
        var_name = self.ui.VarName.text()
        question = self.ui.textQuestion.toPlainText()
        category = self.ui.VarCategory.currentText()
        self.knowledge.variables[var_name] = {'domain': domain, 'category': category, 'question': question}
        return self.knowledge

    def click_buttonEdit(self):
        Window_DialoDomainAdd = DialogDomainAdd()
        Window_DialoDomainAdd.knowledge = self.knowledge
        Window_DialoDomainAdd.ui.domainName.setText(self.ui.Domains.currentText())
        Window_DialoDomainAdd.ui.domainList.addItems(self.knowledge.domains[self.ui.Domains.currentText()])
        if Window_DialoDomainAdd.exec_() == QDialog.Accepted:
            self.knowledge = Window_DialoDomainAdd.click_buttonOK()
            self.refreshDomainValues()
            
if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    myapp = DialogVariableAdd()
    myapp.show()
    sys.exit(app.exec_())