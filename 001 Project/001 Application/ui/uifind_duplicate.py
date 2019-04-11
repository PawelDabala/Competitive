# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'find_duplcate.ui',
# licensing of 'find_duplcate.ui' applies.
#
# Created: Thu Apr 11 06:50:32 2019
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(406, 100)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 392, 83))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_duplicate_nr = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_duplicate_nr.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEdit_duplicate_nr.setObjectName("lineEdit_duplicate_nr")
        self.gridLayout.addWidget(self.lineEdit_duplicate_nr, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(153, 0))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.comboBox_raports_name = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_raports_name.setMinimumSize(QtCore.QSize(150, 0))
        self.comboBox_raports_name.setObjectName("comboBox_raports_name")
        self.gridLayout.addWidget(self.comboBox_raports_name, 0, 1, 1, 1)
        self.pushButton_find = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_find.setObjectName("pushButton_find")
        self.gridLayout.addWidget(self.pushButton_find, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.pushButton_remove_duplicate = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_remove_duplicate.setObjectName("pushButton_remove_duplicate")
        self.gridLayout.addWidget(self.pushButton_remove_duplicate, 1, 2, 1, 1)
        self.pushButton_close = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_close.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_close.setObjectName("pushButton_close")
        self.gridLayout.addWidget(self.pushButton_close, 2, 2, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Dialog", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Dialog", "Raport:", None, -1))
        self.pushButton_find.setText(QtWidgets.QApplication.translate("Dialog", "Wyszukaj", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Dialog", "Liczba zduplikowanych wierszy: ", None, -1))
        self.pushButton_remove_duplicate.setText(QtWidgets.QApplication.translate("Dialog", "Usuń", None, -1))
        self.pushButton_close.setText(QtWidgets.QApplication.translate("Dialog", "Zamknij", None, -1))

