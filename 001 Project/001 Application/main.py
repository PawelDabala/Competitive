#from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QPoint, QSize, QSettings
from PySide2.QtWidgets import QTableWidgetItem, QTableView, QAction, QApplication, QMainWindow, QMessageBox
from PySide2.QtGui import QStandardItem, QStandardItemModel, QIcon, QKeySequence, QFont
from filechose import FileChoser
from excel import Excel
from sql.data import Data
from sql.competitive import Competitive
from sql.base import Session

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
        self.setCentralWidget(self.table)
        self.sti = QStandardItemModel()
        # self.sti.setRowCount(1000)
        # self.sti.setColumnCount(50)
        # for i in range(self.sti.rowCount()):
        #     item = QStandardItem(f' row {i}')
        #     self.sti.setItem(i, 0, item)
        self.sti.setColumnCount(4)
        self.table.setModel(self.sti)
        self.table.verticalHeader().setDefaultSectionSize(10)
        self.table.horizontalHeader().setDefaultSectionSize(200)


        #print(self.sti.rowCount())

        self.createActions()
        self.createMenus()
        self.createStatusBar()

        self.readSettings()

    def closeEvent(self, event):
        self.close()

    def open(self):
        self.filechoser.show()
        self.filechoser.clead_data()

    def save(self):
        #deleta rows from data base for compative name
        session = Session()
        comat = session.query(Competitive).filter(Competitive.name.ilike(f'%{self.compative_name}%')).first()
        session.query(Data).filter_by(competitive_id=comat.id).delete()

        #read data from row and save to data base
        for row in range(self.sti.rowCount())[1:]:
            # name1.datas.append(Data(2019, 11, "Audi", "Stary film"))
            comat.datas.append(
                Data(
                int(self.sti.item(row, 0).text()),
                int(self.sti.item(row, 1).text()),
                self.sti.item(row, 2).text(),
                self.sti.item(row, 3).text()
                )
            )

        session.commit()
        session.close()
        QMessageBox.information(self, "Zapis", "Zapis zakonczyl się powodzeniem.")

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
        size = settings.value("size", QSize(800, 800))
        self.resize(size)
        self.move(pos)

    def get_data(self, paths, compative_name):
        """
        receives data from the filechose form
        :param paths: dictionary with paht to techege, adexpert
        :param compative_name: name of raport
        :return:
        """
        self.compative_name = compative_name
        if len(paths[0]) > 0:
            self.techegedata = Excel.get_data(paths[0])
        else:
            self.techegedata = None
        if len(paths[1]) > 0:
            self.adxpert = Excel.get_data(paths[1], False)
        else:
            self.adxpert = None

        #wczytanie arkusza z bazy danych
        session = Session()
        self.compativedata = session.query(Competitive).filter(Competitive.name.ilike(f'{compative_name}%')).scalar()

        self.populate_row()
        session.close()

    def populate_row(self):
        """
        read data from compatiedate, techegedata, adxpert and past to rows
        :return:
        """
        # without this section data in column one don't show
        self.sti.setRowCount(0)
        self.sti.setRowCount(2)

        #add data from data base
        if self.compativedata:
            for row in self.compativedata.datas:
                rownr = self.sti.rowCount()
                rowvalue = row.values()
                for nr, value in enumerate(rowvalue):
                    item = QStandardItem(f'{value}')
                    font = QFont()
                    font.setPointSize(8)
                    item.setFont(font)
                    self.sti.setItem(rownr-1, nr, item)
                    self.sti.setRowCount(rownr + 1)

        #add data from techegedata
        if self.techegedata:
            for rownr in range(len(self.techegedata[0])):
                self.sti.setRowCount(self.sti.rowCount()+1)
                for colnr in range(len(self.techegedata)):
                    item = QStandardItem(f'{self.techegedata[colnr][rownr]}')
                    font = QFont()
                    font.setPointSize(8)
                    item.setFont(font)
                    self.sti.setItem(self.sti.rowCount()-2, colnr, item)

        #add data from adexpert
        if self.adxpert:
            for rownr in range(len(self.adxpert[0])):
                self.sti.setRowCount(self.sti.rowCount()+1)
                for colnr in range(len(self.adxpert)):
                    item = QStandardItem(f'{self.adxpert[colnr][rownr]}')
                    font = QFont()
                    font.setPointSize(8)
                    item.setFont(font)
                    self.sti.setItem(self.sti.rowCount()-2, colnr, item)

        self.sti.removeRow(self.sti.rowCount()-1)










if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    app.setStyle('fusion')
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
