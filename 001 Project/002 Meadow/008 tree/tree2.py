import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt

app = QApplication(sys.argv)
window = QWidget()
layout = QVBoxLayout(window)

tw = QTreeWidget()
tw.setHeaderLabels(['Name', 'Cost ($)', 'Col3'])
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
btremove = QPushButton('Remove')
btgoall = QPushButton('Goforall')
checkcontrol = QCheckBox("check me")
gotrouchall = QPushButton('GoTrouhAll')
getallchildren = QPushButton('GetAllChildren')
removeexistchildren = QPushButton('RemoveExistChildren')


def test(item, column):
    tw.blockSignals(True)
    root = tw.invisibleRootItem()
    child_count = root.childCount()
    for i in range(child_count):
        item2 = root.child(i)
        if item.text(column) != item2.text(0):
            #print(item2.text(0))
            item2.setCheckState(0, Qt.CheckState.Unchecked)
        else:

            item.setCheckState(0, Qt.CheckState.Checked)

    tw.blockSignals(False)
    #print('########')


tw.itemChanged.connect(test)


"""
adding multi chldren
"""
childlist = [['','chil 1', 'Nany'], ['','chil 2', 'Hary'],['','chil 3', 'Jonn']]
childlist2 = ['chil 1', 'chil 2','chil 3']
#to działa
for ch in childlist:
    newch = QTreeWidgetItem(cf, ch)
    newch.setCheckState(1, Qt.CheckState.Unchecked)

print(tw.columnCount())


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


# def deleteItem():
#     print('delteItem2')
#     root = tw.invisibleRootItem()
#     for item in tw.selectedItems():
#         (item.parent() or root).removeChild(item)

def deleteItem():

    root = tw.invisibleRootItem()
    child_count = root.childCount()
    for i in range(child_count):
        item = root.child(i)
        if item.parent() is None:
            # child_count2 = item.childCount()
            # for j in range(child_count2):
            #     item2 = item.child(j)
            #     # print(item2.text(0))
            #     # print(item2.text(1))
            #     item.removeChild(item2)
            # to dziła bardzo dobrze
            chlist = item.takeChildren()
            for ch in chlist:
                if ch.checkState(1) == Qt.CheckState.Checked:
                    item.removeChild(ch)
                    print(ch.text(1))

        #item.text()
        # if (item.checkState(0) or item.checkState(1)) == Qt.CheckState.Checked:
        #     print(item.text(0))
        #     print(item.text(1))
            #(item.parent() or root).removeChild(item)
    #root1 = tw.takeTopLevelItem(0)

def delteItem2():
    root = tw.invisibleRootItem()
    rootch = root.takeChildren()

    for rch in rootch:
        chili = rch.takeChildren()
        for ch in chili:
            print(ch.text(1))

"""
remove all checked items
"""
def deleteItem3():
    root = tw.invisibleRootItem()
    child_count = root.childCount()
    root.co
    transfer = []
    for i in reversed(range(child_count)):
        item = root.child(i)
        print(item.text(0))
        if item.checkState(0) == Qt.CheckState.Checked:
            temli = item.takeChildren()
            transfer += [i.text(1) for i in temli]
            # transfer += temli
            root.removeChild(item)

        if item is not None:
            child_countch = item.childCount()
            for j in reversed(range(child_countch)):
                print(j)
                itemch = item.child(j)
                print(itemch.text(1))
                if itemch.checkState(1) == Qt.CheckState.Checked:
                    print(f'remove {itemch.text(1)}')
                    transfer.append(itemch.text(1))
                    item.removeChild(itemch)

    print(transfer)


def goforall():
    iterator = QTreeWidgetItemIterator(tw)
    while iterator.value():
        item = iterator.value()
        # print(item.checkState(0))
        if item.parent() is not None:
            print('has parent')
            print(item.text(1))
            tw.removeItemWidget(item, 1)
        print(item.text(0))
        tw.removeItemWidget(item, 0)
        iterator += 1

def go_trouch_all_items():
    iterator = QTreeWidgetItemIterator(tw)
    while iterator.value():
        item = iterator.value()
        parent_name = ''
        old_parent = ''
        all_child = []

        if item.parent() is None:
            #print(f'added new category {item.text(0)}')
            parent_name = item.text(0)
        if item.parent() is not None:
            if item.parent().text(0) == parent_name:
                parentchild = [item.text(i) for i in range(tw.columnCount())[1:]]
                all_child.append(parentchild)


        iterator += 1


def go_trouch_all_items2():
    root = tw.invisibleRootItem()
    child_count = root.childCount()
    parent_name = ''
    all_childs = []

    for i in range(child_count):
        item = root.child(i)
        if item.parent() is None:
            parent_name = item.text(0)

            item_child_count = item.childCount()
            for j in range(item_child_count):
                childs = (item.child(j).text(1), item.child(j).text(2))
                print(type(childs))
                all_childs.append(childs)
                print(type(all_childs))

            print(parent_name)
            print(all_childs)

def check_stauts(chcon):

    if chcon.isChecked():
        print("is check")
    else:
        print("is not check")


def get_all_children():
    iterator = QTreeWidgetItemIterator(tw)
    all_child = []
    while iterator.value():
        item = iterator.value()
        if item.parent() is not None:
                parentchild = [item.text(i) for i in range(tw.columnCount())[1:]]
                all_child.append(parentchild)

        iterator += 1
    print(all_child)
# FIXME: Once file is out of scope
def remove_child_if_exist():
    exists_childs = [[' chil 3 ', 'Jonn']]
    exists_childs = list(list(b.strip().lower() for b in a) for a in exists_childs)
    #exists_childs = list(list(b.lower() for b in a) for a in exists_childs)
    iterator = QTreeWidgetItemIterator(tw)

    while iterator.value():
        item = iterator.value()
        if item.parent() is not None:
            parentchild = [item.text(i) for i in range(tw.columnCount())[1:]]
            parentchild = list(a.strip().lower() for a in parentchild)
            if parentchild in exists_childs:
                item.parent().removeChild(item)

        iterator += 1




bt.clicked.connect(get_selected)
bt2.clicked.connect(show_checked)
btremove.clicked.connect(deleteItem3)
btgoall.clicked.connect(goforall)
checkcontrol.stateChanged.connect(lambda: check_stauts(checkcontrol))
gotrouchall.clicked.connect(go_trouch_all_items2)
getallchildren.clicked.connect(get_all_children)
removeexistchildren.clicked.connect(remove_child_if_exist)

layout.addWidget(tw)
layout.addWidget(bt)
layout.addWidget(bt2)
layout.addWidget(btremove)
layout.addWidget(btgoall)
layout.addWidget(checkcontrol)
layout.addWidget(gotrouchall)
layout.addWidget(getallchildren)
layout.addWidget(removeexistchildren)

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


sys.exit(app.exec_())