from PyQt5 import QtCore, QtGui, QtWidgets
from ES_GUI import Ui_MainWindow
from DialogDomain import Ui_Dialog as Ui_DialogDomains
from DialogDomainAdd import Ui_Dialog as Ui_DialogDomainsAdd

class Knowledge(dict):
    def __init__(self):
        self.domains = {}
        self.domain_types = {"<class 'str'>": 'Строковый', "<class 'int'>": ['Бинарный', 'Целочисленный'], "<class 'float'>": 'Дробный'}
    
    def addDomain(self, domain):
        name, values, domain_type = domain
        self.domains.update({'name': values, 'type': domain_type})

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
        self.DialogDomain_ui.buttonAdd.clicked.connect(self.showDialogDomainAdd)
        #self.DialogDomain_ui.buttonEdit.clicked.connect(self.showDialogDomainEdit)
        #self.DialogDomain_ui.buttonDelete.clicked.connect(self.showDialogDomainDelete)

        # Диалоговое окно для добавления доменов после кнопки ДОБАВИТЬ
        self.DialogDomainAddWindow = QtWidgets.QDialog()
        self.DialogDomainAdd_ui = Ui_DialogDomainsAdd()
        self.DialogDomainAdd_ui.setupUi(self.DialogDomainAddWindow)
        
        # Диалоговое окно для редактирования доменов после кнопки РЕДАКТИРОВАТЬ
        # Диалоговое окно для удаления доменов после кнопки УДАЛИТЬ


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

    def showDialogDomainAdd(self):
        self.DialogDomainAddWindow.show()
        rsp = self.DialogDomainAddWindow.exec_()
        if rsp == QtWidgets.QDialog.Accepted:
            print(1)
        else:
            print(0)

    def showDialogVariables(self):
        pass

    def showDialogOntologyView(self):
        pass

    def showDialogRecommendation(self):
        pass

    def showDialogSolution(self):
        pass

class DialogDomain(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = Ui_DialogDomains()
        self.ui.setupUi(Ui_DialogDomains)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    myapp = Expert_System()
    myapp.show()
    sys.exit(app.exec_())