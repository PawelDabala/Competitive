import sys
import ntpath
from PySide2.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog
from PySide2.QtCore import QFile
from open import Ui_Dialog




class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.bt = self.ui.pushButton
        self.bt.clicked.connect(self.getfile)

    def getfile(self):
        fpath = QFileDialog.getOpenFileName(self, 'Otwórz plik',
         'c:\\',"Pliki Excel (*.xlsx *.xlsm)")
        print(fpath[0])
        print(ntpath.basename(fpath[0]))





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())