from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 406)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 360, 621, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(470, 120, 131, 114))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.buttonAdd = QtWidgets.QPushButton(self.groupBox)
        self.buttonAdd.setObjectName("buttonAdd")
        self.verticalLayout.addWidget(self.buttonAdd)
        self.buttonEdit = QtWidgets.QPushButton(self.groupBox)
        self.buttonEdit.setObjectName("buttonEdit")
        self.verticalLayout.addWidget(self.buttonEdit)
        self.buttonDelete = QtWidgets.QPushButton(self.groupBox)
        self.buttonDelete.setObjectName("buttonDelete")
        self.verticalLayout.addWidget(self.buttonDelete)
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(20, 20, 431, 371))
        self.tableView.setObjectName("tableView")

        self.tableModel = QtGui.QStandardItemModel(Dialog)
        self.tableModel.setHorizontalHeaderLabels(['Имя домена', 'Значения'])

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Список доменов"))
        self.groupBox.setTitle(_translate("Dialog", "Действия"))
        self.buttonAdd.setText(_translate("Dialog", "Добавить"))
        self.buttonEdit.setText(_translate("Dialog", "Редактировать"))
        self.buttonDelete.setText(_translate("Dialog", "Удалить"))