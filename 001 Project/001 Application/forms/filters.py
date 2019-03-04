import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt
from uifilters import Ui_Dialog


class FiltersForm(QDialog):
    def __init__(self, row_nr, filtername, columns, haders, parent=None):
        super(FiltersForm, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        print(filtername)
        #print(columns)
        print(haders)


if __name__=='__main__':
    app = QApplication(sys.argv)
    w = FiltersForm()
    w.show()
    sys.exit(app.exec_())
