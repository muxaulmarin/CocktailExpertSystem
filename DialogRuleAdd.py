from gui_py.DialogRuleAdd import Ui_Dialog
from PyQt5.QtWidgets import QDialog, QWidget, QApplication
from knowledge import Knowledge

class DialogRuleAdd(QDialog):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.knowledge = Knowledge()
        self.edit = None

        self.ui.buttonAdd.clicked.connect(self.click_buttonAdd)
        self.ui.buttonEdit.clicked.connect(self.click_buttonEdit)
        self.ui.buttonDelete.clicked.connect(self.click_buttonDelete)

    def click_buttonAdd(self):
        if self.ui.radioButtonFact.isChecked():
            self.ui.fullCondition.addItem(self.ui.Facts.currentText())
            self.ui.radioButtonFact.setChecked(False)
            self.ui.radioButtonCondition.setChecked(True)
        elif self.ui.radioButtonCondition.isChecked():
            self.ui.fullCondition.addItem(self.ui.condition.currentText())
            self.ui.radioButtonCondition.setChecked(False)
            self.ui.radioButtonFact.setChecked(True)
        else:
            pass

    def RefreshComboBoxFacts(self):
        for fact in self.knowledge.facts:
            row = ' '.join(self.knowledge.facts[fact].values())
            self.ui.Facts.addItem(row)

    def click_buttonOK(self):
        rule = {'condition': [], 'conditions set': []}
        for row in range(self.ui.fullCondition.count()):
            rule['condition'].append(self.ui.fullCondition.item(row).text())
            rule['conditions set'].append(self.ui.fullCondition.item(row).text())
        rule['condition'] = ' '.join(rule['condition'])
        rule['result'] = self.ui.result.text()
        if self.edit == None:
            self.knowledge.rules[len(self.knowledge.rules) + 1] = rule
        else:
            self.knowledge.rules[self.edit] = rule

    def click_buttonEdit(self):
        idx = self.ui.fullCondition.currentRow()
        items = [self.ui.fullCondition.item(i).text() for i in range(self.ui.fullCondition.count())]
        if idx % 2 != 0:
            new_item = self.ui.condition.currentText()
        else:
            new_item = self.ui.Facts.currentText()
        self.ui.fullCondition.clear()
        for n, item in enumerate(items):
            if n == idx:
                self.ui.fullCondition.addItem(new_item)
            else:
                self.ui.fullCondition.addItem(item)

    def click_buttonDelete(self):
        items = [self.ui.fullCondition.item(i).text() for i in range(self.ui.fullCondition.count())][:-1]
        self.ui.fullCondition.clear()
        for item in items:
            self.ui.fullCondition.addItem(item)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    myapp = DialogRuleAdd()
    myapp.show()
    sys.exit(app.exec_())