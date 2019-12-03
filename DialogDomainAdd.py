from gui_py.DialogDomainAdd import Ui_Dialog
from PyQt5.QtWidgets import QDialog, QWidget, QApplication

class DialogDomainAdd(QDialog):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.buttonAdd.clicked.connect(self.click_buttonAdd)
        self.ui.buttonEdit.clicked.connect(self.click_buttonEdit)
        self.ui.buttonDelete.clicked.connect(self.click_buttonDelete)

    def click_buttonAdd(self):
        value = self.ui.domainValue.text()
        self.ui.domainList.addItem(value)
        self.ui.domainValue.setText('')

    def click_buttonEdit(self):
        edit_item = self.ui.domainList.currentItem().text()
        items = [str(self.ui.domainList.item(i).text()) for i in range(self.ui.domainList.count())]
        new_value = self.ui.domainValue.text()
        self.ui.domainList.clear()
        for item in items:
            if edit_item == item:
                self.ui.domainList.addItem(new_value)
            else:
                self.ui.domainList.addItem(item)
        self.ui.domainValue.clear()

    def click_buttonDelete(self):
        delete_item = self.ui.domainList.currentItem().text()
        items = [str(self.ui.domainList.item(i).text()) for i in range(self.ui.domainList.count())]
        self.ui.domainList.clear()
        for item in items:
            if delete_item == item:
                continue
            else:
                self.ui.domainList.addItem(item)
        self.ui.domainValue.clear()

    def get_values(self, domain_type):
        values = []
        for i in range(self.ui.domainList.count()):
            if domain_type == 'Строковый':
                values.append(str(self.ui.domainList.item(i).text()))
            elif domain_type == 'Целочисленный':
                values.append(int(self.ui.domainList.item(i).text()))
            else:
                values.append(float(self.ui.domainList.item(i).text()))
        return values

    def gather_domain(self):
        name = self.ui.domainName.text()
        domain_type = self.ui.domainType.currentText()
        values = self.get_values(domain_type)
        return (name, values, domain_type)


#import sys
#app = QApplication(sys.argv)
#myapp = DialogDomainAdd()
#myapp.show()
#sys.exit(app.exec_())