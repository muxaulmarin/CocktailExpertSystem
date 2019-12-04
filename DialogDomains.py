from gui_py.DialogDomain import Ui_Dialog
from DialogDomainAdd import DialogDomainAdd
from PyQt5.QtWidgets import QDialog, QWidget, QApplication, QTableWidgetItem
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

    def click_buttonAdd(self):
        ui = DialogDomainAdd()
        if ui.exec_() == QDialog.Accepted:
            self.knowledge.addDomain(ui.gather_domain())
            self.update_table()
            print(self.knowledge.domains)

    def click_buttonEdit(self):
        n, name, values, domain_type  = self.gather_row()
        ui = DialogDomainAdd()
        ui.ui.domainType.setCurrentIndex(ui.ui.domainType.findText(domain_type))
        for value in values:
            ui.ui.domainList.addItem(str(value))
        ui.ui.domainName.setText(name)
        if ui.exec_() == QDialog.Accepted:
            name, values, domain_type = ui.gather_domain()
            self.knowledge.editDomain((n, name, values, domain_type))
            self.update_table()

    def update_table(self):
        n_rows = len(self.knowledge.domains)
        self.ui.tableWidget.setRowCount(n_rows)
        for n, num in enumerate(self.knowledge.domains):
            name = self.knowledge.domains[num]['name']
            values = self.knowledge.domains[num]['values']
            domain_type = self.knowledge.domains[num]['type']
            self.ui.tableWidget.setItem(n, 0, QTableWidgetItem(str(num)))
            self.ui.tableWidget.setItem(n, 1, QTableWidgetItem(name))
            self.ui.tableWidget.setItem(n, 2, QTableWidgetItem(domain_type))
            self.ui.tableWidget.setItem(
                n, 3, QTableWidgetItem(', '.join([str(v) for v in values]))
                )

    def gather_row(self):
        row = self.ui.tableWidget.selectedItems()
        for cell in row:
            if cell.column() == 0:
                n = int(cell.text())
            elif cell.column() == 1:
                name = cell.text()
            elif cell.column() == 2:
                domain_type = cell.text()
            elif cell.column() == 3:
                values = cell.text().split(', ')
        if domain_type == 'Вещественный':
            values = [float(v) for v in values]
        elif domain_type == 'Целочисленный':
            values = [int(v) for v in values]
        return n, name, values, domain_type

    def click_buttonDelete(self):
        row = self.ui.tableWidget.selectedItems()
        for cell in row:
            if cell.column() == 0:
                n = int(cell.text())
        del self.knowledge.domains[n]
        self.update_table()