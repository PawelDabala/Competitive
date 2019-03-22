

class FilterRows:

    """
    class filter sending rows and return only rows matched to the pattern
    """

    def __init__(self, org_list, *args):
        self.org_list = org_list
        self.lineedits = args
        self.returnlist = []


    def works_rows(self):
        """
        :return: return list with matching rows
        """
        for row in self.org_list:
            if self.check_rows(row):
                self.returnlist.append(row)

        return self.returnlist

    def check_rows(self, row):
        """
        check all rows is matching to pattern
        :param row:
        :return:
        """
        nr_cell = 0
        for nr, cell in enumerate(row):
            if self.check_cell(nr, cell):
                nr_cell += 1

        if nr_cell == len(self.lineedits):
            return True
        else:
            return False


    def check_cell(self,nr, cell):
        """
        check the invidual cell matching to pattern
        :param nr:
        :param cell:
        :return:
        """
        if len(self.lineedits[nr]) == 0:
            return True

        if self.lineedits[nr].lower() in cell.lower():
            return True
        else:
            return False
