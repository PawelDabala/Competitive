from openpyxl import  load_workbook
from pathlib import Path


def remove_header(lis):
    """
    remove first element from all columns
    :param lis:
    :return:
    """
    temp_lis = []
    for ele in lis:
        ele = list(ele)
        ele.pop(0)
        temp_lis.append(ele)

    return temp_lis


def get_value(cols):
    """
    get value from worksheets cell
    :return:
    """
    temp_list = []
    for col in cols:
        values = []
        for cell in col:
            values.append(cell.value)
        temp_list.append(values)

    return temp_list

def get_data(path, workshet_name):
    # path = path.replace('/', r"'\'")
    wb = load_workbook(path)
    ws = wb[workshet_name]

    col = (list(ws.columns))

    colout = remove_header(col)
    colout = get_value(colout)

    print(colout)
    return colout


def make_dictionary(colout):
    fil_dic = {}
    for nr, value in enumerate(colout[1]):
        if value in fil_dic:
            fil_dic[value].append(colout[0][nr])
        else:
            fil_dic[value] = [colout[0][nr]]

    return fil_dic


# path = Path(r"C:\001_programy\005_competitive\001 Project\001 Application\sql\slowniki.xlsx")
colout = get_data("slowniki.xlsx", 'Sub Category uspojnienie')
print(make_dictionary(colout))





