from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QTableWidgetItem, QApplication, QDialog, QMainWindow, QWidget

from gui_py.MainWindow import MainWindow

from DialogDomains import DialogDomains
from DialogVariables import DialogVariables

from knowledge import Knowledge

class Expert_System(QMainWindow):
    def __init__(self, parent=None):

        QWidget.__init__(self, parent)
        self.ui = MainWindow()
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

        self.ui.test_button.clicked.connect(self.TEST)

    def TEST(self):
        print(self.knowledge.domains)

    def showDialogNew(self):
        pass

    def showDialogOpen(self):
        pass

    def showDialogSaveAs(self):
        pass

    def showDialogExit(self):
        pass

    def showDialogDomains(self):
        Window_DialogDomains = DialogDomains()
        if Window_DialogDomains.exec_() == QDialog.Accepted:
            self.knowledge.mergeDomain(Window_DialogDomains.knowledge.domains)

    def showDialogVariables(self):
        Window_DialogVariables = DialogVariables()
        if Window_DialogVariables.exec_() == QDialog.Accepted:
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

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    myapp = Expert_System()
    myapp.show()
    sys.exit(app.exec_())