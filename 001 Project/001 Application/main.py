#from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QPoint, QSize, QSettings, SIGNAL, Qt
from PySide2.QtWidgets import QTableView, QAction, QApplication, QMainWindow, QMessageBox, \
    QHeaderView
from PySide2.QtGui import QStandardItem, QStandardItemModel, QIcon, QKeySequence, QFont, QBrush, QColor
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
                        'Channel type',
                        'Wyprz',
                        'Upus',
                        'Rabat',
                        'Wyprze Upust Rabat',
                        'Model',
                        'Brand final',
                        'Subbrand (brand+Model)',
                        'Brand Type',
                        'Segment_detailed',
                        'Segment',
                        'Segment_combined',
                        'Campaign Type'
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
        self.set_color_on_header()

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

        self.runWordFilter = QAction("Filtry &Automatyczne",
                                     shortcut="Ctrl+A",
                                     statusTip="Urchom filtry automatyczne",
                                     triggered=self.run_filters)


    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu("&Plik")
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addAction(self.saveAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAct)

        self.filterMenu = self.menuBar().addMenu("&Filtr")
        self.filterMenu.addAction(self.runWordFilter)

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

    def showfilterforms(self, i):
        """
        Show filters for collumn nr"
        :param i:
        :return:
        """
        session = Session()
        filter_ = session.query(FilterF).filter_by(column_nr=i).one_or_none()
        if filter_ is not None and filter_.type == 'manual':
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

    def replace_column(self, col_nr, assignded_column):
        """
        replace column with new data
        :param col_nr:
        :param assignded_column:
        :return:
        """
        self.sti.takeColumn(col_nr)
        self.sti.insertColumn(col_nr, assignded_column)
        self.sti.setHorizontalHeaderLabels(self.headers)
        self.set_color_on_header()


    """
    
    Filters
    
    """

    def assign_value_for_filter(self, filter_id):
        """
        preper list with value from main filter, send to make_filter_list.
        Replace column for filter_id with column with assigned data
        :param filter_id:
        :return:
        """
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
        session.close()
        self.set_color_on_header()
        QMessageBox.information(self, "Informacja", "Operacja zakończona.")

    @staticmethod
    def make_filter_list(filter_id, rows):
        """
        make list with assigned value
        :param filter_id:
        :param rows:
        :return:
        """
        session = Session()
        filter_ = session.query(FilterF).get(filter_id)

        ready_valus = []
        for row in rows:
            flag =False
            row = [i.strip().lower() for i in row]
            for category in filter_.categorys:
                items = [[b.strip().lower() for b in a] for a in category.items]
                if row in items:
                    #make QStandardItem to make column in sti model
                    item = QStandardItem(str(category.name))
                    ready_valus.append(item)
                    flag = True
            if flag is False:
                item = QStandardItem('')
                ready_valus.append(item)

        session.close()
        return ready_valus

    """
    filters: words, cut
    """

    def run_filters(self):
        """
        make filters
        :return:
        """
        session = Session()
        # filters_ = session.query(FilterF).filter_by(type='words').all()
        filters_ = session.query(FilterF).all()
        for fil in filters_:

            if fil.type == 'words':
                rows = self.get_data_from_columns(fil.columns)
                assignded_column = self.make_words_list(fil.id, rows)
                self.replace_column(fil.column_nr, assignded_column)

            elif fil.type == 'cut':
                if fil.name == 'model':
                    rows = self.get_data_from_columns(fil.columns)
                    assignded_column = self.filter_cut_model(rows)
                    self.replace_column(fil.column_nr, assignded_column)

                elif fil.name == 'subbrand_brand_model':
                    rows = self.get_data_from_columns(fil.columns)
                    assignded_column = self.join_columns(rows)
                    self.replace_column(fil.column_nr, assignded_column)

        session.close()
        QMessageBox.information(self, "Informacja", "Operacja zakończona.")

    def get_data_from_columns(self, columns_nr):
        """
        get data for sending columns
        :param columns_nr:
        :return: return list of value from table
        """
        rows = []
        for row in range(self.sti.rowCount()):
            row_value=[]
            for col in columns_nr:
                if self.sti.item(row, col) is not None:
                    row_value.append(self.sti.item(row, col).text())
                else:
                    row_value.append('')
            # row_value = [self.sti.item(row, col).text() for col in columns_nr]
            rows.append(row_value)
        return rows

    @staticmethod
    def make_words_list(filter_id, rows):
        """
        make words list for filters,
        if find word in list assigned name of category
        :param filter_id:
        :param rows:
        :return:
        """

        session = Session()
        filter_ = session.query(FilterF).get(filter_id)

        ready_valus = []
        for row in rows:
            flag = False
            row = [i.lower() for i in row]
            row = ' '.join(row)
            for category in filter_.categorys:
                words = [b.lower() for b in category.words]
                for word in words:
                    if word in row:
                        item = QStandardItem(str(category.name))
                        ready_valus.append(item)
                        flag = True
                        break
            if flag is False:
                item = QStandardItem('')
                ready_valus.append(item)

        session.close()
        return ready_valus

    def filter_cut_model(self, rows):
        """
        cut ferst word from string
        :param rows:
        :return:
        """
        ready_values = []
        for row in rows:
            item = QStandardItem((row[1].replace(row[0], '')).strip())
            ready_values.append(item)

        return ready_values

    def join_columns(self, rows):
        """
        join column in list rows
        """
        temp = [QStandardItem(' '.join(x)) for x in rows]
        return temp




    def set_color_on_header(self):
        """
        changes the color of the header
        :return:
        """

        session = Session()
        filtersf= session.query(FilterF).all()

        for filterf in filtersf:
            if filterf.type == 'manual':
                self.table.model().setHeaderData(filterf.column_nr, Qt.Horizontal, QBrush(QColor(121, 166, 210)), Qt.BackgroundRole )
                self.table.model().setHeaderData(filterf.column_nr, Qt.Horizontal, self.headers[filterf.column_nr], Qt.DisplayRole)
            if filterf.type in ('words', 'cut'):
                self.table.model().setHeaderData(filterf.column_nr, Qt.Horizontal, QBrush(QColor(212, 214, 219)),
                                                 Qt.BackgroundRole)
                self.table.model().setHeaderData(filterf.column_nr, Qt.Horizontal, self.headers[filterf.column_nr],
                                                 Qt.DisplayRole)
        session.close()



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    app.setStyle('fusion')
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
