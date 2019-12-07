# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogVariableAdd.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(347, 592)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(-360, 550, 621, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(30, 80, 291, 261))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Domains = QtWidgets.QComboBox(self.groupBox)
        self.Domains.setObjectName("Domains")
        self.verticalLayout.addWidget(self.Domains)
        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.buttonDelete = QtWidgets.QPushButton(self.groupBox)
        self.buttonDelete.setObjectName("buttonDelete")
        self.verticalLayout.addWidget(self.buttonDelete)
        self.buttonEdit = QtWidgets.QPushButton(self.groupBox)
        self.buttonEdit.setObjectName("buttonEdit")
        self.verticalLayout.addWidget(self.buttonEdit)
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 350, 291, 191))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.VarCategory = QtWidgets.QComboBox(self.groupBox_3)
        self.VarCategory.setObjectName("VarCategory")
        self.verticalLayout_3.addWidget(self.VarCategory)
        self.textQuestion = QtWidgets.QTextEdit(self.groupBox_3)
        self.textQuestion.setObjectName("textQuestion")
        self.verticalLayout_3.addWidget(self.textQuestion)
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(30, 10, 291, 61))
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.VarName = QtWidgets.QLineEdit(self.groupBox_4)
        self.VarName.setObjectName("VarName")
        self.verticalLayout_4.addWidget(self.VarName)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Добавление переменной"))
        self.groupBox.setTitle(_translate("Dialog", "Домен"))
        self.buttonDelete.setText(_translate("Dialog", "Удалить домен"))
        self.buttonEdit.setText(_translate("Dialog", "Редактировать домен"))
        self.groupBox_3.setTitle(_translate("Dialog", "Вид переменной"))
        self.groupBox_4.setTitle(_translate("Dialog", "Имя переменной"))
