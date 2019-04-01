import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt
from uiexcel import Ui_Dialog
from PySide2.QtGui import QStandardItemModel, QStandardItem

from sql.filterf import FilterF
from sql.base import Session
from sql.category import Category



class ExcelForm(QDialog):
    def __init__(self, parent=None):
        super(ExcelForm, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('Generuj plik Excela')
        self.setWindowModality(Qt.ApplicationModal)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('fusion')
    w = ExcelForm()
    w.show()
    sys.exit(app.exec_())
