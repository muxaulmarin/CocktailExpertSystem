from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from ES_GUI import Ui_MainWindow
from DialogDomain import Ui_Dialog as Ui_DialogDomains
from DialogDomainAdd import Ui_Dialog as Ui_DialogDomainsAdd

class Knowledge(dict):
    def __init__(self):
        self.domains = {}
        self.domain_types = {"<class 'str'>": 'Строковый', "<class 'int'>": ['Бинарный', 'Целочисленный'], "<class 'float'>": 'Дробный'}
    
    def addDomain(self, domain):
        name, values, domain_type = domain
        max_N = len(list(self.domains.keys()))
        self.domains[max_N] = {'name': name, 'values': values, 'type': domain_type}

    def editDomain(self, editDomain):
        N, name, values, domain_type = editDomain
        self.domains[N] = {'name': name, 'values': values, 'type': domain_type}

class Expert_System(QtWidgets.QMainWindow):
    def __init__(self, parent=None):

        # Главное окно приложения
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Диалоговое окно для добавления доменов
        self.DialogDomainWindow = QtWidgets.QDialog()
        self.DialogDomain_ui = Ui_DialogDomains()
        self.DialogDomain_ui.setupUi(self.DialogDomainWindow)
        self.DialogDomain_ui.buttonAdd.clicked.connect(self.showDialogDomain_buttonAdd)
        self.DialogDomain_ui.buttonEdit.clicked.connect(self.showDialogDomain_buttonEdit)
        self.DialogDomain_ui.buttonDelete.clicked.connect(self.showDialogDomain_buttonDelete)

        self.DialogDomainAddWindow = QtWidgets.QDialog()
        self.DialogDomainAdd_ui = Ui_DialogDomainsAdd()
        self.DialogDomainAdd_ui.setupUi(self.DialogDomainAddWindow)
        self.DialogDomainAdd_ui.buttonAdd.clicked.connect(self.click_DialogDomainAdd_buttonAdd)
        self.DialogDomainAdd_ui.buttonEdit.clicked.connect(self.click_DialogDomainAdd_buttonEdit)
        self.DialogDomainAdd_ui.buttonDelete.clicked.connect(self.click_DialogDomainAdd_buttonDelete)


        # База знаний
        self.knowledge = Knowledge()

        self.ui.actionNew.triggered.connect(self.showDialogNew)
        self.ui.actionOpen.triggered.connect(self.showDialogOpen)
        self.ui.actionSave.triggered.connect(self.showDialogSaveAs)
        
        self.ui.actionVariables.triggered.connect(self.showDialogVariables)
        self.ui.actionDomains.triggered.connect(self.showDialogDomains)
        self.ui.actionViewOntology.triggered.connect(self.showDialogOntologyView)

        self.ui.actionStart.triggered.connect(self.showDialogRecommendation)

        self.ui.actionSolution.triggered.connect(self.showDialogSolution)

        #self.ui.pushButton.clicked.connect(self.addRules)

    def showDialogNew(self):
        pass

    def showDialogOpen(self):
        pass

    def showDialogSaveAs(self):
        pass

    def showDialogExit(self):
        pass



    def showDialogDomains(self):
        self.DialogDomainWindow.show()
        rsp = self.DialogDomainWindow.exec_()
        if rsp == QtWidgets.QDialog.Accepted:
            print(1)
        else:
            print(0)
    def showDialogDomain_buttonEdit(self):
        n, name, values, domain_type  = self.gather_row()
        self.DialogDomainAdd_ui.domainType.setCurrentIndex(self.DialogDomainAdd_ui.domainType.findText(domain_type))
        for value in values:
            self.DialogDomainAdd_ui.domainList.addItem(str(value))
        self.DialogDomainAdd_ui.domainName.setText(name)
        self.DialogDomainAddWindow.show()
        rsp = self.DialogDomainAddWindow.exec_()
        if rsp == QtWidgets.QDialog.Accepted:
            name, values, domain_type = self.gather_domain()
            self.knowledge.editDomain((n, name, values, domain_type))
            self.update_table()
            self.clear_dialogAdd()
        else:
            pass
    def gather_row(self):
        row = self.DialogDomain_ui.tableWidget.selectedItems()
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
    def get_N(self):
        row = self.DialogDomain_ui.tableWidget.selectedItems()
        for cell in row:
            if cell.column() == 0:
                n = int(cell.text())
        return n
    def showDialogDomain_buttonDelete(self):
        n = self.get_N()
        del self.knowledge.domains[n]
        self.update_table()
    def showDialogDomain_buttonAdd(self):
        self.DialogDomainAddWindow.show()
        rsp = self.DialogDomainAddWindow.exec_()
        if rsp == QtWidgets.QDialog.Accepted:
            self.knowledge.addDomain(self.gather_domain())
            self.update_table()
            self.clear_dialogAdd()
        else:
            pass
    def gather_domain(self):
        name = self.DialogDomainAdd_ui.domainName.text()
        domain_type = self.DialogDomainAdd_ui.domainType.currentText()
        values = self.get_values(domain_type)
        return (name, values, domain_type)
    def get_values(self, domain_type):
        values = []
        for i in range(self.DialogDomainAdd_ui.domainList.count()):
            if domain_type == 'Строковый':
                values.append(str(self.DialogDomainAdd_ui.domainList.item(i).text()))
            elif domain_type == 'Целочисленный':
                values.append(int(self.DialogDomainAdd_ui.domainList.item(i).text()))
            else:
                values.append(float(self.DialogDomainAdd_ui.domainList.item(i).text()))
        return values
    def update_table(self):
        rows = len(self.knowledge.domains)
        self.DialogDomain_ui.tableWidget.setRowCount(rows)
        for n, num in enumerate(self.knowledge.domains):
            name = self.knowledge.domains[num]['name']
            values = self.knowledge.domains[num]['values']
            domain_type = self.knowledge.domains[num]['type']
            self.DialogDomain_ui.tableWidget.setItem(n, 0, QTableWidgetItem(str(num)))
            self.DialogDomain_ui.tableWidget.setItem(n, 1, QTableWidgetItem(name))
            self.DialogDomain_ui.tableWidget.setItem(n, 2, QTableWidgetItem(domain_type))
            self.DialogDomain_ui.tableWidget.setItem(
                n, 3, QTableWidgetItem(', '.join([str(v) for v in values]))
                )     
    def clear_dialogAdd(self):
        self.DialogDomainAdd_ui.domainName.clear()
        self.DialogDomainAdd_ui.domainValue.clear()
        self.DialogDomainAdd_ui.domainList.clear()
    def click_DialogDomainAdd_buttonAdd(self):
        value = self.DialogDomainAdd_ui.domainValue.text()
        self.DialogDomainAdd_ui.domainList.addItem(value)
        self.DialogDomainAdd_ui.domainValue.setText('')
    def click_DialogDomainAdd_buttonEdit(self):
        edit_item = self.DialogDomainAdd_ui.domainList.currentItem().text()
        items = [str(self.DialogDomainAdd_ui.domainList.item(i).text()) for i in range(self.DialogDomainAdd_ui.domainList.count())]
        new_value = self.DialogDomainAdd_ui.domainValue.text()
        self.DialogDomainAdd_ui.domainList.clear()
        for item in items:
            if edit_item == item:
                self.DialogDomainAdd_ui.domainList.addItem(new_value)
            else:
                self.DialogDomainAdd_ui.domainList.addItem(item)
        self.DialogDomainAdd_ui.domainValue.clear()
    def click_DialogDomainAdd_buttonDelete(self):
        delete_item = self.DialogDomainAdd_ui.domainList.currentItem().text()
        items = [str(self.DialogDomainAdd_ui.domainList.item(i).text()) for i in range(self.DialogDomainAdd_ui.domainList.count())]
        self.DialogDomainAdd_ui.domainList.clear()
        for item in items:
            if delete_item == item:
                continue
            else:
                self.DialogDomainAdd_ui.domainList.addItem(item)
        self.DialogDomainAdd_ui.domainValue.clear()

    def showDialogVariables(self):
        pass

    def showDialogOntologyView(self):
        pass

    def showDialogRecommendation(self):
        pass

    def showDialogSolution(self):
        pass

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    myapp = Expert_System()
    myapp.show()
    sys.exit(app.exec_())