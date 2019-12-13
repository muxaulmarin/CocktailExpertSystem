# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogRuleAdd.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(-20, 430, 621, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(50, 20, 200, 60))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Facts = QtWidgets.QComboBox(self.groupBox)
        self.Facts.setObjectName("Facts")
        self.verticalLayout.addWidget(self.Facts)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(300, 20, 80, 60))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.condition = QtWidgets.QComboBox(self.groupBox_2)
        self.condition.setObjectName("condition")
        self.condition.addItem("")
        self.condition.addItem("")
        self.condition.addItem("")
        self.verticalLayout_2.addWidget(self.condition)
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(390, 20, 220, 61))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.result = QtWidgets.QLineEdit(self.groupBox_3)
        self.result.setObjectName("result")
        self.verticalLayout_3.addWidget(self.result)
        self.fullCondition = QtWidgets.QListWidget(Dialog)
        self.fullCondition.setGeometry(QtCore.QRect(50, 95, 330, 351))
        self.fullCondition.setObjectName("fullCondition")
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(390, 90, 220, 130))
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.buttonAdd = QtWidgets.QPushButton(self.groupBox_4)
        self.buttonAdd.setObjectName("buttonAdd")
        self.verticalLayout_4.addWidget(self.buttonAdd)
        self.buttonEdit = QtWidgets.QPushButton(self.groupBox_4)
        self.buttonEdit.setObjectName("buttonEdit")
        self.verticalLayout_4.addWidget(self.buttonEdit)
        self.buttonDelete = QtWidgets.QPushButton(self.groupBox_4)
        self.buttonDelete.setObjectName("buttonDelete")
        self.verticalLayout_4.addWidget(self.buttonDelete)
        self.radioButtonFact = QtWidgets.QRadioButton(Dialog)
        self.radioButtonFact.setGeometry(QtCore.QRect(20, 40, 20, 20))
        self.radioButtonFact.setText("")
        self.radioButtonFact.setChecked(True)
        self.radioButtonFact.setObjectName("radioButtonFact")
        self.radioButtonCondition = QtWidgets.QRadioButton(Dialog)
        self.radioButtonCondition.setGeometry(QtCore.QRect(270, 40, 20, 20))
        self.radioButtonCondition.setText("")
        self.radioButtonCondition.setObjectName("radioButtonCondition")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Добавить правило"))
        self.groupBox.setTitle(_translate("Dialog", "Факт"))
        self.groupBox_2.setTitle(_translate("Dialog", "Условие"))
        self.condition.setItemText(0, _translate("Dialog", "AND"))
        self.condition.setItemText(1, _translate("Dialog", "OR"))
        self.condition.setItemText(2, _translate("Dialog", "NOT"))
        self.groupBox_3.setTitle(_translate("Dialog", "Вывод"))
        self.groupBox_4.setTitle(_translate("Dialog", "Действия"))
        self.buttonAdd.setText(_translate("Dialog", "Добавить"))
        self.buttonEdit.setText(_translate("Dialog", "Редактировать"))
        self.buttonDelete.setText(_translate("Dialog", "Удалить"))
