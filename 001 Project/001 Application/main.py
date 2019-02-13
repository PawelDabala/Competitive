from PySide2 import QtCore, QtGui, QtWidgets

import main_rc
from filechose import FileChoser

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.filechoser = FileChoser(self)
        self.setWindowTitle("VW Competitive")
        self.setWindowIcon(QtGui.QIcon(':/images/vw.png'))

        self.textEdit = QtWidgets.QTextEdit()
        self.setCentralWidget(self.textEdit)

        self.createActions()
        self.createMenus()
        self.createStatusBar()

        self.readSettings()

    def closeEvent(self, event):
        self.close()

    def open(self):
        print("open")
        self.filechoser.show()

    def save(self, ti):
        print("save file", ti)
        ### !!!!! TUTAJ BĘDZIE ZAPIS DO BAZY !!!!!!!
        # if self.curFile:
        #     return self.saveFile(self.curFile)
        #
        # return self.saveAs()

    def createActions(self):
        self.openAct = QtWidgets.QAction(QtGui.QIcon(':/images/open.png'),
                "&Otwórz...", self, shortcut=QtGui.QKeySequence.Open,
                statusTip="Otwóż nowe pliki", triggered=self.open)

        self.saveAct = QtWidgets.QAction(QtGui.QIcon(':/images/save.png'),
                "&Zapisz...", self, shortcut=QtGui.QKeySequence.Save,
                statusTip="Zapisz plik", triggered=self.save)

        self.exitAct = QtWidgets.QAction("&Zamknij", self, shortcut="Ctrl+Q",
                statusTip="Zamknij aplikacje", triggered=self.close)


    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu("&Plik")
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addAction(self.saveAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAct)

    def createStatusBar(self):
        self.statusBar().showMessage("Ready")

    def readSettings(self):
        settings = QtCore.QSettings("Trolltech", "Application Example")
        pos = settings.value("pos", QtCore.QPoint(200, 200))
        size = settings.value("size", QtCore.QSize(400, 400))
        self.resize(size)
        self.move(pos)

if __name__ == '__main__':

    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('fusion')
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
