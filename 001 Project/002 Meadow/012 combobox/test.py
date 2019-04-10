import array
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class CheckBoxDelegate(QItemDelegate):
    def __init__(self, parent=None):
        super(CheckBoxDelegate, self).__init__(parent)

    def createEditor(parent, op, idx):
        self.editor = QCheckBox(parent)
        a


udims = ['1001', '1002', '1003', '1004']
cmb = QComboBox()
delegate = CheckBoxDelegate()
cmb.setItemDelegate(delegate)
model = QStandardItemModel(len(udims), 1)
for i, udim in enumerate(udims):
    item = QStandardItem(udim)
    item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
    item.setData(Qt.Checked | Qt.CheckStateRole)
    model.setItem(i, 0, item)

cmb.setModel(model)