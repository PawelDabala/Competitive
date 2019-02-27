import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt
from uifilters import Ui_Dialog


class TestUI(QDialog):
    def __init__(self):
        super(TestUI, self).__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        #self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    w = TestUI()
    w.show()
    sys.exit(app.exec_())
