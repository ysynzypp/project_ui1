from xlrd import open_workbook
import sys
import os
sys.path.append("../")
from Base.BasePath import path

class ExcelReader:
    def __init__(self, excel, sheet=0, title_line=True):

        if os.path.exists(excel):
            self.excel = excel
        else:

            raise FileNotFoundError('文件找不到或文件处于打开状态，请检查文件是否处于打开状态')
        self.sheet = sheet
        self.title_line = title_line
        self._data = list()

    def method(self):
        if not self._data:
            workbook = open_workbook(self.excel)
            if type(self.sheet) not in [int, str]:
                raise Exception('Please pass in <type int> or <type str>, not {0}'.format(type(self.sheet)))
            elif type(self.sheet) == int:
                self.s = workbook.sheet_by_index(self.sheet)
            else:
                self.s = workbook.sheet_by_name(self.sheet)
        return self.s
    @property
    def data(self):
        self.method()
        if self.title_line:
            title = self.s.row_values(0)            # 首行为title
            for col in range(1, self.s.nrows):
                # 依次遍历其余行，与首行组成dict，拼到self._data中
                a = dict(zip(title, self.s.row_values(col)))
                a['行号'] = col
                self._data.append(a)
        else:
            for col in range(0, self.s.nrows):
                # 遍历所有行，拼到self._data中
                self._data.append(self.s.row_values(col))
        return self._data




if __name__ == "__main__":
    from pprint import pprint
    a = ExcelReader(path.Case).data
    pprint(a)
    print(
        path.Case
    )


