from gui_py.good_End import Ui_Dialog

from PyQt5.QtWidgets import QDialog, QWidget, QApplication, QTableWidgetItem, QAbstractItemView
from PyQt5.QtCore import Qt

from knowledge import Knowledge
from MLV import MLV

class Dialog_GoodEnd(QDialog):
    def __init__(self, end, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        coctails = end.split(' == ')[-1].split(', ')

        for coctail in coctails:
            self.ui.listWidget.addItem(coctail)

        self.ui.label.setText('Вам подойдут следующие коктейли:')