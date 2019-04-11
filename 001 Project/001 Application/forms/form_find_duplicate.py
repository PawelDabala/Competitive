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
        self.pb.close = self.ui.pushButton_close

        # # signals
        # self.pb_connect.clicked.connect(self.connect_raports)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('fusion')
    w = FindDuplicate()
    w.show()
    sys.exit(app.exec_())

