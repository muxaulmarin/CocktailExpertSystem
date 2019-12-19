from gui_py.DialogRecommendation import Ui_Dialog
from END import End

from PyQt5.QtWidgets import QDialog, QWidget, QApplication, QTableWidgetItem, QAbstractItemView
from PyQt5.QtCore import Qt

import random

from knowledge import Knowledge
from MLV import MLV

class DialogRecommendation(QDialog):
    def __init__(self, knowledge, goal, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.tableWidget.setColumnWidth(0, self.ui.tableWidget.width()-15)
        self.ui.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.tableWidget.setSelectionBehavior(self.ui.tableWidget.SelectRows)
        
        self.ui.pushButton.setText('Принять ответ')
        self.ui.pushButton.clicked.connect(self.click_Answer)
        self.ui.buttonTest.clicked.connect(self.click_buttonTEST)

        self.knowledge = knowledge
        self.goal = goal

        self.questions = {}
        self.answers = {}
        self.facts = []

        self.questionsExtractor()

        if len(self.questions) != 0:
            self.consultation()


    def click_Answer(self):
        if len(self.ui.tableWidget.selectedIndexes()) == 0:
            pass
        else:
            idx = self.ui.tableWidget.selectedIndexes()[0].row()
            answer = self.ui.tableWidget.item(idx, 0).text()
            question = self.ui.label.text()
            self.answers[question] = answer

            for var in self.knowledge.variables:
                if self.knowledge.variables[var]['question'] == question:
                    break
            self.facts.append(var + ' == ' + answer)
            print(self.facts)

            self.consultation()

    def questionsExtractor(self):
        for request_var in self.knowledge.request_goals:
            question = self.knowledge.variables[request_var]['question']
            domain = self.knowledge.variables[request_var]['domain']
            answers = self.knowledge.domains[domain]
            self.questions[question] = answers

    def consultation(self):
        if len(self.questions) == 0:
            self.ui.label.setText('END')
            self.ui.tableWidget.setRowCount(0)
            self.findAnswerGoal()
            self.End(self.facts[0])
        else:
            question, answers = list(self.questions.items())[0]
            print(self.questions.keys())
            del self.questions[question]
            print('delete')
            print(self.questions.keys())
            self.ui.label.setText(question)
            self.ui.tableWidget.setRowCount(0)
            for n, answer in enumerate(answers):
                self.ui.tableWidget.insertRow(n)
                self.ui.tableWidget.setItem(n, 0, QTableWidgetItem(answer))
            for n_row in range(self.ui.tableWidget.rowCount()):
                self.ui.tableWidget.item(n_row, 0).setFlags(Qt.ItemIsSelectable |  Qt.ItemIsEnabled)
            self.ui.tableWidget.resizeRowsToContents()

    def findAnswerGoal(self):
        N = len(self.facts)
        empty_iterations = 0
        while empty_iterations < 3:
            for rule_id in self.knowledge.rules_mlv:
                premises = self.knowledge.rules[rule_id]['premises']
                premises = [premise for premise in premises if premise not in ['AND', 'OR', 'NOT']]
                isNeed = True
                for premise in premises:
                    if premise not in self.facts:
                        isNeed = False
                        break
                if isNeed:
                    changed_facts = []
                    for fact in self.facts:
                        if fact in premises:
                            continue
                        else:
                            changed_facts.append(fact)
                    result = self.knowledge.rules[rule_id]['result']
                    self.facts = changed_facts + [result]
                else:
                    continue
            if len(self.facts) == N:
                empty_iterations += 1
            else:
                N = len(self.facts)
        if len(self.facts) != 1:
            self.facts = ['По вашему запросу ничего не найдено']

    def End(self, answer):
        Window_End = End(answer)
        if Window_End.exec_() == QDialog.Accepted:
            self.ui.pushButton.setText('Начать!')
            self.ui.tableWidget.setRowCount(0)
            self.ui.label.setText(' ')
        else:
            pass

    def click_buttonTEST(self):
        print(self.goal)
        print(self.knowledge.rules_mlv)
        print(self.knowledge.derivable_goals)
        print(self.knowledge.request_goals)