import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtGui import QStandardItemModel, QStandardItem, QBrush, QColor
from PySide2.QtWidgets import QTableView, QMainWindow, QHBoxLayout, QPushButton
from PySide2.QtCore import Qt




class Window(QtWidgets.QWidget):
    """
    zmiana nagłówka działa tylko dla stylu fusion, działa tylko dla stylu 'fusion"
    """
    def __init__(self):
        super(Window, self).__init__()

        self.table = QTableView()
        self.sti = QStandardItemModel()
        self.sti.setColumnCount(3)
        self.table.setModel(self.sti)

        self.sti.setRowCount(8)

        #piersza możliwośc przez QStandardItem
        # item1 = QStandardItem('Red')
        # item1.setBackground(QBrush(Qt.red))
        # self.sti.setHorizontalHeaderItem(1, item1)

        #Druga możliwosć przez odwołanie modelu:
        self.table.model().setHeaderData(0, Qt.Horizontal, QBrush(QColor(121, 166, 210)), Qt.BackgroundRole)
        self.table.model().setHeaderData(0, Qt.Horizontal, "One", Qt.DisplayRole)

        self.mlayout = QHBoxLayout()
        self.mlayout.addWidget(self.table)

        self.setLayout(self.mlayout)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('fusion')
    window = Window()
    window.show()
    sys.exit(app.exec_())


