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

    @staticmethod
    def remove_none_row(columns):

        for row_nr in reversed(range(len(columns[0]))):
            if columns[0][row_nr] is None:
                for col in columns:
                    col.pop(row_nr)

        return columns


    @classmethod
    def get_data(cls, path, tech=True):
        # try:
        #     myfile = open(path, "r+")
        # except IOError:
        #     print("Could not open file! Please close Excel!")

        wb = load_workbook(path)
        ws = wb.worksheets[0]

        col = (list(ws.columns))

        colout = cls.remove_header(col)
        colout = cls.get_value(colout)
        colout = cls.remove_none_row(colout)

        if tech:
            print("rozmiesc kolumny w kolejnosci techenge")
            colout = cls.chenge_poz(colout,
                                    [0, 1, 2, 3, 4, 5, 6, 7, 8, 12, 13, 9, 14, 11, 18, 17, 10, 15, 16],
                                    [6, 7, 8, 9, 15, 16, 18, 19, 22, 23, 25]
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

        temp_list.pop(15)
        temp_list.insert(15, len(lis[0])*["TV"])
        return temp_list








