import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt
from uifilltes_manage import Ui_Dialog

# from sqlalchemy import and_
# from sql.filterf import FilterF
# from sql.base import Session
# from sql.category import Category
# from sql.competitive import Competitive
# from sql.data import Data
# from sql.compatitive_filter import CompativeFilterf


class FiltersManager(QDialog):
    def __init__(self, parent=None):
        super(FiltersManager, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('Znajdz duplikaty')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('fusion')
    w = FiltersManager()
    w.show()
    sys.exit(app.exec_())

