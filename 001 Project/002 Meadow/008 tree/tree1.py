import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt

app = QApplication(sys.argv)
window = QWidget()
layout = QVBoxLayout(window)

tw = QTreeWidget()
tw.setHeaderLabels(['Name', 'Cost ($)'])
tw.setAlternatingRowColors(True)
cg = QTreeWidgetItem(tw, ['carrtos', '0.99'])
cg.setCheckState(0, Qt.CheckState.Checked)
c1 = QTreeWidgetItem(cg, ['carrt', '0.33'])
c1.setCheckState(0, Qt.CheckState.Unchecked)
h = QTreeWidgetItem(['ham', '50.13'])
h.setDisabled(True)
tw.addTopLevelItem(h) # dobra funkcja dodaje nowy gałąź powyżej drugiej

bt = QPushButton("Press me")

def get_selected():
    """
    Jak otrzyma zaznaczony pozycje
    :return:
    """
    getSelected = tw.selectedItems()
    if getSelected:
        baseNode = getSelected[0]
        getChildNode = baseNode.text(0)
        print(getChildNode)

bt.clicked.connect(get_selected)


layout.addWidget(tw)
layout.addWidget(bt)
window.show()

# root = tw.invisibleRootItem()
# # child_count = root.childCount()
# # for i in range(child_count):
# #     item = root.child(i)
# #     print(item.text(0))

"""
tak przechodzi przez wszystkie zaznaczone
"""
iterator = QTreeWidgetItemIterator(tw)
while iterator.value():
    item = iterator.value()
    print(item.checkState(0))
    print(item.text(0))
    iterator += 1

sys.exit(app.exec_())