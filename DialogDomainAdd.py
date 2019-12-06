from gui_py.DialogDomainAdd_v2 import Ui_dialog
from PyQt5.QtWidgets import QDialog, QWidget, QApplication

class DialogDomainAdd(QDialog):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_dialog()
        self.ui.setupUi(self)

        self.ui.domainName.setPlaceholderText('Имя домена')

        self.ui.buttonAdd.clicked.connect(self.click_buttonAdd)
        self.ui.buttonEdit.clicked.connect(self.click_buttonEdit)
        self.ui.buttonDelete.clicked.connect(self.click_buttonDelete)

    def click_buttonAdd(self):
        if self.ui.domainValue.text() == '':
            pass
        else:
            self.ui.domainList.addItem(self.ui.domainValue.text())
            self.ui.domainValue.clear()

    def click_buttonEdit(self):
        edit_item = self.ui.domainList.currentItem().text()
        items = [str(self.ui.domainList.item(i).text()) for i in range(self.ui.domainList.count())]
        new_value = self.ui.domainValue.text()
        if new_value == '':
            pass
        else:
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

    def get_values(self):
        values = [str(self.ui.domainList.item(i).text()) for i in range(self.ui.domainList.count())]
        return values

    def gather_domain(self):
        name = self.ui.domainName.text()
        values = self.get_values()
        return name, values

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    myapp = DialogDomainAdd()
    myapp.show()
    sys.exit(app.exec_())