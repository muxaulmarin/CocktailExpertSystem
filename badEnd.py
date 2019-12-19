from gui_py.bad_End import Ui_Dialog

from PyQt5.QtWidgets import QDialog, QWidget, QApplication, QTableWidgetItem, QAbstractItemView
from PyQt5.QtCore import Qt

from knowledge import Knowledge
from MLV import MLV

class Dialog_BadEnd(QDialog):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        coctails = ['Лонг Айленд', 'Май Тай', 'Белый русский', 'Космополитан', 'Зомби', 'Апероль Шпритц']

        for coctail in coctails:
            self.ui.listWidget.addItem(coctail)

        self.ui.label.setText('К сожалению по вашему запросу ничего не найдено. \n попробуйте коктейли из неоспоримой классики \n или \n пройдите консультацию еще раз. \n Неоспоримая классика среди коктейлей:')