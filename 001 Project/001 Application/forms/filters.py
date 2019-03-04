import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt
from uifilters import Ui_Dialog
from PySide2.QtGui import QStandardItemModel, QStandardItem


class FiltersForm(QDialog):
    def __init__(self, row_nr, filtername, columns, headersname, parent=None):
        super(FiltersForm, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.table = self.ui.tableViewcolumns
        self.sti = QStandardItemModel()
        self.table.setModel(self.sti)

        """
        set controls data
        """
        self.sti.setHorizontalHeaderLabels(headersname)
        self.sti.setColumnCount(len(headersname))

    def setrowdata(self, columns):
        """
        add data to rows
        :param columns:
        :return:
        """
        for row in columns:
            for col in row:
                Tutaj kontynuj!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                item = QStandardItem(col)
                item.setCheckable(True)
                item.setEditable(False)










if __name__=='__main__':
    app = QApplication(sys.argv)
    w = FiltersForm()
    w.show()
    sys.exit(app.exec_())
