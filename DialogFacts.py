from gui_py.DialogFacts import Ui_Dialog
from PyQt5.QtWidgets import QDialog, QWidget, QApplication, QTableWidgetItem, QAbstractItemView
from PyQt5.QtCore import Qt
from knowledge import Knowledge

class DialogFacts(QDialog):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.knowledge = Knowledge()

        self.ui.tableWidget.setColumnWidth(0, 135)
        self.ui.tableWidget.setColumnWidth(1, 60)
        self.ui.tableWidget.setColumnWidth(2, 135)
        self.ui.tableWidget.setSelectionBehavior(self.ui.tableWidget.SelectRows)
        self.ui.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)

        self.ui.variables.currentTextChanged.connect(self.RefreshValues)
        self.ui.buttonAdd.clicked.connect(self.click_buttonAdd)
        self.ui.buttonEdit.clicked.connect(self.click_buttonEdit)
        self.ui.buttonDelete.clicked.connect(self.click_buttonDelete)
        
    def RefreshVariables(self):
        self.ui.variables.addItems(self.knowledge.variables.keys())

    def RefreshValues(self):
        var_name = self.ui.variables.currentText()
        domain = self.knowledge.variables[var_name]['domain']
        values = self.knowledge.domains[domain]
        self.ui.values.clear()
        self.ui.values.addItems(values)

    def click_buttonAdd(self):
        var_name = self.ui.variables.currentText()
        condition = self.ui.condition.currentText()
        value = self.ui.values.currentText()
        N = str(len(self.knowledge.facts) + 1)
        self.knowledge.facts[N] = {'variable': var_name, 'condition': condition, 'value': value}
        self.RefreshView()
        print(len(self.knowledge.facts))

    def click_buttonEdit(self):
        if len(self.ui.tableWidget.selectedIndexes()) == 0:
            pass
        else:
            idx = self.ui.tableWidget.selectedIndexes()[0].row()
            var_name = self.ui.tableWidget.item(idx, 0).text()
            condition = self.ui.tableWidget.item(idx, 1).text()
            value = self.ui.tableWidget.item(idx, 2).text()
            for fact_N in self.knowledge.facts:
                t_var_name = self.knowledge.facts[fact_N]['variable']
                t_condition = self.knowledge.facts[fact_N]['condition']
                t_value = self.knowledge.facts[fact_N]['value']
                if var_name == t_var_name and condition == t_condition and value == t_value:
                    var_name = self.ui.variables.currentText()
                    condition = self.ui.condition.currentText()
                    value = self.ui.values.currentText()
                    self.knowledge.facts[fact_N] = {'variable': var_name, 'condition': condition, 'value': value}
            self.RefreshView()

    def click_buttonDelete(self):
        if len(self.ui.tableWidget.selectedIndexes()) == 0:
            pass
        else:
            idx = self.ui.tableWidget.selectedIndexes()[0].row()
            var_name = self.ui.tableWidget.item(idx, 0).text()
            condition = self.ui.tableWidget.item(idx, 1).text()
            value = self.ui.tableWidget.item(idx, 2).text()
            for fact_N in self.knowledge.facts:
                t_var_name = self.knowledge.facts[fact_N]['variable']
                t_condition = self.knowledge.facts[fact_N]['condition']
                t_value = self.knowledge.facts[fact_N]['value']
                if var_name == t_var_name and condition == t_condition and value == t_value:
                    break
            del self.knowledge.facts[fact_N]
            self.RefreshView()

    def RefreshView(self):
        self.ui.tableWidget.setRowCount(0)
        for n, fact_N in enumerate(self.knowledge.facts):
            self.ui.tableWidget.insertRow(n)
            var_name = self.knowledge.facts[fact_N]['variable']
            condition = self.knowledge.facts[fact_N]['condition']
            value = self.knowledge.facts[fact_N]['value']
            self.ui.tableWidget.setItem(n, 0, QTableWidgetItem(var_name))
            self.ui.tableWidget.setItem(n, 1, QTableWidgetItem(condition))
            self.ui.tableWidget.setItem(n, 2, QTableWidgetItem(value))
        for n_row in range(self.ui.tableWidget.rowCount()):
            for n_col in range(3):
                self.ui.tableWidget.item(n_row, n_col).setFlags(Qt.ItemIsSelectable |  Qt.ItemIsEnabled)
        self.ui.tableWidget.resizeRowsToContents()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    myapp = DialogFacts()
    myapp.show()
    sys.exit(app.exec_())