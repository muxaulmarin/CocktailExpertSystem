# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogRecommendation.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(312, 480)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(20, 110, 270, 311))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(6)
        self.tableWidget.setFont(font)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(100, 440, 110, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 270, 60))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.buttonTest = QtWidgets.QPushButton(Dialog)
        self.buttonTest.setGeometry(QtCore.QRect(10, 430, 75, 23))
        self.buttonTest.setObjectName("buttonTest")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Рекомендация"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Варианты ответа"))
        self.pushButton.setText(_translate("Dialog", "Принять ответ"))
        self.label.setText(_translate("Dialog", "TextLabel"))
        self.buttonTest.setText(_translate("Dialog", "TEST"))
