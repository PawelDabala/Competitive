from PySide2 import QtCore, QtGui, QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.mainLayout = QtWidgets.QHBoxLayout()

        self.labelOne = QtWidgets.QLabel("One")
        self.layoutOne = QtWidgets.QHBoxLayout()
        self.layoutOne.addWidget(self.labelOne)

        self.labelTwo = QtWidgets.QLabel("Two")
        self.layoutTwo = QtWidgets.QHBoxLayout()
        self.layoutTwo.addWidget(self.labelTwo)

        self.mainLayout.addLayout(self.layoutOne,)
        self.mainLayout.addLayout(self.layoutTwo)

        self.setLayout(self.mainLayout)
        self.resize(500,450)

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())







