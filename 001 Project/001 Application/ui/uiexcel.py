# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'excel.ui',
# licensing of 'excel.ui' applies.
#
# Created: Tue Apr  2 16:28:36 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(489, 304)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 480, 275))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(9)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 55))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 60))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 191, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setMaximumSize(QtCore.QSize(43, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox_raport_name = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_raport_name.setObjectName("comboBox_raport_name")
        self.horizontalLayout.addWidget(self.comboBox_raport_name)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox_3.setMinimumSize(QtCore.QSize(100, 200))
        self.groupBox_3.setMaximumSize(QtCore.QSize(80, 200))
        self.groupBox_3.setObjectName("groupBox_3")
        self.listWidget_year = QtWidgets.QListWidget(self.groupBox_3)
        self.listWidget_year.setGeometry(QtCore.QRect(0, 20, 101, 181))
        self.listWidget_year.setSizeIncrement(QtCore.QSize(4, 0))
        self.listWidget_year.setObjectName("listWidget_year")
        self.horizontalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox_4.setMinimumSize(QtCore.QSize(100, 0))
        self.groupBox_4.setMaximumSize(QtCore.QSize(100, 16777215))
        self.groupBox_4.setObjectName("groupBox_4")
        self.listWidget_mont = QtWidgets.QListWidget(self.groupBox_4)
        self.listWidget_mont.setGeometry(QtCore.QRect(0, 20, 101, 181))
        self.listWidget_mont.setSizeIncrement(QtCore.QSize(4, 0))
        self.listWidget_mont.setObjectName("listWidget_mont")
        self.horizontalLayout_2.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox_5.setMinimumSize(QtCore.QSize(100, 0))
        self.groupBox_5.setMaximumSize(QtCore.QSize(100, 16777215))
        self.groupBox_5.setObjectName("groupBox_5")
        self.listWidget_week = QtWidgets.QListWidget(self.groupBox_5)
        self.listWidget_week.setGeometry(QtCore.QRect(0, 20, 101, 181))
        self.listWidget_week.setSizeIncrement(QtCore.QSize(4, 0))
        self.listWidget_week.setObjectName("listWidget_week")
        self.horizontalLayout_2.addWidget(self.groupBox_5)
        self.groupBox_6 = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox_6.setMinimumSize(QtCore.QSize(150, 0))
        self.groupBox_6.setMaximumSize(QtCore.QSize(150, 16777215))
        self.groupBox_6.setObjectName("groupBox_6")
        self.listWidget_producer = QtWidgets.QListWidget(self.groupBox_6)
        self.listWidget_producer.setGeometry(QtCore.QRect(0, 20, 151, 181))
        self.listWidget_producer.setSizeIncrement(QtCore.QSize(4, 0))
        self.listWidget_producer.setObjectName("listWidget_producer")
        self.horizontalLayout_2.addWidget(self.groupBox_6)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 270, 471, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.lineEdit_rows_count = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_rows_count.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lineEdit_rows_count.setObjectName("lineEdit_rows_count")
        self.horizontalLayout_3.addWidget(self.lineEdit_rows_count)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.pushButton_excel = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_excel.setObjectName("pushButton_excel")
        self.horizontalLayout_3.addWidget(self.pushButton_excel)
        self.pushButton_close = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout_3.addWidget(self.pushButton_close)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Dialog", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("Dialog", "Raport", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Dialog", "nazwa:", None, -1))
        self.groupBox_3.setTitle(QtWidgets.QApplication.translate("Dialog", "Rok", None, -1))
        self.groupBox_4.setTitle(QtWidgets.QApplication.translate("Dialog", "Miesiąc", None, -1))
        self.groupBox_5.setTitle(QtWidgets.QApplication.translate("Dialog", "Tydzień", None, -1))
        self.groupBox_6.setTitle(QtWidgets.QApplication.translate("Dialog", "Producer", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Dialog", "Wierszy:", None, -1))
        self.pushButton_excel.setText(QtWidgets.QApplication.translate("Dialog", "Excel", None, -1))
        self.pushButton_close.setText(QtWidgets.QApplication.translate("Dialog", "Zamknij", None, -1))

