# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogVariables.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(756, 480)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(110, 430, 621, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 471, 421))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(510, 30, 231, 121))
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
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(510, 157, 231, 251))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textDomain = QtWidgets.QLabel(self.groupBox_3)
        self.textDomain.setText("")
        self.textDomain.setObjectName("textDomain")
        self.verticalLayout_3.addWidget(self.textDomain)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.text_box2 = QtWidgets.QLabel(self.groupBox_4)
        self.text_box2.setText("")
        self.text_box2.setObjectName("text_box2")
        self.verticalLayout_4.addWidget(self.text_box2)
        self.verticalLayout_2.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_5)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_5.addWidget(self.textBrowser)
        self.verticalLayout_2.addWidget(self.groupBox_5)
        self.testButton = QtWidgets.QPushButton(Dialog)
        self.testButton.setGeometry(QtCore.QRect(590, 410, 75, 23))
        self.testButton.setObjectName("testButton")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Список переменных"))
        self.groupBox.setTitle(_translate("Dialog", "Действия"))
        self.buttonAdd.setText(_translate("Dialog", "Добавить"))
        self.buttonEdit.setText(_translate("Dialog", "Редактировать"))
        self.buttonDelete.setText(_translate("Dialog", "Удалить"))
        self.groupBox_2.setTitle(_translate("Dialog", "Текушая переменная"))
        self.groupBox_3.setTitle(_translate("Dialog", "Домен"))
        self.groupBox_4.setTitle(_translate("Dialog", "Способ означивания"))
        self.groupBox_5.setTitle(_translate("Dialog", "Текст вопроса для озвучивания"))
        self.testButton.setText(_translate("Dialog", "TEST"))