import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt
from uifind_duplicate import Ui_Dialog

from sql.filterf import FilterF
from sql.base import Session
from sql.category import Category
from sql.competitive import Competitive
from sql.data import Data
from sql.compatitive_filter import CompativeFilterf


class FindDuplicate(QDialog):
    def __init__(self, parent=None):
        super(FindDuplicate, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('Znajdz duplikaty')

        self.cb_raports = self.ui.comboBox_raports_name
        self.li_nr_dup = self.ui.lineEdit_duplicate_nr
        self.pb_find = self.ui.pushButton_find
        self.pb_remove = self.ui.pushButton_remove_duplicate
        self.pb_close = self.ui.pushButton_close

        self.li_nr_dup.setReadOnly(True)

        # signals
        # self.pb_connect.clicked.connect(self.connect_raports)
        self.pb_close.clicked.connect(self.close)

    def set_raports(self):
        """
        fill combo box: cb_raports
        """
        try:
            session = Session()
            competitiev = session.query(Competitive).all()
        except:
            QMessageBox.critical(self, "Błąd", "Nie można połączyć się z bazą danych")
            return

        self.cb_raports.clear()

        for compet in competitiev:
            self.cb_raports.addItem(compet.name)

        session.close()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('fusion')
    w = FindDuplicate()
    w.show()
    sys.exit(app.exec_())

