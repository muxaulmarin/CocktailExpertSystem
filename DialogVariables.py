from gui_py.DialogVariables import Ui_Dialog
from DialogVariableAdd import DialogVariableAdd
from PyQt5.QtWidgets import QDialog, QWidget, QApplication, QTableWidgetItem
from PyQt5.QtCore import Qt

from knowledge import Knowledge

class DialogVariables(QDialog):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.knowledge = Knowledge()

        self.ui.tableWidget.setColumnWidth(0, 120)
        self.ui.tableWidget.setColumnWidth(1, 120)
        self.ui.tableWidget.setColumnWidth(2, 190)
        self.ui.tableWidget.setSelectionBehavior(self.ui.tableWidget.SelectRows)

        self.ui.buttonAdd.clicked.connect(self.showDialogVariableAdd)
        self.ui.testButton.clicked.connect(self.click_buttonTest)
        self.ui.buttonDelete.clicked.connect(self.click_buttonDelete)
        
        self.ui.tableWidget.itemSelectionChanged.connect(self.RefreshQuestionDomainBoxes)

    def showDialogVariableAdd(self):
        Window_DialogVariableAdd = DialogVariableAdd()
        Window_DialogVariableAdd.knowledge = self.knowledge
        Window_DialogVariableAdd.addDomainsToComboBox()

        if Window_DialogVariableAdd.exec_() == QDialog.Accepted:
            self.knowledge = Window_DialogVariableAdd.click_buttonOK()
            self.RefreshView()

    def RefreshView(self):
        self.ui.tableWidget.setRowCount(0)
        for n, variable in enumerate(self.knowledge.variables):
            self.ui.tableWidget.insertRow(n)
            self.ui.tableWidget.setItem(n, 0, QTableWidgetItem(variable))
            category = self.knowledge.variables[variable]['category']
            self.ui.tableWidget.setItem(n, 1, QTableWidgetItem(category))
            domain = self.knowledge.variables[variable]['domain']
            self.ui.tableWidget.setItem(n, 2, QTableWidgetItem(domain))
        for n_row in range(self.ui.tableWidget.rowCount()):
            for n_col in range(self.ui.tableWidget.columnCount()):
                self.ui.tableWidget.item(n_row, n_col).setFlags(Qt.ItemIsSelectable |  Qt.ItemIsEnabled)

    def click_buttonTest(self):
        print(f'Domains {self.knowledge.domains}', 
        f'Variables {self.knowledge.variables}', 
        sep='\n')

    def RefreshQuestionDomainBoxes(self):
        if self.ui.tableWidget.currentIndex().row() == -1:
            self.ui.Question.clear()
        else:
            name = self.ui.tableWidget.item(self.ui.tableWidget.currentIndex().row(), 0).text()
            self.ui.Question.setText(self.knowledge.variables[name]['question'])
            domain = self.knowledge.variables[name]['domain']
            values = self.knowledge.domains[domain]
            self.ui.domainValues.addItems(values)
            self.previous_select = self.ui.tableWidget.currentRow()

    def click_buttonDelete(self):
        pass

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    myapp = DialogVariables()
    myapp.show()
    sys.exit(app.exec_())