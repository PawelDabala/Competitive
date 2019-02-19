#from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QPoint, QSize, QSettings
from PySide2.QtWidgets import QTableWidgetItem, QTableView, QAction, QApplication, QMainWindow
from PySide2.QtGui import QStandardItem, QStandardItemModel, QIcon, QKeySequence
from filechose import FileChoser
from excel import Excel
from pprint import pprint

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.filechoser = FileChoser(self)
        self.setWindowTitle("VW Competitive")
        self.setWindowIcon(QIcon(':/images/vw.png'))

        """
        Test wstawienia wartosci do tabeli
        """
        self.table = QTableView()
        # self.setCentralWidget(self.table)
        # self.sti = QStandardItemModel()
        # self.sti.setRowCount(1000)
        # self.sti.setColumnCount(50)
        # for i in range(self.sti.rowCount()):
        #     item = QStandardItem(f' row {i}')
        #     self.sti.setItem(i, 0, item)
        #
        # self.table.setModel(self.sti)
        self.table.verticalHeader().setDefaultSectionSize(10)
        self.table.horizontalHeader().setDefaultSectionSize(200)

        self.createActions()
        self.createMenus()
        self.createStatusBar()

        self.readSettings()

    def closeEvent(self, event):
        self.close()

    def open(self):
        self.filechoser.show()

    def save(self, ti):
        pass
        ### !!!!! TUTAJ BĘDZIE ZAPIS DO BAZY !!!!!!! ADD!!!
        # if self.curFile:
        #     return self.saveFile(self.curFile)
        #
        # return self.saveAs()

    def createActions(self):
        self.openAct = QAction(QIcon(':/images/open.png'),
                "&Otwórz...", self, shortcut=QKeySequence.Open,
                statusTip="Otwóż nowe pliki", triggered=self.open)

        self.saveAct = QAction(QIcon(':/images/save.png'),
                "&Zapisz...", self, shortcut=QKeySequence.Save,
                statusTip="Zapisz plik", triggered=self.save)

        self.exitAct = QAction("&Zamknij", self, shortcut="Ctrl+Q",
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
        settings = QSettings("Trolltech", "Application Example")
        pos = settings.value("pos", QPoint(200, 200))
        size = settings.value("size", QSize(400, 400))
        self.resize(size)
        self.move(pos)

    def get_data(self, paths, compative_name):
        """
        receives data from the filechose form
        :param paths: dictionary with paht to techege, adexpert
        :param compative_name: name of raport
        :return:
        """
        pprint(paths[0])
        self.compative_name = compative_name
        self.techegedata = Excel.get_data_from_techedge(paths[0])
        print(self.techegedata)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    app.setStyle('fusion')
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
