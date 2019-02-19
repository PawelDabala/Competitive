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

    def get_data_from_techedge(self, path):
        wb = load_workbook(path)
        ws = wb.worksheets[0]

        col = (list(ws.columns))
        col = self.remove_header(col)

        #ADD!!! ustawianie column w odpowiedniej kolejnosci

        return  col




