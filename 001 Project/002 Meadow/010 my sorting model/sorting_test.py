from PySide2 import QtCore, QtGui, QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__()


        self.proxyView = QtWidgets.QTableView()

        self.proxyView.setSortingEnabled(True)

        self.sti = QtGui.QStandardItemModel()
        self.sti.setHorizontalHeaderLabels(['Imie', 'Nazwisko','Miasto'])

        names = ['Ania', 'Hania', 'Ewa', 'Klara', 'Ewa']
        last_names = ['Kowalska', 'Michalkiewicz', 'Rzeromska', 'Janik', 'Kazimierczuk']
        city = ['Warszawa', 'Lodz', 'Gdansk', 'Wrocław', 'Wieliczka']

        for nr, name in enumerate(names):
            item = QtGui.QStandardItem(name)
            self.sti.setItem(nr, 0, item)

        for nr, lname in enumerate(last_names):
            item = QtGui.QStandardItem(lname)
            self.sti.setItem(nr, 1, item)

        for nr, lname in enumerate(city):
            item = QtGui.QStandardItem(lname)
            self.sti.setItem(nr, 2, item)

        self.proxyView.setModel(self.sti)

        self.filterOne = QtWidgets.QLineEdit()
        self.filterTwo = QtWidgets.QLineEdit()
        self.filterThree = QtWidgets.QLineEdit()
        self.butcheck = QtWidgets.QPushButton("Check")

        self.filterLayout = QtWidgets.QHBoxLayout()
        self.filterLayout.addWidget(self.filterOne)
        self.filterLayout.addWidget(self.filterTwo)
        self.filterLayout.addWidget(self.filterThree)
        self.filterLayout.addWidget(self.butcheck)

        self.orginal_list = self.get_all_rows()

        # #coment: SIGNALS
        self.filterOne.textChanged.connect(self.make_filter)
        self.filterTwo.textChanged.connect(self.make_filter)
        self.filterThree.textChanged.connect(self.make_filter)
        self.filterThree.setClearButtonEnabled(True)
        self.filterThree.setEnabled(False)
        self.butcheck.clicked.connect(self.make_filter)

        sourceLayout = QtWidgets.QVBoxLayout()
        sourceLayout.addWidget(self.proxyView)
        sourceLayout.addLayout(self.filterLayout)

        self.setWindowTitle('Basic Sort/Filter Model')
        self.resize(500, 550)
        self.setLayout(sourceLayout)

    def get_all_rows(self):

        rows = []
        for row in range(self.sti.rowCount()):
            cells = []
            for col in range(self.sti.columnCount()):
                cells.append(self.sti.item(row, col).text())
            rows.append(cells)

        return rows

    def make_filter(self):

        filterrow = FilterRows(self.orginal_list,
                               self.filterOne.text(),
                               self.filterTwo.text(),
                               self.filterThree.text())
        final_list = filterrow.works_rows()

        self.populate_rows(final_list)

    def populate_rows(self, final_list):

        #delete all rows
        for row in reversed(range(self.sti.rowCount())):
            self.sti.removeRow(row)

        # if len(final_list) == 0:
        #     final_list = self.orginal_list

        for nr_row, row in enumerate(final_list):
            for nr_col, col in enumerate(row):
                item = QtGui.QStandardItem(col)
                self.sti.setItem(nr_row, nr_col, item)


class FilterRows:

    def __init__(self, org_list, *args):
        self.org_list = org_list
        self.lineedits = args
        self.returnlist = []


    def works_rows(self):
        for row in self.org_list:
            if self.check_rows(row):
                self.returnlist.append(row)

        return self.returnlist

    def check_rows(self, row):
        nr_cell = 0
        for nr, cell in enumerate(row):
            if self.check_cell(nr, cell):
                nr_cell += 1
        #
        if nr_cell == len(self.lineedits):
            return True
        else:
            return False


    def check_cell(self,nr, cell):
        #jezeli nie wypelniono pola
        if len(self.lineedits[nr]) == 0:
            return True

        if self.lineedits[nr].lower() in cell.lower():
            return True
        else:
            return False



if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())







