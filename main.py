from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import (QTableWidgetItem, QApplication, QDialog, 
                             QMainWindow, QWidget, QFileDialog, 
                             QMessageBox)

from gui_py.MainWindow import MainWindow

from DialogDomains import DialogDomains
from DialogVariables import DialogVariables
from DialogSaveAs import DialogSaveAs
from DialogOpen import DialogOpen
from DialogFacts import DialogFacts
from DialogRuleAdd import DialogRuleAdd
from DialogSVG import WindowSVG
from DialogRecommendation import DialogRecommendation

from knowledge import Knowledge

import os
import json
import pickle
import random

class Expert_System(QMainWindow):
    def __init__(self, parent=None):

        QWidget.__init__(self, parent)
        self.ui = MainWindow()
        self.ui.setupUi(self)

        self.knowledge = Knowledge()

        self.file = None

        self.ui.actionNew.triggered.connect(self.showDialogNew)
        self.ui.actionOpen.triggered.connect(self.showDialogOpen)
        self.ui.actionSaveAs.triggered.connect(self.showDialogSaveAs)
        self.ui.actionSave.triggered.connect(self.saveKnowledge)
        
        self.ui.actionDomains.triggered.connect(self.showDialogDomains)
        self.ui.actionVariables.triggered.connect(self.showDialogVariables)
        self.ui.actionViewOntology.triggered.connect(self.showDialogOntologyView)
        self.ui.actionFacts.triggered.connect(self.showDialogFacts)

        self.ui.actionStart.triggered.connect(self.showDialogRecommendation)

        self.ui.actionSolution.triggered.connect(self.showDialogSolution)

        self.ui.buttonAdd.clicked.connect(self.showDialogAddRule)
        self.ui.buttonEdit.clicked.connect(self.showDialogEditRule)
        self.ui.buttonDelete.clicked.connect(self.click_buttonDelete)

        self.ui.test_button.clicked.connect(self.TEST)

    def TEST(self):
        print('', '' ,
        self.knowledge.domains, 
        self.knowledge.variables, 
        self.knowledge.rules,
        sep='\n')

    def showDialogNew(self):
        qm = QMessageBox()
        ret = qm.question(self,'', "Вы уверены?", qm.Yes | qm.No)
        if ret == qm.Yes:
            self.knowledge = Knowledge()
            self.setWindowTitle('Coctail Expert System - Untitled' )
        else:
            pass

    def showDialogOpen(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        self.file = fileName
        if fileName:
            with open(fileName, 'rb') as pkl:
                knowledge_dict = pickle.load(pkl)
                self.knowledge.domains = knowledge_dict['domains']
                self.knowledge.variables = knowledge_dict['variables']
                self.knowledge.facts = knowledge_dict['facts']
                self.knowledge.rules = knowledge_dict['rules']
        self.setWindowTitle('Coctail Expert System - ' + fileName.split('/')[-1])
        self.ui.Rules.clear()
        for N in self.knowledge.rules:
            rule = self.knowledge.rules[N]['condition']
            result = self.knowledge.rules[N]['result']
            self.ui.Rules.addItem('IF ' + rule + ' THEN ' + result)

    def saveKnowledge(self):
        if self.file:
            knowledge_dict = {'domains': self.knowledge.domains, 
                              'variables': self.knowledge.variables, 
                              'facts': self.knowledge.facts, 
                              'rules': self.knowledge.rules}

            with open(self.file, 'wb') as pkl:
                pickle.dump(knowledge_dict, pkl, protocol=pickle.HIGHEST_PROTOCOL)

    def showDialogSaveAs(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            knowledge_dict = {'domains': self.knowledge.domains, 
                              'variables': self.knowledge.variables, 
                              'facts': self.knowledge.facts, 
                              'rules': self.knowledge.rules}

            with open(fileName, 'wb') as pkl:
                pickle.dump(knowledge_dict, pkl, protocol=pickle.HIGHEST_PROTOCOL)

    def showDialogExit(self):
        pass

    def showDialogDomains(self):
        Window_DialogDomains = DialogDomains()
        Window_DialogDomains.knowledge = self.knowledge
        Window_DialogDomains.RefreshView()
        if Window_DialogDomains.exec_() == QDialog.Accepted:
            self.knowledge = Window_DialogDomains.knowledge

    def showDialogVariables(self):
        Window_DialogVariables = DialogVariables()
        Window_DialogVariables.knowledge = self.knowledge
        Window_DialogVariables.RefreshView()
        if Window_DialogVariables.exec_() == QDialog.Accepted:
            self.knowledge = Window_DialogVariables.knowledge

    def showDialogFacts(self):
        Window_DialogFacts = DialogFacts()
        Window_DialogFacts.knowledge = self.knowledge
        Window_DialogFacts.RefreshVariables()
        Window_DialogFacts.RefreshView()
        if Window_DialogFacts.exec_() == QDialog.Accepted:
            self.knowledge = Window_DialogFacts.knowledge

    def showDialogOntologyView(self):
        Window_SVG = WindowSVG()
        if Window_SVG.exec_() == QDialog.Accepted:
            pass
        else:
            pass

    def showDialogRecommendation(self):
        Window_DialogRecommendation = DialogRecommendation()
        Window_DialogRecommendation.knowledge = self.knowledge
        Window_DialogRecommendation.extractQuestionAnsAnswers()
        Window_DialogRecommendation.exec_()
        print(Window_DialogRecommendation.questions)

    def showDialogSolution(self):
        pass

    def showDialogAddRule(self):
        Window_DialogRuleAdd = DialogRuleAdd()
        Window_DialogRuleAdd.knowledge = self.knowledge
        Window_DialogRuleAdd.RefreshComboBoxFacts()
        if Window_DialogRuleAdd.exec_() == QDialog.Accepted:
            Window_DialogRuleAdd.click_buttonOK()
            self.knowledge = Window_DialogRuleAdd.knowledge
            self.ui.Rules.clear()
            for N in self.knowledge.rules:
                rule = self.knowledge.rules[N]['condition']
                result = self.knowledge.rules[N]['result']
                self.ui.Rules.addItem('IF ' + rule + ' THEN ' + result)

    def showDialogEditRule(self):
        Window_DialogRuleAdd = DialogRuleAdd()
        Window_DialogRuleAdd.knowledge = self.knowledge
        Window_DialogRuleAdd.RefreshComboBoxFacts()
        N = self.get_N()
        Window_DialogRuleAdd.edit = self.ui.Rules.currentRow() + 1
        for condition in self.knowledge.rules[N]['conditions set']:
            Window_DialogRuleAdd.ui.fullCondition.addItem(condition)
        Window_DialogRuleAdd.ui.result.setText(self.knowledge.rules[N]['result'])

        if Window_DialogRuleAdd.exec_() == QDialog.Accepted:
            Window_DialogRuleAdd.click_buttonOK()
            self.knowledge = Window_DialogRuleAdd.knowledge
            self.ui.Rules.clear()
            for R in self.knowledge.rules:
                rule = self.knowledge.rules[R]['condition']
                result = self.knowledge.rules[R]['result']
                self.ui.Rules.addItem('IF ' + rule + ' THEN ' + result)

    def click_buttonDelete(self):
        N = self.ui.Rules.currentRow() + 1
        del self.knowledge.rules[N]
        self.ui.Rules.clear()
        for R in self.knowledge.rules:
            rule = self.knowledge.rules[R]['condition']
            result = self.knowledge.rules[R]['result']
            self.ui.Rules.addItem('IF ' + rule + ' THEN ' + result)

    def get_N(self):
        fullRule = self.ui.Rules.currentItem().text()
        for N in self.knowledge.rules:
            joined_conditions = 'IF ' + ' '.join(self.knowledge.rules[N]) + ' THEN ' + self.knowledge.rules[N]['result']
            if fullRule == joined_conditions:
                break
        return N

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    myapp = Expert_System()
    myapp.show()
    sys.exit(app.exec_())