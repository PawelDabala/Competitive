# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connect_raports.ui',
# licensing of 'connect_raports.ui' applies.
#
# Created: Tue Apr  9 06:50:06 2019
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(317, 91)
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 301, 51))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(100, 0))
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.comboBox_main_raport = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_main_raport.setObjectName("comboBox_main_raport")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_main_raport)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.comboBox_connect_raport = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_connect_raport.setObjectName("comboBox_connect_raport")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox_connect_raport)
        self.pushButton_connect_raports = QtWidgets.QPushButton(Dialog)
        self.pushButton_connect_raports.setGeometry(QtCore.QRect(232, 63, 80, 23))
        self.pushButton_connect_raports.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pushButton_connect_raports.setObjectName("pushButton_connect_raports")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Dialog", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Dialog", "Raport główny", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Dialog", "Rapord do dołączenia", None, -1))
        self.pushButton_connect_raports.setText(QtWidgets.QApplication.translate("Dialog", "Połącz", None, -1))

