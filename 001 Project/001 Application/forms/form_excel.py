import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt
from uiexcel import Ui_Dialog
from PySide2.QtGui import QStandardItemModel, QStandardItem

from sql.filterf import FilterF
from sql.base import Session
from sql.category import Category
from sql.competitive import Competitive
from sql.data import Data
from sql.compatitive_filter import CompativeFilterf


class ExcelForm(QDialog):
    def __init__(self, parent=None):
        super(ExcelForm, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('Generuj plik Excela')
        self.setWindowModality(Qt.ApplicationModal)

        self.cb_raport_name = self.ui.comboBox_raport_name
        self.lv_year = self.ui.listWidget_year
        self.lv_month = self.ui.listWidget_mont
        self.lv_week = self.ui.listWidget_week
        self.lv_producer = self.ui.listWidget_producer

        self.le_rows_nr = self.ui.lineEdit_rows_count
        self.le_rows_nr.setReadOnly(True)

        self.pb_excel = self.ui.pushButton_excel
        self.pb_cancel = self.ui.pushButton_close

        #signals
        self.pb_cancel.clicked.connect(self.close)
        self.cb_raport_name.currentTextChanged.connect(self.set_filter_section)

        #functions
        self.set_compatives()
        self.set_filter_section()

    def set_compatives(self):
        """
        read rows from database with competitive name
        :return:
        """
        try:
            session = Session()
            competitev = session.query(Competitive).all()

        except:
            QMessageBox.critical(self, "Błąd", "Nie można połączyć się z bazą danych")
            return

        for compet in competitev:
            self.cb_raport_name.addItem(compet.name)

        session.close()

    def set_filter_section(self):
        print('jest super')
        session = Session()
        id_nr = self.get_data_id()
        year = [ye.year for ye in session.query(Data).distinct(Data.year).filter(Data.competitive_id == id_nr).all()]
        self.set_li_value(self.lv_year, year)

        session.close()



    def get_data_id(self):

        com_name = self.cb_raport_name.currentText()

        try:
            session = Session()
            compative_id = session.query(Competitive.id).filter_by(name=com_name).one()
        except:
            QMessageBox.critical(self, "Błąd", "Nie można połączyć się z bazą danych")
            return

        session.close()
        return compative_id.id




    def set_cb_value(self, lv, value):
        """
        add value to combo box
        :param cb:
        :param value:
        :return:
        """
        lv.clear()
        cb.set
        for val in value:
            cb.addItem(str(val))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('fusion')
    w = ExcelForm()
    w.show()
    sys.exit(app.exec_())
