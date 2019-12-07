from gui_py.DialogDomain import Ui_Dialog
from DialogDomainAdd import DialogDomainAdd
from PyQt5.QtWidgets import QDialog, QWidget, QTableWidgetItem, QApplication, QTableView
from PyQt5.QtGui import QStandardItem
from PyQt5.QtCore import Qt
from knowledge import Knowledge

class DialogDomains(QDialog):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.knowledge = Knowledge()

        self.ui.buttonAdd.clicked.connect(self.click_buttonAdd)
        self.ui.buttonEdit.clicked.connect(self.click_buttonEdit)
        self.ui.buttonDelete.clicked.connect(self.click_buttonDelete)

        self.ui.tableWidget.setColumnWidth(0, 120)
        self.ui.tableWidget.setColumnWidth(1, 280)
        self.ui.tableWidget.setSelectionBehavior(self.ui.tableWidget.SelectRows)

    def click_buttonAdd(self):
        ui = DialogDomainAdd()
        if ui.exec_() == QDialog.Accepted:
            self.knowledge.addDomain(ui.gather_domain())
            self.update_table()

    def click_buttonEdit(self):
        n = len(self.ui.tableWidget.selectedIndexes())
        if n == 0:
            pass
        else:
            name, values = self.gather_row()
            ui = DialogDomainAdd()
            for value in values:
                ui.ui.domainList.addItem(str(value))
            ui.ui.domainName.setText(name)
            if ui.exec_() == QDialog.Accepted:
                name, values = ui.gather_domain()
                self.knowledge.editDomain(name, values)
                self.update_table()

    def update_table(self):
        self.ui.tableWidget.setRowCount(0)
        for n, domain in enumerate(self.knowledge['domains']):
            self.ui.tableWidget.insertRow(n)
            self.ui.tableWidget.setItem(n, 0, QTableWidgetItem(domain))
            values = ', '.join([str(v) for v in self.knowledge['domains'][domain]])
            self.ui.tableWidget.setItem(n, 1, QTableWidgetItem(values))
        for n_row in range(self.ui.tableWidget.rowCount()):
            for n_col in range(2):
                self.ui.tableWidget.item(n_row, n_col).setFlags(Qt.ItemIsSelectable |  Qt.ItemIsEnabled)

    def gather_row(self):
        n = len(self.ui.tableWidget.selectedIndexes())
        if n == 0:
            pass
        else:
            for idx in self.ui.tableWidget.selectedIndexes():
                name = self.ui.tableWidget.item(idx.row(), 0).text()
                values = self.ui.tableWidget.item(idx.row(), 1).text()
            return name, values.split(', ')

    def click_buttonDelete(self):
        n = len(self.ui.tableWidget.selectedIndexes())
        if n == 0:
            pass
        else:
            for idx in self.ui.tableWidget.selectedIndexes():
                name = self.ui.tableWidget.item(idx.row(), 0).text()
            del self.knowledge['domains'][name]
            self.update_table()

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    myapp = DialogDomains()
    myapp.show()
    sys.exit(app.exec_())