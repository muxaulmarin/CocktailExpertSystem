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

    def showDialogVariableAdd(self):
        Window_DialogVariableAdd = DialogVariableAdd()
        Window_DialogVariableAdd.knowledge = self.knowledge
        Window_DialogVariableAdd.addDomainsToComboBox()

        if Window_DialogVariableAdd.exec_() == QDialog.Accepted:
            print(1)
        else:
            print(0)

    def RefreshView(self):
        self.ui.tableWidget.setRowCount(0)
        for n, variable in enumerate(self.knowledge['variables']):
            self.ui.tableWidget.insertRow(n)
            self.ui.tableWidget.setItem(n, 0, QTableWidgetItem(variable))
            category = self.knowledge['variables'][variable]['var_category']
            self.ui.tableWidget.setItem(n, 1, QTableWidgetItem(category))
            self.ui.tableWidget.setItem(n, 2, QTableWidgetItem('domain'))
        for n_row in range(self.ui.tableWidget.rowCount()):
            for n_col in range(self.ui.tableWidget.columnCount()):
                self.ui.tableWidget.item(n_row, n_col).setFlags(Qt.ItemIsSelectable |  Qt.ItemIsEnabled)


    def click_buttonTest(self):
        print(self.knowledge)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    myapp = DialogVariables()
    myapp.show()
    sys.exit(app.exec_())