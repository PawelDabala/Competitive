import sys
import ntpath
from PySide2.QtWidgets import (
    QApplication,
    QDialog,
    QFileDialog,
    QMessageBox
    )
from uifilechose import Ui_Dialog

from sql.base import Session
from sql.competitive import Competitive
from sql.data import Data
from sql.filterf import FilterF
from sql.compatitive_filter import CompativeFilterf
from sql.category import Category

from sqlalchemy import exc


class FileChoser(QDialog):
    def __init__(self, parent=None):
        super(FileChoser, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.main = parent

        #buttons
        self.pbtechedge = self.ui.pushButton_techedge
        self.pbadexpert = self.ui.pushButton_adexpert
        self.pbaddall = self.ui.pushButton_addall
        self.pbaddrapo = self.ui.pushButton_addraports

        #lineedit
        self.letechedge = self.ui.lineEdit_techedge
        self.leadexpert = self.ui.lineEdit_adexpert
        self.leaddraport = self.ui.lineEdit_addraport

        #combobox
        self.cbraports = self.ui.comboBox_raports

        #connects
        self.pbtechedge.clicked.connect(lambda: self.pic_file(self.letechedge, 0))
        self.pbadexpert.clicked.connect(lambda: self.pic_file(self.leadexpert, 1))
        self.pbaddrapo.clicked.connect(self.add_new_competitive)
        self.pbaddall.clicked.connect(self.send_values)

        self.paths = {
                      0: "",
                      1: "",
                      2: "",
                    }

        """
        read records from database
        """
        self.populate_row_competitive()

    def clead_data(self):
        """
        clean data in form
        :return:
        """
        self.paths = {
            0: "",
            1: "",
            2: "",
        }

        self.letechedge.setText("")
        self.leadexpert.setText("")


    def pic_file(self, lename, nr):
        """
        open file dialog to open file
        :param lename: lineedit where will show picked file
        :return: path to file
        """
        fpath = QFileDialog.getOpenFileName(self, 'Otwórz plik',
                                            'c:\\', "Pliki Excel (*.xlsx *.xlsm)")
        lename.setText(ntpath.basename(fpath[0]))
        self.paths[nr] = fpath[0]

    def send_values(self):
        self.close()
        self.main.get_data(self.paths, str(self.cbraports.currentText()))



    def add_new_competitive(self):
        """
        add new competitive name to data base
        :return:
        """

        new_name = self.leaddraport.text()
        if self.check_is_not_empty(new_name):
            """
            add new name to data base
            """
            try:
                session = Session()
                name = Competitive(new_name)
                session.add(name)
                session.commit()
                session.close()

            except exc.IntegrityError:
                QMessageBox.critical(self, "Bład", "Błąd zapisu danych do bazy.\n Podana nazwa już istnieje")
                return

            """
            add value to combo box and clear line edit
            """
            self.leaddraport.setText('')
            self.cbraports.addItem(new_name)
            self.cbraports.setCurrentText(new_name)

    def populate_row_competitive(self):
        """
        read rows from database with competitive name
        :return:
        """
        try:
            session = Session()
            competits = session.query(Competitive).all()

        except:
            QMessageBox.critical(self, "Błąd", "Nie można połączyć się z bazą danych")
            return

        for compet in competits:
            self.cbraports.addItem(compet.name)

    @staticmethod
    def check_is_not_empty(text):
        """
        check the line edit with new client is not empty
        """
        if len(text) == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Wartość w polu nie może być pusta")
            msg.setWindowTitle("Błąd")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return False
        return True



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('fusion')
    window = FileChoser()
    window.show()
    sys.exit(app.exec_())






