import sys
import ntpath
from PySide2.QtWidgets import (
    QApplication,
    QDialog,
    QFileDialog
    )
from uifilechose import Ui_Dialog

class FileChoser(QDialog):
    def __init__(self, parent=None):
        super(FileChoser, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

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
        self.pbaddall.clicked.connect(self.add)

        self.paths = {
                      0: "",
                      1: "",
                      2: "",
                    }

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

    def add(self):
        print(self.paths[0])
        print(self.paths[1])

    def add_new_competitive(self):
        print("add new competitive")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('fusion')
    window = FileChoser()
    window.show()
    sys.exit(app.exec_())






