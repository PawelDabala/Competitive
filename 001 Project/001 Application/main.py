#from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QPoint, QSize, QSettings, SIGNAL
from PySide2.QtWidgets import QTableView, QAction, QApplication, QMainWindow, QMessageBox, \
    QHeaderView
from PySide2.QtGui import QStandardItem, QStandardItemModel, QIcon, QKeySequence, QFont
from filechose import FileChoser
from excel import Excel
from sql.data import Data
from sql.competitive import Competitive
from sql.filterf import FilterF
from sql.base import Session
from forms.filters import FiltersForm


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
        self.sti.setColumnCount(6)
        self.table.setModel(self.sti)
        self.table.verticalHeader().setDefaultSectionSize(10)
        self.table.horizontalHeader().setDefaultSectionSize(200)
        self.headers = ['Year',
                        'Month',
                        'Week',
                        'Sector',
                        'Category',
                        'Sub Category',
                        'Produkt(4)',
                        'Branża(I)',
                        'Kategoria(II)',
                        'Dział(III)',
                        'Producer',
                        'Brand',
                        'Sub Brand',
                        'Film Code',
                        'Film Code 2',
                        'Media',
                        'Glowne Medium',
                        'Medium',
                        'Wydawca Nadawca',
                        'Periodyczność',
                        'Duration',
                        'Typ reklamy',
                        'Forma Reklamy',
                        'Typ Strony',
                        'L.emisji',
                        'Sum.Str',
                        'Cost',
                        'PT/OFF',
                        'TRP',
                        'TRP30',
                        'Count',
                        'Channel group',
                        'Channel type'
                        ]
        self.sti.setHorizontalHeaderLabels(self.headers)
        self.sti.setColumnCount(len(self.headers))
        #self.table.setSortingEnabled(True)
        #self.table.horizontalHeader().connect()
        self.connect(self.table.horizontalHeader(), SIGNAL("sectionClicked(int)"), self.showfilterforms)

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
        """
        save data to data base
        :return:
        """
        #deleta rows from data base for compative name
        session = Session()
        comat = session.query(Competitive).filter(Competitive.name.ilike(f'%{self.compative_name}%')).first()
        session.query(Data).filter_by(competitive_id=comat.id).delete()

        #read data from row and save to data base
        for row in range(self.sti.rowCount()):
            datas = []
            for col in range(self.sti.columnCount()):
                if col in (0, 1, 2, 20, 24, 30):
                    try:
                        #tutaj poprawic nie chce wpisać
                        if self.sti.item(row, col) is not None:
                            datas.append(int(self.sti.item(row, col).text()))
                        else:
                            datas.append(None)
                    except ValueError:
                        datas.append(None)
                elif col in (25, 26, 28, 29):
                    try:
                        if self.sti.item(row, col) is not None:
                            datas.append(float(self.sti.item(row, col).text()))
                        else:
                            datas.append(None)
                    except ValueError:
                        datas.append(None)
                else:
                    if self.sti.item(row, col) is not None:
                        datas.append(self.sti.item(row, col).text())
                    else:
                        datas.append(None)

            comat.datas.append(Data(*datas))

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
        self.compativedata = session.query(Competitive).filter_by(name=compative_name).first()

        self.populate_row()
        session.close()

    def populate_row(self):
        """
        read data from compatiedate, techegedata, adxpert and past to rows
        :return:
        """
        # without this section data in column one don't show
        self.sti.setRowCount(0)
        self.sti.setRowCount(1)

        font = QFont()
        font.setPointSize(8)

        #add data from data base
        if self.compativedata:
            for row in self.compativedata.datas:
                rownr = self.sti.rowCount()
                rowvalue = row.values()
                for nr, value in enumerate(rowvalue):
                    item = QStandardItem(f'{value}')
                    item.setFont(font)
                    self.sti.setItem(rownr-1, nr, item)
                    self.sti.setRowCount(rownr + 1)

        #add data from techegedata
        if self.techegedata:
            for rownr in range(len(self.techegedata[0])):
                self.sti.setRowCount(self.sti.rowCount()+1)
                for colnr in range(len(self.techegedata)):
                    if len(self.techegedata[colnr]) == 0:
                        continue
                    item = QStandardItem(f'{self.techegedata[colnr][rownr]}')
                    item.setFont(font)
                    self.sti.setItem(self.sti.rowCount()-2, colnr, item)

        #add data from adexpert
        if self.adxpert:
            for rownr in range(len(self.adxpert[0])):
                self.sti.setRowCount(self.sti.rowCount()+1)
                for colnr in range(len(self.adxpert)):
                    if len(self.adxpert[colnr]) == 0:
                        continue
                    item = QStandardItem(f'{self.adxpert[colnr][rownr]}')
                    item.setFont(font)
                    self.sti.setItem(self.sti.rowCount()-2, colnr, item)

        self.sti.removeRow(self.sti.rowCount()-1)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        """
        Mozna zrobić tak ale wolał bym w nagłowku
        """
        # but = QPushButton("Button")
        # self.table.setIndexWidget(self.sti.index(0, 3), but)
        # but.clicked.connect(self.TestBut)

    def showfilterforms(self, i):
        session = Session()
        filter_ = session.query(FilterF).filter_by(column_nr=i).one_or_none()
        if filter_ is not None:
            columns = self.prapercolumns(filter_.columns)
            headersname = [self.headers[i] for i in filter_.columns]
            self.filter = FiltersForm(filter_.id, columns, headersname, self)
            self.filter.show()

        session.close()

    def prapercolumns(self, columns):
        """
        get unic data from sending columns
        :param args:
        :return:
        """
        mainlist = []
        for col in columns:
            collist = []
            for row in range(self.sti.rowCount()):
                if row == 0:
                    continue
                collist.append(self.sti.item(row, col).text())
            mainlist.append(collist)

        return list(set(zip(*mainlist)))

    def assign_value_for_filter(self, filter_id):
        session = Session()
        filter_ = session.query(FilterF).get(filter_id)
        rows = []
        for row in range(self.sti.rowCount()):
            row_value = [self.sti.item(row, col).text() for col in filter_.columns]
            rows.append(row_value)

        read_rows = self.make_filter_list(filter_id, rows)
        col_nr = filter_.column_nr
        self.sti.takeColumn(col_nr)
        self.sti.insertColumn(col_nr, read_rows)
        self.sti.setHorizontalHeaderLabels(self.headers)
        # #FIXME: it work but very slow
        # for nr, newrow in enumerate(read_rows):
        #     item = QStandardItem(str(newrow))
        #     print(nr, item.text())
        #     self.sti.setItem(nr, col_nr, item)
        #     # self.sti.item(newrow, filter_.column_nr).setText(newrow)
        session.close()
        QMessageBox.information(self, "Informacja", "Operacja zakończona.")

    @staticmethod
    def make_filter_list(filter_id, rows):
        session = Session()
        filter_ = session.query(FilterF).get(filter_id)

        ready_valus = []
        for row in rows:
            flag =False
            for category in filter_.categorys:
                if row in category.items:
                    item = QStandardItem(str(category.name))
                    ready_valus.append(item)
                    flag = True
            if flag is False:
                item = QStandardItem('')
                ready_valus.append(item)

        session.close()
        return ready_valus


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    app.setStyle('fusion')
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
