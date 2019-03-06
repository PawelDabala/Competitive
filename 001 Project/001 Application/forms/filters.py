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
        self.tw.itemChanged.connect(self.uncheck_others_items_tree)
        self.ui.pushButtonadddata.clicked.connect(self.add_children)

    """
    
    tree functions
    
    """
    def add_new_parent_node(self):

        value = self.ui.lineEditaddnew.text()
        if len(value) > 0:
            if self.isunique(value):
                newnod = QTreeWidgetItem(self.tw, [value])
                newnod.setCheckState(0, Qt.CheckState.Unchecked)
                self.ui.lineEditaddnew.setText("")
            else:
                QMessageBox.critical(self, 'Uwaga!!!',
                     "Podana nazwa już istnieje.",
                     QMessageBox.Ok)

    def isunique(self, name):
        """
        check the new value is unice int tree view
        :param name:
        :return:
        """
        #read data from tree view
        root = self.tw.invisibleRootItem()
        child_count = root.childCount()
        nodesname = []
        for i in range(child_count):
            item = root.child(i)
            nodesname.append(item.text(0))

        nodesname = [x.upper() for x in nodesname]
        if name.upper() in nodesname:
            return False
        else:
            return True

    def uncheck_others_items_tree(self, item, column):
        """
        leve only one checked item
        :param item:
        :param column:
        :return:
        """
        self.tw.blockSignals(True)
        root = self.tw.invisibleRootItem()
        child_count = root.childCount()
        for i in range(child_count):
            item2 = root.child(i)
            if item.text(column) != item2.text(0):
                item2.setCheckState(0, Qt.CheckState.Unchecked)
            else:
                item.setCheckState(0, Qt.CheckState.Checked)
        self.tw.blockSignals(False)

    def get_checked_item(self):
        """
        :return: return checked item in tree view
        """
        root = self.tw.invisibleRootItem()
        child_count = root.childCount()
        for i in range(child_count):
            item = root.child(i)
            if item.checkState(0) == Qt.CheckState.Checked:
                return item

    def add_children(self):
        """
        adding items from list to tree
        :return:
        """
        childlist = self.getCheckedItemsTable()
        item = self.get_checked_item()

        #add value to list
        for ch in childlist:
            newitem = QTreeWidgetItem(item, ch)
            newitem.setCheckState(1, Qt.CheckState.Unchecked)
        self.removeCheckedItemsTable()

    """
    
    table view functions
    
    """
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

    def getCheckedItemsTable(self):
        """
        return table with checked items
        :return:
        """
        """
        DO POPRAWY, colmulmny nie moga byc na sztywno !!!!!!!!
        """
        checkeditems = []
        for i in range(self.sti.rowCount()):
            if self.sti.item(i, 0).checkState() == 2:
                checkeditems.append([
                                    "",
                                    self.sti.item(i, 0).text(),
                                    self.sti.item(i, 1).text()
                                    ])
        return checkeditems

    def removeCheckedItemsTable(self):
        """
        remove row frol list table
        :return:
        """
        for i in reversed(range(self.sti.rowCount())):
            if self.sti.item(i, 0).checkState() == 2:
                self.sti.removeRow(i)


if __name__=='__main__':
    app = QApplication(sys.argv)
    w = FiltersForm()
    w.show()
    sys.exit(app.exec_())
