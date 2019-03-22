import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt
from uifilters import Ui_Dialog
from PySide2.QtGui import QStandardItemModel, QStandardItem

from sql.filterf import FilterF
from sql.base import Session
from sql.category import Category
from funclass.filterrows import FilterRows




class FiltersForm(QDialog):
    def __init__(self, filter_id, columns, headersname, parent=None):
        super(FiltersForm, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.filter_id = filter_id
        self.columns = columns
        self.main_form = parent

        #form
        self.line_filters = [self.ui.lineEditfilter_1,
                             self.ui.lineEditfilter_2,
                             self.ui.lineEditfilter_3,
                             self.ui.lineEditfilter_4,
                             self.ui.lineEditfilter_5]

        for line in self.line_filters:
            line.setClearButtonEnabled(True)
            line.setEnabled(False)
            line.textChanged.connect(self.make_filter)

        #table
        self.table = self.ui.tableViewcolumns
        self.sti = QStandardItemModel()
        self.table.setModel(self.sti)
        self.table.verticalHeader().setDefaultSectionSize(10)
        self.table.horizontalHeader().setDefaultSectionSize(172)
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
        self.ui.pushButtonremovenodes.clicked.connect(self.delete_tree_items)
        self.ui.checkBoxCheckAll.stateChanged.connect(lambda: self.select_deselect_rows(self.ui.checkBoxCheckAll))
        self.ui.checkBoxnotassigne.stateChanged.connect(lambda: self.show_not_assigned_rows(self.ui.checkBoxnotassigne))
        self.ui.pushButtonrun.clicked.connect(self.make_assigned)
        self.ui.pushButtonremove_fitlers_text.clicked.connect(self.clear_all_filter_line)

        """
        function
        """
        self.get_data_from_database()
        self.set_filter_line_enable()
        self.start_rows = self.get_all_data_table()

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
                # save to database
                self.save_data_from_tree()
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

    def delete_tree_items(self):
        """
        delete checked items from tree
        :return:
        """
        root = self.tw.invisibleRootItem()
        child_count = root.childCount()
        transfers = []

        #delete main node
        for i in reversed(range(child_count)):
            item = root.child(i)
            if item.checkState(0) == Qt.CheckState.Checked:
                children = item.takeChildren()
                for child in children:
                    temchild = []
                    for colnr in range(self.tw.columnCount())[1:]:
                        temchild.append(child.text(colnr))
                    transfers.append(temchild)
                root.removeChild(item)
            #delete childe node
            if item is not None:
                child_count = item.childCount()
                for j in reversed(range(child_count)):
                    itemch = item.child(j)
                    if itemch.checkState(1) == Qt.CheckState.Checked:
                        temchild = []
                        for colnr in range(self.tw.columnCount())[1:]:
                            temchild.append(itemch.text(colnr))
                        transfers.append(temchild)
                        item.removeChild(itemch)

        self.add_rowto_table(transfers)

        # save to database
        self.save_data_from_tree()

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
        #treechilds = self.get_all_tree_children()

        if item is None:
            QMessageBox.critical(self, 'Uwaga!!!',
                                 "Elementy nie zostały przeniesione\nZaznacz kategorie po prawej stronie.",
                                 QMessageBox.Ok)
        else:
            #remove exist childs from tree
            self.remove_child_if_exist_in_tree(childlist)

            #add value to list
            for ch in childlist:
                newitem = QTreeWidgetItem(item, ch)
                newitem.setCheckState(1, Qt.CheckState.Unchecked)

            self.removeCheckedItemsTable()

        #save to database
        self.save_data_from_tree()

    def save_data_from_tree(self):
        """
        1) delete in data base all categorys for filter
        2) save all catecorys and under categroy to database
        """

        #delete all categorys
        session = Session()
        filter_ = session.query(FilterF).get(self.filter_id)
        delete_q = Category.__table__.delete().where(Category.filter_id == filter_.id)
        session.execute(delete_q)
        session.commit()

        root = self.tw.invisibleRootItem()
        child_count = root.childCount()

        for i in range(child_count):
            item = root.child(i)
            if item.parent() is None:
                parent_name = item.text(0)
                all_childs = []
                for j in range(item.childCount()):
                    childs = [item.child(j).text(i) for i in range(self.tw.columnCount())[1:]]
                    all_childs.append(childs)

                new_category = Category(parent_name, all_childs)
                filter_.categorys.append(new_category)

        session.commit()
        session.close()

    def get_data_from_database(self):
        """
        get all categorys for filter and send to show in treewidget
        """

        session = Session()
        categorys = session.query(Category).filter_by(filter_id=self.filter_id).all()
        for category in categorys:
            head = QTreeWidgetItem(self.tw, [category.name])
            head.setCheckState(0, Qt.CheckState.Unchecked)
            for item in category.items:
                newch = QTreeWidgetItem(head, [''] + item)
                newch.setCheckState(1, Qt.CheckState.Unchecked)

    def get_all_tree_children(self):
        """
        get all children from tree widget
        :return: tuple all chldren
        """
        iterator = QTreeWidgetItemIterator(self.tw)
        all_child = []
        while iterator.value():
            item = iterator.value()
            if item.parent() is not None:
                parentchild = [item.text(i) for i in range(self.tw.columnCount())[1:]]
                all_child.append(parentchild)

            iterator += 1
        return all_child

    def remove_child_if_exist_in_tree(self, exists_childs):
        """
        remove item from tree widget if is in exists_childs list
        :param exists_childs:
        :return:
        """
        exists_childs = list(list(b.strip().lower() for b in a) for a in exists_childs)
        iterator = QTreeWidgetItemIterator(self.tw)

        while iterator.value():
            item = iterator.value()
            if item.parent() is not None:
                parentchild = [item.text(i) for i in range(self.tw.columnCount())[1:]]
                parentchild = list(a.strip().lower() for a in parentchild)
                parentchild = ['']+parentchild
                if parentchild in exists_childs:
                    item.parent().removeChild(item)
                    continue
            iterator += 1

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
        #FIXME colmulmny nie moga byc na sztywno
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

    def get_all_data_table(self):
        """
        get all rows from table
        :return: list of rows
        """
        rows = []
        for row in range(self.sti.rowCount()):
            cols = []
            for col in range(self.sti.columnCount()):
                cols.append(self.sti.item(row, col).text())
            rows.append(cols)
        return rows

    def add_rowto_table(self, newrows):
        """
        add row form filter to table if not
        allready exist in table
        :return:
        """
        tabledata = self.get_all_data_table()

        for nr, row in enumerate(newrows):
            if row not in tabledata:
                rowcount = self.sti.rowCount()
                self.sti.setRowCount(rowcount)
                for col in range(len(row)):
                    item = QStandardItem(str(newrows[nr][col]))
                    if col == 0:
                        item.setCheckable(True)
                    self.sti.setItem(rowcount, col, item)

    def select_deselect_rows(self, chcontrol):
        """
        check or unchecked checbox in table
        :param chcontrol:
        :return:
        """
        for rnr in range(self.sti.rowCount()):
            if chcontrol.isChecked():
                item = self.sti.item(rnr, 0)
                item.setCheckState(Qt.CheckState.Checked)
            else:
                item = self.sti.item(rnr, 0)
                item.setCheckState(Qt.CheckState.Unchecked)

    def removeAllItemsTable(self):
        """
        remove all rows from list table
        :return:
        """
        for i in reversed(range(self.sti.rowCount())):
                self.sti.removeRow(i)

    def show_not_assigned_rows(self, chcontrol):
        """
        if checbox is check, show in table only rows not exist in tree
        :param chcontrol: status of checkbox control
        :return:
        """

        if chcontrol.isChecked():

            treeitems = self.get_all_tree_children()
            columns = self.columns
            #columns = self.get_all_data_table()
            #FixMe: tutaj musi pobierac w zależnosci czy filter jest pusty pelna lista
            #FixMe: gdy zawiera wartosci powinien zwracac przefiltrwana liste
            notassigned = self.set_not_assigned(treeitems, columns)
            if self.is_filter_empty():
                self.add_rowto_table(notassigned)
            else:
                self.make_filter()
        else:
            self.setrowdata(self.columns)

    def set_not_assigned(self, treeitems, columns):

        self.removeAllItemsTable()
        treeitems = list(list(b.strip().lower() for b in a) for a in treeitems)
        columns = list(list(b.strip().lower() for b in a) for a in columns)

        notassigned = []
        for nr, row in enumerate(columns):
            if row not in treeitems:
                notassigned.append(self.columns[nr])

        return notassigned


    """
    
    Form "filters" function
    
    """
    def make_assigned(self):
        self.main_form.assign_value_for_filter(self.filter_id)

    def set_filter_line_enable(self):
        """
        Make liene_filters eneble for the number of columns
        :return:
        """
        for col_nr in range(self.sti.columnCount()):
            self.line_filters[col_nr].setEnabled(True)

    def clear_all_filter_line(self):
        """
        clear all line_filter
        :return:
        """
        for fil in self.line_filters:
            fil.setText("")

    def make_filter(self):

        if self.ui.checkBoxnotassigne.checkState() == Qt.CheckState.Checked:
            rows = self.set_not_assigned(self.get_all_tree_children(), self.columns)
        else:
            rows = self.start_rows

        # if len(rows) == 0: #dlaczego rows jest 't'
        #     rows = self.start_rows

        line_texts = [lin.text() for lin in self.line_filters if lin.isEnabled()]
        filterrow = FilterRows(rows, *line_texts)
        final_list = filterrow.works_rows()

        self.removeAllItemsTable()
        self.add_rowto_table(final_list)

    def is_filter_empty(self):
        """
        check if filter line contains anny strings
        :return:
        """
        for lin in self.line_filters:
            if len(lin.text()) > 0:
                return False
        return True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = FiltersForm()
    w.show()
    sys.exit(app.exec_())
