import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt
from uiconnect_raports import Ui_Dialog

from sql.filterf import FilterF
from sql.base import Session
from sql.category import Category
from sql.competitive import Competitive
from sql.data import Data
from sql.compatitive_filter import CompativeFilterf


class ConnectRaports(QDialog):
    def __init__(self, parent=None):
        super(ConnectRaports, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('Połącz raporty')

        self.cb_main_rap = self.ui.comboBox_main_raport
        self.cb_connect_rap = self.ui.comboBox_connect_raport
        self.pb_connect = self.ui.pushButton_connect_raports


    def set_raports(self):
        """
        fill combo box: main raport and connect raports with data
        """

        try:
            session = Session()
            competitiev = session.query(Competitive).all()
        except:
            QMessageBox.critical(self, "Błąd", "Nie można połączyć się z bazą danych")
            return

        self.cb_main_rap.clear()
        self.cb_connect_rap.clear()
        for compet in competitiev:
            self.cb_main_rap.addItem(compet.name)
            self.cb_connect_rap.addItem(compet.name)










if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('fusion')
    w = ConnectRaports()
    w.show()
    sys.exit(app.exec_())

