
from PyQt5 import QtSvg, QtCore
from PyQt5.QtWidgets import QWidget, QDialog, QDialogButtonBox

class Dialog_Ui(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Tree")
        Dialog.resize(1000, 650)
        self.viewer = QtSvg.QSvgWidget(r"embed.svg", parent=Dialog)
        self.viewer.setGeometry(0, 0, 1000, 650)

class WindowSVG(QDialog):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Dialog_Ui()
        self.ui.setupUi(self)




