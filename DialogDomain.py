from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QTableWidget, QTableWidgetItem, QGroupBox, QVBoxLayout, QPushButton
from DialogDomainAdd import Ui_Dialog as Ui_DialogDomainAdd
from knowledge import Knowledge

class Ui_Dialog(object):

    def __init__(self):
        self.knowledge = Knowledge()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 406)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 360, 621, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.tableWidget = QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(30, 20, 411, 321))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(470, 120, 131, 114))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.buttonAdd = QPushButton(self.groupBox)
        self.buttonAdd.setObjectName("buttonAdd")
        self.verticalLayout.addWidget(self.buttonAdd)
        self.buttonEdit = QPushButton(self.groupBox)
        self.buttonEdit.setObjectName("buttonEdit")
        self.verticalLayout.addWidget(self.buttonEdit)
        self.buttonDelete = QPushButton(self.groupBox)
        self.buttonDelete.setObjectName("buttonDelete")
        self.verticalLayout.addWidget(self.buttonDelete)

        self.buttonAdd.clicked.connect(self.click_buttonAdd)
        self.buttonEdit.clicked.connect(self.click_buttonEdit)
        self.buttonDelete.clicked.connect(self.click_buttonDelete)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Список доменов"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "№"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Домен"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Тип данных"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Значения"))
        self.groupBox.setTitle(_translate("Dialog", "Действия"))
        self.buttonAdd.setText(_translate("Dialog", "Добавить"))
        self.buttonEdit.setText(_translate("Dialog", "Редактировать"))
        self.buttonDelete.setText(_translate("Dialog", "Удалить"))


    def click_buttonAdd(self):
        Window_DialogDomainsAdd = QDialog()
        DialogDomainAE_UI = Ui_DialogDomainAdd()
        DialogDomainAE_UI.setupUi(Window_DialogDomainsAdd)
        rsp = Window_DialogDomainsAdd.exec_()
        if rsp == QDialog.Accepted():
            print(1)
        else:
            print(0)

    def click_buttonEdit(self):
        pass

    def click_buttonDelete(self):
        pass

    def gather_row(self):
        row = self.tableWidget.selectedItems()
        for cell in row:
            if cell.column() == 0:
                n = int(cell.text())
            elif cell.column() == 1:
                name = cell.text()
            elif cell.column() == 2:
                domain_type = cell.text()
            elif cell.column() == 3:
                values = cell.text().split(', ')
        if domain_type == 'Вещественный':
            values = [float(v) for v in values]
        elif domain_type == 'Целочисленный':
            values = [int(v) for v in values]
        return n, name, domain_type, values

