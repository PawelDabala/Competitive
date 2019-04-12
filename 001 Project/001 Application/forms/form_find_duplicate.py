import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt
from uifind_duplicate import Ui_Dialog

from sqlalchemy import and_
from sql.filterf import FilterF
from sql.base import Session
from sql.category import Category
from sql.competitive import Competitive
from sql.data import Data
from sql.compatitive_filter import CompativeFilterf


class FindDuplicate(QDialog):
    def __init__(self, parent=None):
        super(FindDuplicate, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('Znajdz duplikaty')

        self.cb_raports = self.ui.comboBox_raports_name
        self.li_nr_dup = self.ui.lineEdit_duplicate_nr
        self.pb_find = self.ui.pushButton_find
        self.pb_remove = self.ui.pushButton_remove_duplicate
        self.pb_close = self.ui.pushButton_close

        self.li_nr_dup.setReadOnly(True)

        # signals
        self.pb_close.clicked.connect(self.close)
        self.pb_find.clicked.connect(self.find_duplicate)
        self.pb_remove.clicked.connect(self.remove_duplicate)

    def set_raports(self):
        """
        fill combo box: cb_raports
        """
        try:
            session = Session()
            competitiev = session.query(Competitive).all()
        except:
            QMessageBox.critical(self, "Błąd", "Nie można połączyć się z bazą danych")
            return

        self.cb_raports.clear()

        for compet in competitiev:
            self.cb_raports.addItem(compet.name)

        session.close()

    def remove_duplicate(self):
        """
        remove duplicate from list
        """
        data = self.get_data()
        rows = [x[2:32] for x in data]
        session = Session()

        for nr in reversed(range(len(rows))):
            if rows.count(rows[nr]) > 1:
                rows.pop(nr)
                session.query(Data).filter(and_(
                    Data.id == data[nr][0],
                    Data.competitive_id == data[nr][1]
                )).delete()
        session.commit()
        session.close()
        self.li_nr_dup.setText('')
        QMessageBox.information(self,'Duplicaty', 'Spoty zostały usunięte')

    @staticmethod
    def count_duplicate(rows):
        """
        count duplicate
        """
        rows = [x[2:32] for x in rows]
        return abs(len(set(map(tuple, rows))) - len(rows))

    def get_data(self):
        rap_name = self.cb_raports.currentText()
        session = Session()
        compative = session.query(Competitive).filter_by(name=rap_name).first()
        data = session.query(Data).filter_by(competitive_id=compative.id).all()
        headers = Data.__table__.columns.keys()
        # remove id, compatitive_id
        headers = headers[0:32]
        # make list
        final_list = []
        for row in data:
            columns = []
            for key in headers:
                columns.append(row.__dict__[key])
            final_list.append(columns)

        session.close()
        return final_list

    def find_duplicate(self):
        data = self.get_data()
        self.li_nr_dup.setText(str(self.count_duplicate(data)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('fusion')
    w = FindDuplicate()
    w.show()
    sys.exit(app.exec_())

