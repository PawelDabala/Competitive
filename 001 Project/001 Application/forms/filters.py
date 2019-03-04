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

        #table
        self.table = self.ui.tableViewcolumns
        self.sti = QStandardItemModel()
        self.table.setModel(self.sti)
        self.table.verticalHeader().setDefaultSectionSize(10)
        self.table.horizontalHeader().setDefaultSectionSize(200)
        self.table.setSortingEnabled(True)

        #treeWidget
        self.tw = self.ui.treeWidgetasignet
        self.tw.setHeaderLabels(['Name', 'Year', 'Channel'])
        self.tw.setAlternatingRowColors(True)

        """
        set controls data
        """
        self.sti.setHorizontalHeaderLabels(headersname)
        self.sti.setColumnCount(len(headersname))
        self.setrowdata(columns)

        """
        signals
        """
        self.ui.pushButtonaddnew.clicked.connect(self.add_new_parent_node)

    def setrowdata(self, columns):
        """
        add data to table rows
        :param columns:
        :return:
        """
        for row in range(len(columns)):
            for col in range(len(columns[row])):
                item = QStandardItem(columns[row][col])
                item.setEditable(False)
                if col == 0:
                    item.setCheckable(True)
                self.sti.setItem(row, col, item)

    def add_new_parent_node(self):
        print("add_new_parent_node")
        value = self.ui.lineEditaddnew.text()
        if len(value) > 0:
            newnod = QTreeWidgetItem(self.tw,[value])
            if self.isunique():
                newnod.setCheckState(0, Qt.CheckState.Unchecked)
            else:
                print('value all ready exist')


    def isunique(self):

        root = self.tw.invisibleRootItem()
        child_count = root.childCount()
        for i in range(child_count):
            item = root.child(i)
            print(item.text(0))
        #to nie działa poprawnie
        # iterator = QTreeWidgetItemIterator(self.tw)
        # parnode = []
        #
        # while iterator.value():
        #     item = iterator.value()
        #     print(item.text(0))
        #     # if item.parent() is None:
        #     #     if item.text(0) in parnode:
        #     #         return False
        #     #     else:
        #     #         parnode.append(item.text(0))


if __name__=='__main__':
    app = QApplication(sys.argv)
    w = FiltersForm()
    w.show()
    sys.exit(app.exec_())
