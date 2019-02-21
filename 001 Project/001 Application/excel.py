from openpyxl import load_workbook


class Excel:

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

    @classmethod
    def get_data(cls, path, tech=True):
        wb = load_workbook(path)
        ws = wb.worksheets[0]

        col = (list(ws.columns))

        colout = cls.remove_header(col)
        colout = cls.get_value(colout)

        if tech:
            print("rozmiesc kolumny w kolejnosci techenge")
            """
                   #ADD!!! ustawianie column w odpowiedniej kolejnosci
            """
        else:
            print("rozmiesc kolumn w kolejnosci adexpert")

        return colout









