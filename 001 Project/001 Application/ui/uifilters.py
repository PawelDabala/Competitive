# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filters.ui',
# licensing of 'filters.ui' applies.
#
# Created: Thu Mar  7 14:10:02 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1307, 727)
        self.treeWidgetasignet = QtWidgets.QTreeWidget(Dialog)
        self.treeWidgetasignet.setGeometry(QtCore.QRect(10, 10, 301, 651))
        self.treeWidgetasignet.setObjectName("treeWidgetasignet")
        self.treeWidgetasignet.headerItem().setText(0, "1")
        self.tableViewcolumns = QtWidgets.QTableView(Dialog)
        self.tableViewcolumns.setGeometry(QtCore.QRect(330, 10, 971, 651))
        self.tableViewcolumns.setObjectName("tableViewcolumns")
        self.pushButtonadddata = QtWidgets.QPushButton(Dialog)
        self.pushButtonadddata.setGeometry(QtCore.QRect(310, 320, 21, 41))
        self.pushButtonadddata.setObjectName("pushButtonadddata")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 670, 301, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEditaddnew = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEditaddnew.setObjectName("lineEditaddnew")
        self.horizontalLayout.addWidget(self.lineEditaddnew)
        self.pushButtonaddnew = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonaddnew.setObjectName("pushButtonaddnew")
        self.horizontalLayout.addWidget(self.pushButtonaddnew)
        self.pushButtonremovenodes = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonremovenodes.setObjectName("pushButtonremovenodes")
        self.horizontalLayout.addWidget(self.pushButtonremovenodes)
        self.pushButtonrun = QtWidgets.QPushButton(Dialog)
        self.pushButtonrun.setGeometry(QtCore.QRect(1230, 700, 75, 23))
        self.pushButtonrun.setObjectName("pushButtonrun")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(330, 700, 211, 21))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBoxnotassigne = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.checkBoxnotassigne.setObjectName("checkBoxnotassigne")
        self.horizontalLayout_2.addWidget(self.checkBoxnotassigne)
        self.checkBoxCheckAll = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.checkBoxCheckAll.setObjectName("checkBoxCheckAll")
        self.horizontalLayout_2.addWidget(self.checkBoxCheckAll)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Dialog", None, -1))
        self.pushButtonadddata.setText(QtWidgets.QApplication.translate("Dialog", "<", None, -1))
        self.pushButtonaddnew.setText(QtWidgets.QApplication.translate("Dialog", "Nowy", None, -1))
        self.pushButtonremovenodes.setText(QtWidgets.QApplication.translate("Dialog", "Usuń", None, -1))
        self.pushButtonrun.setText(QtWidgets.QApplication.translate("Dialog", "Urchom", None, -1))
        self.checkBoxnotassigne.setText(QtWidgets.QApplication.translate("Dialog", "nie przypisane", None, -1))
        self.checkBoxCheckAll.setText(QtWidgets.QApplication.translate("Dialog", "zaznacz wszystkie", None, -1))

