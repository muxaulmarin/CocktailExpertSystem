from gui_py.DialogRecommendation import Ui_Dialog

from PyQt5.QtWidgets import QDialog, QWidget, QApplication, QTableWidgetItem, QAbstractItemView
from PyQt5.QtCore import Qt

import random

from knowledge import Knowledge

class DialogRecommendation(QDialog):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.questions = {}

        self.ui.tableWidget.setColumnWidth(0, self.ui.tableWidget.width()-15)
        self.ui.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.tableWidget.setSelectionBehavior(self.ui.tableWidget.SelectRows)
        self.knowledge = Knowledge()

        self.ui.pushButton.setText('Начать!')
        self.ui.label.setText(' ')
        
        if self.ui.pushButton.text() == 'Начать!':
            self.ui.pushButton.clicked.connect(self.click_Start)
        else:
            self.ui.pushButton.clicked.connect(self.click_Answer)

    def extractQuestionAnsAnswers(self):
        for var in self.knowledge.variables:
            question = self.knowledge.variables[var]['question']
            if len(question) > 3:
                domain = self.knowledge.variables[var]['domain']
                answers = self.knowledge.domains[domain]
                self.questions[question] = answers

    def get_question_answers(self):
        n = len(self.questions) - 1
        if n > 0:
            question = [key for key in self.questions][random.randint(0, n)]
        elif n == 0:
            question = [key for key in self.questions][0]
        else:
            return 0, 0
        answers = self.questions[question]
        del self.questions[question]
        return question, answers

    def give_question(self, question, answers):
        question, answers = self.get_question_answers()
        if question == 0 and answers == 0:
            self.ui.label.setText('END')
            self.ui.tableWidget.clear()
        else:
            self.ui.label.setText(question)
            self.ui.tableWidget.setRowCount(0)
            for n, answer in enumerate(answers):
                self.ui.tableWidget.insertRow(n)
                self.ui.tableWidget.setItem(n, 0, QTableWidgetItem(answer))
            for n_row in range(self.ui.tableWidget.rowCount()):
                self.ui.tableWidget.item(n_row, 0).setFlags(Qt.ItemIsSelectable |  Qt.ItemIsEnabled)
            self.ui.tableWidget.resizeRowsToContents()

    def RefreshView(self):
        pass

    def click_Answer(self):
        self.give_question(*self.get_question_answers())

    def click_Start(self):
        self.ui.pushButton.setText('Принять ответ')
        self.give_question(*self.get_question_answers())


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    myapp = DialogRecommendation()
    myapp.show()
    sys.exit(app.exec_())