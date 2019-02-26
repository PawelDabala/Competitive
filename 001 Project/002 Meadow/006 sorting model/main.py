from PySide2 import QtCore, QtGui, QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.proxyModel= QtCore.QSortFilterProxyModel()
        self.proxyModel.setDynamicSortFilter(True)

        self.sourceGroupBox = QtWidgets.QGroupBox("Original Model")
        self.proxyGroupBox = QtWidgets.QGroupBox("Sort/Filtered Model")

        self.sourceView = QtWidgets.QTreeView()
        self.sourceView.setRootIsDecorated(False)
        self.sourceView.setAlternatingRowColors(True)

        self.proxyView = QtWidgets.QTreeView()
        self.proxyView.setRootIsDecorated(False)
        self.proxyView.setAlternatingRowColors(True)
        self.proxyView.setModel(self.proxyModel)
        self.proxyView.setSortingEnabled(True)

        self.sortCaseSensitivityCheckBox = QtWidgets.QCheckBox("Case sensitive sorting")
        self.filterCaseSensitivityCheckBox = QtWidgets.QCheckBox("Case sensitive filter")

        self.filterPatternLineEdit = QtWidgets.QLineEdit()
        self.filterPatternLabel =QtWidgets.QLabel("&Filter pattern:")
        self.filterPatternLabel.setBuddy(self.filterPatternLineEdit)

        self.filterSyntaxComboBox = QtWidgets.QComboBox()
        self.filterSyntaxComboBox.addItem("Regular expression",
                            QtCore.QRegExp.RegExp)
        self.filterSyntaxComboBox.addItem("Wildcard",
                                QtCore.QRegExp.RegExp)
        self.filterSyntaxComboBox.addItem("Fixed string",
                                QtCore.QRegExp.FixedString)
        self.filterSynaxLabel = QtWidgets.QLabel("Filter &syntax:")
        self.filterSynaxLabel.setBuddy(self.filterSyntaxComboBox)
        









if __name__ == '__main__':

    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.setSourceModel(createMailModel(window))
    window.show()
    sys.exit(app.exec_())