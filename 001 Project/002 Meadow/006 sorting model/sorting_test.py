from PySide2 import QtCore, QtGui, QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.proxyModel = QtCore.QSortFilterProxyModel()
        self.proxyModel.setDynamicSortFilter(True)

        self.proxyView = QtWidgets.QTableView()
        self.proxyView.setModel(self.proxyModel)
        self.proxyView.setSortingEnabled(True)

        self.sti = QtGui.QStandardItemModel()
        self.sti.setHorizontalHeaderLabels(['Imie', 'Nazwisko'])

        names = ['Ania', 'Hania', 'Ewa', 'Klara', 'Ewa']
        last_names = ['Kowalska', 'Michalkiewicz', 'Rzeromska', 'Janik', 'Kazimierczuk']

        for nr, name in enumerate(names):
            item = QtGui.QStandardItem(name)
            self.sti.setItem(nr, 0, item)

        for nr, lname in enumerate(last_names):
            item = QtGui.QStandardItem(lname)
            self.sti.setItem(nr, 1, item)

        self.proxyModel.setSourceModel(self.sti)

        self.filterOne = QtWidgets.QLineEdit()
        self.filterTwo = QtWidgets.QLineEdit()

        self.filterLayout = QtWidgets.QHBoxLayout()
        self.filterLayout.addWidget(self.filterOne)
        self.filterLayout.addWidget(self.filterTwo)

        #coment: SIGNALS
        self.filterOne.textChanged.connect(self.filterRegExpChanged)
        self.filterTwo.textChanged.connect(self.filterRegExpChanged2)

        sourceLayout = QtWidgets.QVBoxLayout()
        sourceLayout.addWidget(self.proxyView)
        sourceLayout.addLayout(self.filterLayout)

        self.setWindowTitle('Basic Sort/Filter Model')
        self.resize(500, 550)
        self.setLayout(sourceLayout)

    def filterRegExpChanged(self):
        print("filterRegExpChanged")
        syntax_nr = QtCore.QRegExp.RegExp
        syntax = QtCore.QRegExp.PatternSyntax(syntax_nr)
        caseSensitivity = QtCore.Qt.CaseInsensitive

        regExp =QtCore.QRegExp(self.filterOne.text(),
                               caseSensitivity,
                               syntax)
        self.proxyModel.setFilterRegExp(regExp)
        self.proxyModel.setFilterKeyColumn(0)

    def filterRegExpChanged2(self):
        print("filterRegExpChanged2")

        syntax_nr = QtCore.QRegExp.RegExp
        syntax = QtCore.QRegExp.PatternSyntax(syntax_nr)
        caseSensitivity = QtCore.Qt.CaseInsensitive

        regExp =QtCore.QRegExp(self.filterTwo.text(),
                               caseSensitivity,
                               syntax)
        self.proxyModel.setFilterRegExp(regExp)
        self.proxyModel.setFilterKeyColumn(1)






if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())







