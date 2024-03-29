from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(342, 558)
        self.buttonBox = QtWidgets.QDialogButtonBox(dialog)
        self.buttonBox.setGeometry(QtCore.QRect(-370, 520, 621, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox = QtWidgets.QGroupBox(dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 301, 53))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.domainName = QtWidgets.QLineEdit(self.groupBox)
        self.domainName.setObjectName("domainName")
        self.verticalLayout.addWidget(self.domainName)
        self.groupBox_3 = QtWidgets.QGroupBox(dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 230, 301, 281))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.domainList = QtWidgets.QListWidget(self.groupBox_3)
        self.domainList.setObjectName("domainList")
        self.verticalLayout_3.addWidget(self.domainList)
        self.groupBox_4 = QtWidgets.QGroupBox(dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 80, 301, 141))
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.domainValue = QtWidgets.QLineEdit(self.groupBox_4)
        self.domainValue.setObjectName("domainValue")
        self.verticalLayout_4.addWidget(self.domainValue)
        self.buttonAdd = QtWidgets.QPushButton(self.groupBox_4)
        self.buttonAdd.setObjectName("buttonAdd")
        self.verticalLayout_4.addWidget(self.buttonAdd)
        self.buttonEdit = QtWidgets.QPushButton(self.groupBox_4)
        self.buttonEdit.setObjectName("buttonEdit")
        self.verticalLayout_4.addWidget(self.buttonEdit)
        self.buttonDelete = QtWidgets.QPushButton(self.groupBox_4)
        self.buttonDelete.setObjectName("buttonDelete")
        self.verticalLayout_4.addWidget(self.buttonDelete)

        self.retranslateUi(dialog)
        self.buttonBox.accepted.connect(dialog.accept)
        self.buttonBox.rejected.connect(dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Добавление домена"))
        self.groupBox.setTitle(_translate("dialog", "Имя домена"))
        self.groupBox_3.setTitle(_translate("dialog", "Список допустимых значений"))
        self.groupBox_4.setTitle(_translate("dialog", "Допустимое значение"))
        self.buttonAdd.setText(_translate("dialog", "Добавить"))
        self.buttonEdit.setText(_translate("dialog", "Редактировать"))
        self.buttonDelete.setText(_translate("dialog", "Удалить"))