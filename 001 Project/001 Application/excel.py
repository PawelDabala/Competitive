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
            colout = cls.chenge_poz(colout,
                                    [0, 1, 2, 3, 4, 5, 6, 7, 8, 12, 13, 9, 14, 11, 17, 10, 15, 16, 18],
                                    [6, 7, 8, 9, 15, 16, 18, 19, 22, 23, 24, 25]
                                    )
        else:
            for i in range(4):
                colout.append([None]*len(colout[0]))

        return colout

    @classmethod
    def chenge_poz(cls, lis, poz, emptys=[]):
        """
        chenge pozytion lists in list end insert empty list
        :param lis: - list of data
        :param poz: - pozition where columns shoud past
        :param emptys: - pozition where empty clumns shoud insert
        :return:
        """
        temp_list = []
        for nr in poz:
            temp_list.append(lis[nr])

        #insert empty list
        for nr in emptys:
            temp_list.insert(nr, [])

        return temp_list








