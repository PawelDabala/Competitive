import sys
from PySide2.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication, QLabel, QLineEdit, QFrame, QDialog


class basicWindow(QDialog):
    def __init__(self):
        super().__init__()

        grid_laout = QGridLayout()

        self.setLayout(grid_laout)

        label = QLabel("Wybierz Plik")
        grid_laout.addWidget(label, 0,0, 1,3)

        label = QLabel('Raport techage')
        grid_laout.addWidget(label,1,0)


        le = QLineEdit()
        #le.setMaximumWidth(200)
        grid_laout.addWidget(le,1,1,1,5)

        pb = QPushButton("Dodaj")
        grid_laout.addWidget(pb,1,6)





        # button = QPushButton('4, 7')
        # grid_laout.addWidget(button, 1,0, -1, 1)

        # for x in range(1,3):
        #     for y in range(1,3):
        #         button = QPushButton(str(str(3*x+y)))
        #         grid_laout.addWidget(button, x, y)

        self.setWindowTitle("Dodaj Pliki")
        self.setGeometry(200,200,400,200)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    windowExample = basicWindow()
    windowExample.show()
    sys.exit(app.exec_())