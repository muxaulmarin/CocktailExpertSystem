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
import pickle

class Expert_System(QMainWindow):
    def __init__(self, parent=None):

        QWidget.__init__(self, parent)
        self.ui = MainWindow()
        self.ui.setupUi(self)

        self.knowledge = Knowledge()

        for i in range(1, 11):
            self.knowledge.domains[str(i)] = [str(j) for j in range(i, i+5)]

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

        self.setWindowTitle('Coctail Expert System - Untitled' )

    def TEST(self):
        print(f'Domains {self.knowledge.domains}', 
        f'Variables {self.knowledge.variables}', 
        sep='\n')

    def showDialogNew(self):
        # Clearing Knowledge...
        self.knowledge = Knowledge()
        self.setWindowTitle('Coctail Expert System - Untitled' )

    def showDialogOpen(self):
        # Work with pickled PyObjects
        Window_DialogOpen = DialogOpen()
        if Window_DialogOpen.exec_() == QDialog.Accepted:
            folder = Window_DialogOpen.ui.folder.text()
            file_name = Window_DialogOpen.ui.file_name.text()
            with open(os.path.join(folder, file_name), 'rb') as pyobj:
                self.knowledge = pickle.load(pyobj)
        self.setWindowTitle('Coctail Expert System - ' + Window_DialogOpen.ui.file_name.text())

    def showDialogSaveAs(self):
        # Work with pickled PyObjects
        Window_DialogSaveAs = DialogSaveAs()
        if Window_DialogSaveAs.exec_() == QDialog.Accepted:
            folder = Window_DialogSaveAs.ui.folder.text()
            file_name = Window_DialogSaveAs.ui.file_name.text() + '.obj'
            with open(os.path.join(folder, file_name), 'wb') as pyobj:
                pickle.dump(self.knowledge, pyobj, protocol=pickle.HIGHEST_PROTOCOL)

    def showDialogExit(self):
        pass

    def showDialogDomains(self):
        # Open Dialog Window for knowledge.domains
        Window_DialogDomains = DialogDomains()
        Window_DialogDomains.knowledge = self.knowledge
        Window_DialogDomains.RefreshView()
        if Window_DialogDomains.exec_() == QDialog.Accepted:
            # Rewriting knowledge
            self.knowledge = Window_DialogDomains.knowledge

    def showDialogVariables(self):
        Window_DialogVariables = DialogVariables()
        Window_DialogVariables.knowledge = self.knowledge
        Window_DialogVariables.RefreshView()
        if Window_DialogVariables.exec_() == QDialog.Accepted:
            self.knowledge = Window_DialogVariables.knowledge

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