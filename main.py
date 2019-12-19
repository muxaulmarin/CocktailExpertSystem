from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import (QTableWidgetItem, QApplication, QDialog, 
                             QMainWindow, QWidget, QFileDialog, 
                             QMessageBox, QAbstractItemView)

from gui_py.MainWindow import Ui_MainWindow

from DialogDomains import DialogDomains
from DialogVariables import DialogVariables
from DialogSaveAs import DialogSaveAs
from DialogOpen import DialogOpen
from DialogFacts import DialogFacts
from DialogRuleAdd import DialogRuleAdd
from DialogSVG import WindowSVG
from DialogRecommendation import DialogRecommendation
from DialogGoal import DialogGoal
from DialogSolution import DialogSolution

from knowledge import Knowledge
from MLV import MLV

import os
import json
import pickle
import random

class Expert_System(QMainWindow):
    def __init__(self, parent=None):

        QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.knowledge = Knowledge()

        self.file = None
        self.goal = None
        self.log = None

        self.setWindowTitle('Экспертная система')

        self.ui.actionNew.triggered.connect(self.showDialogNew)
        self.ui.actionOpen.triggered.connect(self.showDialogOpen)
        self.ui.actionSaveAs.triggered.connect(self.showDialogSaveAs)
        self.ui.actionSave.triggered.connect(self.saveKnowledge)
        
        self.ui.actionDomains.triggered.connect(self.showDialogDomains)
        self.ui.actionVariables.triggered.connect(self.showDialogVariables)
        self.ui.actionViewOntology.triggered.connect(self.showDialogOntologyView)
        self.ui.actionFacts.triggered.connect(self.showDialogFacts)

        self.ui.actionStart.triggered.connect(self.showDialogRecommendation)
        self.ui.action.triggered.connect(self.showDialogGoal)

        self.ui.actionSolution.triggered.connect(self.showDialogSolution)

        self.ui.buttonAdd.clicked.connect(self.showDialogAddRule)
        self.ui.buttonEdit.clicked.connect(self.showDialogEditRule)
        self.ui.buttonDelete.clicked.connect(self.click_buttonDelete)

        self.ui.Rules.setDragDropMode(QAbstractItemView.InternalMove)

    def showDialogNew(self):
        qm = QMessageBox()
        qm.setWindowTitle('Создать новую базу знаний')
        ret = qm.question(self,'', "Вы уверены?", qm.Yes | qm.No)
        if ret == qm.Yes:
            self.knowledge = Knowledge()
            self.setWindowTitle('Экспертная система - БезНазвания' )
        else:
            pass

    def showDialogOpen(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","JSON Files (*.json);;Pickle Files (*.obj)", options=options)
        self.file = fileName
        if fileName.endswith('.obj'):
            with open(fileName, 'rb') as pkl:
                knowledge_dict = pickle.load(pkl)
                self.knowledge.domains = knowledge_dict['domains']
                self.knowledge.variables = knowledge_dict['variables']
                self.knowledge.facts = knowledge_dict['facts']
                self.knowledge.rules = knowledge_dict['rules']
            self.setWindowTitle('Экспертная система - ' + fileName.split('/')[-1])
            self.ui.Rules.clear()
            for num, N in enumerate(self.knowledge.rules):
                rule = self.knowledge.rules[N]['condition']
                result = self.knowledge.rules[N]['result']
                self.ui.Rules.addItem(f'{num} -- IF ' + rule + ' THEN ' + result)
        elif fileName.endswith('.json'):
            with open(fileName, 'r') as jsonfile:
                knowledge_dict = json.load(jsonfile)
                self.knowledge.domains = knowledge_dict['domains']
                self.knowledge.variables = knowledge_dict['variables']
                self.knowledge.facts = knowledge_dict['facts']
                self.knowledge.rules = knowledge_dict['rules']
            self.setWindowTitle('Экспертная система - ' + fileName.split('/')[-1])
            self.ui.Rules.clear()
            for num, N in enumerate(self.knowledge.rules):
                rule = self.knowledge.rules[N]['condition']
                result = self.knowledge.rules[N]['result']
                self.ui.Rules.addItem(f'{num} -- IF ' + rule + ' THEN ' + result)

    def saveKnowledge(self):
        if self.file == None:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
            if fileName:
                knowledge_dict = {'domains': self.knowledge.domains, 
                                  'variables': self.knowledge.variables, 
                                  'facts': self.knowledge.facts, 
                                  'rules': self.knowledge.rules}

                with open(fileName + '.obj', 'wb') as pkl:
                    pickle.dump(knowledge_dict, pkl, protocol=pickle.HIGHEST_PROTOCOL)
            self.file = fileName
            self.setWindowTitle('Экспертная система - ' + fileName.split('/')[-1])

        else:
            if self.file.endswith('.obj'):
                knowledge_dict = {'domains': self.knowledge.domains, 
                                  'variables': self.knowledge.variables, 
                                  'facts': self.knowledge.facts, 
                                  'rules': self.knowledge.rules}

                with open(self.file, 'wb') as pkl:
                    pickle.dump(knowledge_dict, pkl, protocol=pickle.HIGHEST_PROTOCOL)
            else:
                knowledge_dict = {'domains': self.knowledge.domains, 
                                  'variables': self.knowledge.variables, 
                                  'facts': self.knowledge.facts, 
                                  'rules': self.knowledge.rules}

                with open(self.file, 'w') as jsonfile:
                    json.dump(knowledge_dict, jsonfile)

    def showDialogSaveAs(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            knowledge_dict = {'domains': self.knowledge.domains, 
                              'variables': self.knowledge.variables, 
                              'facts': self.knowledge.facts, 
                              'rules': self.knowledge.rules}

            with open(fileName + '.obj', 'wb') as pkl:
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
        if self.file:
            Window_SVG = WindowSVG()
            if Window_SVG.exec_() == QDialog.Accepted:
                pass
            else:
                pass
        else:
            qm = QMessageBox()
            qm.setWindowTitle('Нет БЗ')
            ret = qm.question(self,'', "В системе нет знаний", qm.Ok)
            if ret == qm.Ok:
                pass
            else:
                pass

    def showDialogRecommendation(self):
        if self.goal == None and len(self.knowledge.variables) != 0:
            self.showDialogGoal()
            Window_DialogRecommendation = DialogRecommendation(self.knowledge, self.goal)
            if Window_DialogRecommendation.exec_() == 0:
                self.log = Window_DialogRecommendation.log
        elif len(self.knowledge.variables) != 0:
            Window_DialogRecommendation = DialogRecommendation(self.knowledge, self.goal)
            if Window_DialogRecommendation.exec_() == 0:
                self.log = Window_DialogRecommendation.log
        else:
            qm = QMessageBox()
            qm.setWindowTitle('Нет БЗ')
            ret = qm.question(self,'', "В системе выводимых переменных", qm.Ok)
            if ret == qm.Ok:
                pass
            else:
                pass

    def showDialogGoal(self):
        if len(self.knowledge.variables) == 0:
            qm = QMessageBox()
            qm.setWindowTitle('Нет БЗ')
            ret = qm.question(self,'', "В системе выводимых переменных", qm.Ok)
            if ret == qm.Ok:
                pass
            else:
                pass
        else:
            Window_DialogGoal = DialogGoal(self.knowledge)

            if Window_DialogGoal.exec_() == QDialog.Accepted:
                self.goal = Window_DialogGoal.click_buttonOK()

                mlv = MLV(self.knowledge.as_dict())
                mlv.inference_logical_mechanism(self.goal)

                self.knowledge.derivable_goals = mlv.derivable_goals
                self.knowledge.request_goals = mlv.request_goals
                self.knowledge.rules_mlv = mlv.rules

    def showDialogSolution(self):
        if self.log:
            Window_DialogSolution = DialogSolution(self.log)
            Window_DialogSolution.exec_()
        else:
            qm = QMessageBox()
            qm.setWindowTitle('Нет БЗ')
            ret = qm.question(self,'', "Вы должны пройти консультацию", qm.Ok)
            if ret == qm.Ok:
                pass
            else:
                pass

    def showDialogAddRule(self):
        Window_DialogRuleAdd = DialogRuleAdd()
        Window_DialogRuleAdd.knowledge = self.knowledge
        Window_DialogRuleAdd.RefreshComboBoxFacts()
        if Window_DialogRuleAdd.exec_() == QDialog.Accepted:
            Window_DialogRuleAdd.click_buttonOK()
            self.knowledge = Window_DialogRuleAdd.knowledge
            self.ui.Rules.clear()
            self.RefreshRules()

    def showDialogEditRule(self):
        if len(self.ui.Rules.selectedIndexes()) == 0:
            pass
        else:
            Window_DialogRuleAdd = DialogRuleAdd()
            Window_DialogRuleAdd.knowledge = self.knowledge
            Window_DialogRuleAdd.RefreshComboBoxFacts()
            N = self.find_key()
            Window_DialogRuleAdd.edit = N
            for condition in self.knowledge.rules[N]['premises']:
                Window_DialogRuleAdd.ui.fullCondition.addItem(condition)
            Window_DialogRuleAdd.ui.result.setText(self.knowledge.rules[N]['result'])

            if Window_DialogRuleAdd.exec_() == QDialog.Accepted:
                Window_DialogRuleAdd.click_buttonOK()
                self.knowledge = Window_DialogRuleAdd.knowledge
                self.ui.Rules.clear()
                self.RefreshRules()

    def click_buttonDelete(self):
        if len(self.ui.Rules.selectedIndexes()) == 0:
            pass
        else:
            del self.knowledge.rules[self.find_key()]
            self.ui.Rules.clear()
            self.RefreshRules()

    def get_N(self):
        if len(self.ui.Rules.selectedIndexes()) == 0:
            pass
        else:
            fullRule = self.ui.Rules.currentItem().text()
            for N in self.knowledge.rules:
                joined_conditions = 'IF ' + ' '.join(self.knowledge.rules[N]) + ' THEN ' + self.knowledge.rules[N]['result']
                if fullRule == joined_conditions:
                    break
            return N

    def RefreshRules(self):
        for num, R in enumerate(self.knowledge.rules):
            rule = self.knowledge.rules[R]['condition']
            result = self.knowledge.rules[R]['result']
            self.ui.Rules.addItem(f'{num} -- IF ' + rule + ' THEN ' + result)

    def find_key(self):
        selected_row = self.ui.Rules.currentItem().text()
        for key in self.knowledge.rules:
            rule = self.knowledge.rules[key]['condition']
            result = self.knowledge.rules[key]['result']
            current_row = 'IF ' + rule + ' THEN ' + result
            if selected_row.endswith(current_row):
                break
        return key

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    myapp = Expert_System()
    myapp.show()
    sys.exit(app.exec_())