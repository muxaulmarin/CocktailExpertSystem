from gui_py.DialogSaveAs import Ui_Dialog
from PyQt5.QtWidgets import QDialog, QWidget

class DialogSaveAs(QDialog):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.folder.setText('D:\Learning\AI_Chuprina\CocktailExpertSystem')
        self.ui.file_name.setText('COCTAILS')