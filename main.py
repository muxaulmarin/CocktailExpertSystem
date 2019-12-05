from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QTableWidgetItem, QApplication, QDialog, QMainWindow, QWidget

from gui_py.MainWindow import MainWindow

from DialogDomains import DialogDomains
from DialogVariables import DialogVariables
from DialogSaveAs import DialogSaveAs
from DialogOpen import DialogOpen

from knowledge import Knowledge

import os
import json

class Expert_System(QMainWindow):
    def __init__(self, parent=None):

        QWidget.__init__(self, parent)
        self.ui = MainWindow()
        self.ui.setupUi(self)

        self.knowledge = Knowledge()

        self.ui.actionNew.triggered.connect(self.showDialogNew)
        self.ui.actionOpen.triggered.connect(self.showDialogOpen)
        self.ui.actionSave.triggered.connect(self.showDialogSaveAs)
        
        self.ui.actionDomains.triggered.connect(self.showDialogDomains) #FULL
        self.ui.actionVariables.triggered.connect(self.showDialogVariables)
        self.ui.actionViewOntology.triggered.connect(self.showDialogOntologyView)

        self.ui.actionStart.triggered.connect(self.showDialogRecommendation)

        self.ui.actionSolution.triggered.connect(self.showDialogSolution)

        self.ui.pushButton.clicked.connect(self.showDialogAddRule)

        self.ui.test_button.clicked.connect(self.TEST)

    def TEST(self):
        print(self.knowledge)

    def showDialogNew(self):
        self.knowledge = Knowledge()

    def showDialogOpen(self):
        Window_DialogOpen = DialogOpen()
        if Window_DialogOpen.exec_() == QDialog.Accepted:
            folder = Window_DialogOpen.ui.folder.text()
            file_name = Window_DialogOpen.ui.file_name.text() + '.json'
            with open(os.path.join(folder, file_name), 'r') as json_file:
                json_file = json.load(json_file)
                self.knowledge.loadKnowledge(json_file)

    def showDialogSaveAs(self):
        Window_DialogSaveAs = DialogSaveAs()
        if Window_DialogSaveAs.exec_() == QDialog.Accepted:
            folder = Window_DialogSaveAs.ui.folder.text()
            file_name = Window_DialogSaveAs.ui.file_name.text() + '.json'
            with open(os.path.join(folder, file_name), 'w') as json_file:
                json.dump(self.knowledge, json_file)

    def showDialogExit(self):
        pass

    def showDialogDomains(self):
        Window_DialogDomains = DialogDomains()
        if Window_DialogDomains.exec_() == QDialog.Accepted:
            self.knowledge.mergeDomain(Window_DialogDomains.knowledge['domains'])

    def showDialogVariables(self):
        Window_DialogVariables = DialogVariables()
        Window_DialogVariables.knowledge['variables'] = self.knowledge['variables']
        
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