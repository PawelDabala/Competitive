import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt
from uifilltes_manage import Ui_Dialog

from sqlalchemy import and_
from sql.filterf import FilterF
from sql.base import Session
# from sql.category import Category
# from sql.competitive import Competitive
# from sql.data import Data
# from sql.compatitive_filter import CompativeFilterf


class FiltersManager(QDialog):
    def __init__(self, parent=None):
        super(FiltersManager, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('Filtry Manualne')
        self.main = parent

        self.lw_filters = self.ui.listWidget_filters
        self.chb_all = self.ui.checkBox_checkall
        self.pb_run = self.ui.pushButton_run
        self.pb_close = self.ui.pushButton_close

        #Signals
        self.pb_close.clicked.connect(self.close)
        self.pb_run.clicked.connect(self.run_filtes)
        self.chb_all.stateChanged.connect(lambda: self.select_deselect_items(self.chb_all))

        #functions
        self.get_filters()

        #setings
        self.chb_all.setText("Odznacz")
        self.chb_all.setCheckState(Qt.Checked)

    def get_filters(self):
        """
        connect to data base and get all manual filters
        """

        try:
            session = Session()
            filters = session.query(FilterF).filter_by(type='manual').all()
        except:
            QMessageBox.critical(self, 'Bład', 'Brak połaczenia z baza danych')

        filter_name = [fil.name for fil in filters]
        self.set_cb_value(self.lw_filters, filter_name)
        session.close()


    def set_cb_value(self, lv, value):
        """
        add value to combo box
        :param cb:
        :param value:
        :return:
        """
        lv.clear()
        for val in value:
            item = QListWidgetItem(str(val))
            item.setCheckState(Qt.Checked)
            lv.addItem(item)

    def select_deselect_items(self, chcontrol):
        """
        check or unchecked checkbox in lw
        :param chcontrol:
        :return:
        """

        if chcontrol.isChecked():
            self.chb_all.setText("Odznacz")
            for rnr in range(self.lw_filters.count()):
                item = self.lw_filters.item(rnr)
                item.setCheckState(Qt.Checked)
        else:
            self.chb_all.setText("Zaznacz")
            for rnr in range(self.lw_filters.count()):
                item = self.lw_filters.item(rnr)
                item.setCheckState(Qt.Unchecked)

    def get_checked_items(self, lw):
        """
        :param lw: ListWidget
        :return: list of checked items
        """
        chitems = []
        for rnr in range(lw.count()):
            item = lw.item(rnr)
            if item.checkState() == Qt.Checked:
                chitems.append(item.text())

        return chitems

    def run_filtes(self):
        """
        run assign function from main form for all checked filters id.
        """

        chitems = self.get_checked_items(self.lw_filters)
        session = Session()
        filter_id = [fil.id for fil in session.query(FilterF).filter(FilterF.name.in_(chitems)).all()]

        #start assign
        for id in filter_id:
            self.main.assign_value_for_filter(id, False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('fusion')
    w = FiltersManager()
    w.show()
    sys.exit(app.exec_())

