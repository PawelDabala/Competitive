import sys
from PySide2.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication


class basicWindow(QWidget):
    def __init__(self):
        super().__init__()
        grid_laout = QGridLayout()
        self.setLayout(grid_laout)

        for x in range(3):
            for y in range(3):
                button = QPushButton(str(str(3*x+y)))
                grid_laout.addWidget(button, x, y)

        self.setWindowTitle("Basic Grid Layout")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    windowExample = basicWindow()
    windowExample.show()
    sys.exit(app.exec_())