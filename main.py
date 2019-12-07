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

        self.setWindowTitle('Coctail Expert System - Untitled' )

    def TEST(self):
        print(self.knowledge)

    def showDialogNew(self):
        self.knowledge = Knowledge()
        self.setWindowTitle('Coctail Expert System - Untitled' )

    def showDialogOpen(self):
        Window_DialogOpen = DialogOpen()
        if Window_DialogOpen.exec_() == QDialog.Accepted:
            folder = Window_DialogOpen.ui.folder.text()
            file_name = Window_DialogOpen.ui.file_name.text()
            with open(os.path.join(folder, file_name), 'rb') as pyobj:
                self.knowledge.loadKnowledge(pickle.load(pyobj))
        self.setWindowTitle('Coctail Expert System - ' + Window_DialogOpen.ui.file_name.text())

    def showDialogSaveAs(self):
        Window_DialogSaveAs = DialogSaveAs()
        if Window_DialogSaveAs.exec_() == QDialog.Accepted:
            folder = Window_DialogSaveAs.ui.folder.text()
            file_name = Window_DialogSaveAs.ui.file_name.text()
            with open(os.path.join(folder, file_name), 'wb') as pyobj:
                domains = self.knowledge['domains']
                variables = self['variables']
                nodes = self['nodes']
                edges= self['edges']
                labels = self['labels']
                pickle.dump({'domains': domains, 
                             'variables': variables, 
                             'nodes': nodes, 
                             'edges': edges, 
                             'labels': labels}, pyobj, protocol=pickle.HIGHEST_PROTOCOL)

    def showDialogExit(self):
        pass

    def showDialogDomains(self):
        Window_DialogDomains = DialogDomains()
        Window_DialogDomains.knowledge = self.knowledge
        Window_DialogDomains.update_table()
        if Window_DialogDomains.exec_() == QDialog.Accepted:
            self.knowledge.mergeDomain(Window_DialogDomains.knowledge['domains'])

    def showDialogVariables(self):
        Window_DialogVariables = DialogVariables()
        Window_DialogVariables.knowledge = self.knowledge
        Window_DialogVariables.RefreshView()
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