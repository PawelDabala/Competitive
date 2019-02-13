import sys
from PySide2.QtWidgets import QApplication, QDialog, QFileDialog
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

        #lineedit
        self.letechedge = self.ui.lineEdit_techedge
        self.leadexpert = self.ui.lineEdit_adexpert
        self.leaddraport = self.ui.lineEdit_addraport

        #combobox
        self.cbraports = self.ui.comboBox_raports
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('fusion')
    window = FileChoser()
    window.show()
    sys.exit(app.exec_())






