from openpyxl import  load_workbook
from pathlib import Path


class MakeDictionary:
    def __init__(self, path, worksheet_name):
        self.path = path
        self.worksheet_name = worksheet_name

    @staticmethod
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

    @staticmethod
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

    def get_data(self, path, worksheet_name):
        wb = load_workbook(path)
        ws = wb[worksheet_name]

        col = (list(ws.columns))

        colout = self.remove_header(col)
        colout = self.get_value(colout)

        return colout

    @staticmethod
    def make_dictionary(colout):
        fil_dic = {}
        for nr, value in enumerate(colout[1]):
            if value in fil_dic:
                fil_dic[value].append([colout[0][nr]])
            else:
                fil_dic[value] = [[colout[0][nr]]]

        return fil_dic

    def set_dictionary(self):
        colout = self.get_data(self.path, self.worksheet_name)
        return self.make_dictionary(colout)


# # path = Path(r"C:\001_programy\005_competitive\001 Project\001 Application\sql\slowniki.xlsx")
# colout = get_data("slowniki.xlsx", 'Sub Category uspojnienie')
# print(make_dictionary(colout))





