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
cg.setCheckState(0, Qt.CheckState.Unchecked)
cf = QTreeWidgetItem(tw, ['dog'])
cf.setCheckState(0, Qt.CheckState.Unchecked)
ch = QTreeWidgetItem(tw, ['cat'])
ch.setCheckState(0, Qt.CheckState.Unchecked)


c1 = QTreeWidgetItem(cg, ['carrt', '0.33'])
c1.setCheckState(0, Qt.CheckState.Unchecked)
# h = QTreeWidgetItem(['ham', '50.13'])
# h.setDisabled(True)
# tw.addTopLevelItem(h) # dobra funkcja dodaje nowy gałąź powyżej drugiej

bt = QPushButton("Press me")
bt2 = QPushButton("Show checked")


def test(item, column):
    tw.blockSignals(True)
    root = tw.invisibleRootItem()
    child_count = root.childCount()
    for i in range(child_count):
        item2 = root.child(i)
        if item.text(column) != item2.text(0):
            print(item2.text(0))
            item2.setCheckState(0, Qt.CheckState.Unchecked)
        else:

            item.setCheckState(0, Qt.CheckState.Checked)

    tw.blockSignals(False)
    print('########')


tw.itemChanged.connect(test)


"""
adding multi chldren
"""
childlist = [['','chil 1'], ['','chil 2'],['','chil 3']]
childlist2 = ['chil 1', 'chil 2','chil 3']
#to działa
for ch in childlist:
    newch = QTreeWidgetItem(cf, ch)
    newch.setCheckState(1, Qt.CheckState.Unchecked)


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

"""
get checked item
"""
def show_checked():
    root = tw.invisibleRootItem()
    child_count = root.childCount()
    for i in range(child_count):
        item = root.child(i)
        if item.checkState(0) == Qt.CheckState.Checked:
            print(item.text(0))


bt.clicked.connect(get_selected)
bt2.clicked.connect(show_checked)

layout.addWidget(tw)
layout.addWidget(bt)
layout.addWidget(bt2)

window.show()

"""
to działa bardzo dobrze
"""
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
    # print(item.checkState(0))
    # print(item.text(0))
    iterator += 1

sys.exit(app.exec_())