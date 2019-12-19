from gui_py.DialogRecommendation import Ui_Dialog
from goodEnd import Dialog_GoodEnd
from badEnd import Dialog_BadEnd
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

        self.knowledge = knowledge
        self.goal = goal

        self.questions = {}
        self.answers = {}
        self.facts = []
        self.log = []

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
            self.log.append(['Вы дали ответ -- ', answer])
            for var in self.knowledge.variables:
                if self.knowledge.variables[var]['question'] == question:
                    break
            self.facts.append(var + ' == ' + answer)

            self.consultation()

    def questionsExtractor(self):
        for request_var in self.knowledge.request_goals:
            question = self.knowledge.variables[request_var]['question']
            domain = self.knowledge.variables[request_var]['domain']
            answers = self.knowledge.domains[domain]
            self.questions[question] = answers

    def consultation(self):
        if len(self.questions) == 0:
            self.ui.label.setText('')
            self.ui.tableWidget.setRowCount(0)
            self.findAnswerGoal()
            self.log.append(['В результате консультации вы получили ответ на запрос -- ', self.goal])
            self.log.append(['Ответ -- ', self.facts[0]])
            self.End(self.facts[0])
        else:
            question, answers = list(self.questions.items())[0]
            self.log.append(['Был задан вопрос -- ', question])
            del self.questions[question]
            self.ui.label.setText(question)
            self.ui.tableWidget.setRowCount(0)
            for n, answer in enumerate(answers):
                self.ui.tableWidget.insertRow(n)
                self.ui.tableWidget.setItem(n, 0, QTableWidgetItem(answer))
            for n_row in range(self.ui.tableWidget.rowCount()):
                self.ui.tableWidget.item(n_row, 0).setFlags(Qt.ItemIsSelectable |  Qt.ItemIsEnabled)
            self.ui.tableWidget.resizeRowsToContents()

    def findAnswerGoal(self):
        self.log.append(['На основании ответов, полученных во время консультации'])
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
                    self.log.append(['Сработало правило -- ', 
                                     'ЕСЛИ ', 
                                     self.knowledge.rules[rule_id]['condition'], 
                                     ' ТО ', 
                                     self.knowledge.rules[rule_id]['result']])
                    changed_facts = []
                    for fact in self.facts:
                        if fact in premises:
                            continue
                        else:
                            changed_facts.append(fact)
                    result = self.knowledge.rules[rule_id]['result']
                    self.facts = changed_facts + [result]
                    self.log.append(['В результате был выведен следующий факт -- ', result])
                else:
                    continue
            if len(self.facts) == N:
                empty_iterations += 1
            else:
                N = len(self.facts)
        if len(self.facts) != 1:
            self.facts = ['ПУСТО']

    def End(self, answer):
        self.close()
        if self.goal != 'Коктейли':
            Window_End = End(answer)
            Window_End.exec_()
        else:
            if 'ПУСТО' in answer:
                Window_End = Dialog_BadEnd()
                Window_End.exec_()
            else:
                Window_End = Dialog_GoodEnd(answer)
                Window_End.exec_()