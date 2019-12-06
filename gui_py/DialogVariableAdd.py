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
        Dialog.resize(640, 532)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(-20, 480, 621, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(350, 20, 271, 441))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Domains = QtWidgets.QComboBox(self.groupBox)
        self.Domains.setObjectName("Domains")
        self.verticalLayout.addWidget(self.Domains)
        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 90, 291, 61))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.VarType = QtWidgets.QComboBox(self.groupBox_2)
        self.VarType.setObjectName("VarType")
        self.verticalLayout_2.addWidget(self.VarType)
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 160, 291, 301))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.VarCategory = QtWidgets.QComboBox(self.groupBox_3)
        self.VarCategory.setObjectName("VarCategory")
        self.verticalLayout_3.addWidget(self.VarCategory)
        self.TextQuestion = QtWidgets.QTextBrowser(self.groupBox_3)
        self.TextQuestion.setObjectName("TextQuestion")
        self.verticalLayout_3.addWidget(self.TextQuestion)
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(30, 20, 291, 61))
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.VarName = QtWidgets.QLineEdit(self.groupBox_4)
        self.VarName.setObjectName("VarName")
        self.verticalLayout_4.addWidget(self.VarName)
        self.testButton = QtWidgets.QPushButton(Dialog)
        self.testButton.setGeometry(QtCore.QRect(130, 490, 75, 23))
        self.testButton.setObjectName("testButton")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
		
        for var_type in ['Строковый', 'Целочисленный', 'Вещественный', 'Булевый']:
            self.VarType.addItem(var_type)

        for var_cat in ['Выводимая', 'Запрашиваемая', 'Запрашиваемо-выводимая']:
            self.VarCategory.addItem(var_cat)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Добавление переменной"))
        self.groupBox.setTitle(_translate("Dialog", "Домен"))
        self.pushButton.setText(_translate("Dialog", "Убрать домен"))
        self.pushButton_2.setText(_translate("Dialog", "Редактировать домен"))
        self.groupBox_2.setTitle(_translate("Dialog", "Тип переменной"))
        self.groupBox_3.setTitle(_translate("Dialog", "Вид переменной"))
        self.groupBox_4.setTitle(_translate("Dialog", "Имя переменной"))
        self.testButton.setText(_translate("Dialog", "TEST"))
