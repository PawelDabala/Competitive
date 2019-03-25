import sys, os
from PySide2 import QtCore, QtGui, QtWidgets
app=QtWidgets.QApplication(sys.argv)


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self):
        QtCore.QAbstractTableModel.__init__(self)

        self.items=['One','Two','Three','Four','Five','Six','Seven']

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.items)
    def columnCount(self, index=QtCore.QModelIndex()):
        return 1

    def data(self, index, role):
        if not index.isValid() or not (0<=index.row()<len(self.items)):
            return QtCore.QVariant()

        item=str(self.items[index.row()])

        if role==QtCore.Qt.UserRole:
            return item

        if role==QtCore.Qt.DisplayRole:
            return item

        if role==QtCore.Qt.TextColorRole:
            return QtCore.QVariant(QtGui.QColor(QtCore.Qt.white))

        if role == QtCore.Qt.BackgroundRole:
            if index.row()%2:
                return QtCore.QVariant(QtGui.QColor(QtCore.Qt.gray))
            else:
                return QtCore.QVariant(QtGui.QColor(QtCore.Qt.darkGray))

        if role == QtCore.Qt.TextAlignmentRole:
            return (QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

    def headerData(self, column, orientation, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.TextAlignmentRole:
            return (QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        if role == QtCore.Qt.BackgroundRole:
            return QtCore.QVariant(QtGui.QColor(QtCore.Qt.blue))

        if role == QtCore.Qt.ForegroundRole:
            if orientation == QtCore.Qt.Horizontal:
                return QtCore.QVariant(QtGui.QColor(QtCore.Qt.red))
            elif orientation == QtCore.Qt.Vertical:
                return QtCore.QVariant(QtGui.QColor(QtCore.Qt.green))

        if role == QtCore.Qt.DisplayRole and orientation == QtCore.Qt.Horizontal:
            return QtCore.QString('Horizont Column')

        if role == QtCore.Qt.DisplayRole and orientation == QtCore.Qt.Vertical:
            return QtCore.QString('Vertical Column')

        if role == QtCore.Qt.FontRole:
            return QtGui.QFont('Times', pointSize=5, weight=-1, italic=True)


class TableView(QtWidgets.QTableView):
    def __init__(self, parent=None):
        super(TableView, self).__init__(parent)

        # self.horizontalHeader().setResizeMode(self.QHeaderView.Stretch)

        myModel=TableModel()
        self.setModel(myModel)

view=TableView()
view.show()
sys.exit(app.exec_())