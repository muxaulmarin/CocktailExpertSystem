from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QTableWidgetItem, QApplication, QDialog, QMainWindow, QWidget

from ES_GUI import Ui_MainWindow

from DialogDomain import Ui_Dialog as Ui_DialogDomains
from DialogVariables import Ui_Dialog as Ui_DialogVariables

from knowledge import Knowledge

class Expert_System(QMainWindow):
    def __init__(self, parent=None):

        QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.knowledge = Knowledge()

        self.ui.actionNew.triggered.connect(self.showDialogNew)
        self.ui.actionOpen.triggered.connect(self.showDialogOpen)
        self.ui.actionSave.triggered.connect(self.showDialogSaveAs)
        
        self.ui.actionDomains.triggered.connect(self.showDialogDomains)
        self.ui.actionVariables.triggered.connect(self.showDialogVariables)
        self.ui.actionViewOntology.triggered.connect(self.showDialogOntologyView)

        self.ui.actionStart.triggered.connect(self.showDialogRecommendation)

        self.ui.actionSolution.triggered.connect(self.showDialogSolution)

        self.ui.pushButton.clicked.connect(self.showDialogAddRule)

    def showDialogNew(self):
        pass

    def showDialogOpen(self):
        pass

    def showDialogSaveAs(self):
        pass

    def showDialogExit(self):
        pass

    def showDialogDomains(self):
        Window_DialogDomain = QDialog()
        ui = Ui_DialogDomains()
        ui.setupUi(Window_DialogDomain)
        rsp = Window_DialogDomain.exec_()
        if rsp == QDialog.Accepted:
            print(1)
        else:
            print(0)

    def showDialogVariables(self):
        Window_DialogVariables = QDialog()
        ui = Ui_DialogVariables()
        ui.setupUi(Window_DialogVariables)
        rsp = Window_DialogVariables.exec_()
        if rsp == QDialog.Accepted:
            print(1)
        else:
            print(0)

    def showDialogOntologyView(self):
        pass

    def showDialogRecommendation(self):
        pass

    def showDialogSolution(self):
        pass

    def showDialogAddRule(self):
        pass

    #def showDialogDomain_buttonEdit(self):
    #    n, name, values, domain_type  = self.gather_row()
    #    self.DialogDomainAdd_ui.domainType.setCurrentIndex(self.DialogDomainAdd_ui.domainType.findText(domain_type))
    #    for value in values:
    #        self.DialogDomainAdd_ui.domainList.addItem(str(value))
    #    self.DialogDomainAdd_ui.domainName.setText(name)
    #    self.DialogDomainAddWindow.show()
    #    rsp = self.DialogDomainAddWindow.exec_()
    #    if rsp == QtWidgets.QDialog.Accepted:
    #        name, values, domain_type = self.gather_domain()
    #        self.knowledge.editDomain((n, name, values, domain_type))
    #        self.update_table()
    #        self.clear_dialogAdd()
    #    else:
    #        pass
    #def gather_row(self):
    #    row = self.DialogDomain_ui.tableWidget.selectedItems()
    #    for cell in row:
    #        if cell.column() == 0:
    #            n = int(cell.text())
    #        elif cell.column() == 1:
    #            name = cell.text()
    #        elif cell.column() == 2:
    #            domain_type = cell.text()
    #        elif cell.column() == 3:
    #            values = cell.text().split(', ')
    #    if domain_type == 'Вещественный':
    #        values = [float(v) for v in values]
    #    elif domain_type == 'Целочисленный':
    #        values = [int(v) for v in values]
    #    return n, name, values, domain_type
    #def get_N(self):
    #    row = self.DialogDomain_ui.tableWidget.selectedItems()
    #    for cell in row:
    #        if cell.column() == 0:
    #            n = int(cell.text())
    #    return n
    #def showDialogDomain_buttonDelete(self):
    #    n = self.get_N()
    #    del self.knowledge.domains[n]
    #    self.update_table()
    #def showDialogDomain_buttonAdd(self):
    #    self.DialogDomainAddWindow.show()
    #    rsp = self.DialogDomainAddWindow.exec_()
    #    if rsp == QtWidgets.QDialog.Accepted:
    #        self.knowledge.addDomain(self.gather_domain())
    #        self.update_table()
    #        self.clear_dialogAdd()
    #    else:
    #        pass
    #def gather_domain(self):
    #    name = self.DialogDomainAdd_ui.domainName.text()
    #    domain_type = self.DialogDomainAdd_ui.domainType.currentText()
    #    values = self.get_values(domain_type)
    #    return (name, values, domain_type)
    #def get_values(self, domain_type):
    #    values = []
    #    for i in range(self.DialogDomainAdd_ui.domainList.count()):
    #        if domain_type == 'Строковый':
    #            values.append(str(self.DialogDomainAdd_ui.domainList.item(i).text()))
    #        elif domain_type == 'Целочисленный':
    #            values.append(int(self.DialogDomainAdd_ui.domainList.item(i).text()))
    #        else:
    #            values.append(float(self.DialogDomainAdd_ui.domainList.item(i).text()))
    #    return values
    #def update_table(self):
    #    rows = len(self.knowledge.domains)
    #    self.DialogDomain_ui.tableWidget.setRowCount(rows)
    #    for n, num in enumerate(self.knowledge.domains):
    #        name = self.knowledge.domains[num]['name']
    #        values = self.knowledge.domains[num]['values']
    #        domain_type = self.knowledge.domains[num]['type']
    #        self.DialogDomain_ui.tableWidget.setItem(n, 0, QTableWidgetItem(str(num)))
    #        self.DialogDomain_ui.tableWidget.setItem(n, 1, QTableWidgetItem(name))
    #        self.DialogDomain_ui.tableWidget.setItem(n, 2, QTableWidgetItem(domain_type))
    #        self.DialogDomain_ui.tableWidget.setItem(
    #            n, 3, QTableWidgetItem(', '.join([str(v) for v in values]))
    #            )     
    #def clear_dialogAdd(self):
    #    self.DialogDomainAdd_ui.domainName.clear()
    #    self.DialogDomainAdd_ui.domainValue.clear()
    #    self.DialogDomainAdd_ui.domainList.clear()
    #def click_DialogDomainAdd_buttonAdd(self):
    #    value = self.DialogDomainAdd_ui.domainValue.text()
    #    self.DialogDomainAdd_ui.domainList.addItem(value)
    #    self.DialogDomainAdd_ui.domainValue.setText('')
    #def click_DialogDomainAdd_buttonEdit(self):
    #    edit_item = self.DialogDomainAdd_ui.domainList.currentItem().text()
    #    items = [str(self.DialogDomainAdd_ui.domainList.item(i).text()) for i in range(self.DialogDomainAdd_ui.domainList.count())]
    #    new_value = self.DialogDomainAdd_ui.domainValue.text()
    #    self.DialogDomainAdd_ui.domainList.clear()
    #    for item in items:
    #        if edit_item == item:
    #            self.DialogDomainAdd_ui.domainList.addItem(new_value)
    #        else:
    #            self.DialogDomainAdd_ui.domainList.addItem(item)
    #    self.DialogDomainAdd_ui.domainValue.clear()
    #def click_DialogDomainAdd_buttonDelete(self):
    #    delete_item = self.DialogDomainAdd_ui.domainList.currentItem().text()
    #    items = [str(self.DialogDomainAdd_ui.domainList.item(i).text()) for i in range(self.DialogDomainAdd_ui.domainList.count())]
    #    self.DialogDomainAdd_ui.domainList.clear()
    #    for item in items:
    #        if delete_item == item:
    #            continue
    #        else:
    #            self.DialogDomainAdd_ui.domainList.addItem(item)
    #    self.DialogDomainAdd_ui.domainValue.clear()

    

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    myapp = Expert_System()
    myapp.show()
    sys.exit(app.exec_())