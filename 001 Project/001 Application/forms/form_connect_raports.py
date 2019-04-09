import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt
from uiconnect_raports import Ui_Dialog

from sqlalchemy import and_
from filterf import FilterF
from base import Session
from category import Category
from competitive import Competitive
from data import Data
from compatitive_filter import CompativeFilterf


class ConnectRaports(QDialog):
    def __init__(self, parent=None):
        super(ConnectRaports, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('Połącz raporty')

        self.cb_main_rap = self.ui.comboBox_main_raport
        self.cb_connect_rap = self.ui.comboBox_connect_raport
        self.pb_connect = self.ui.pushButton_connect_raports
        






if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('fusion')
    w = ConnectRaports()
    w.show()
    sys.exit(app.exec_())

