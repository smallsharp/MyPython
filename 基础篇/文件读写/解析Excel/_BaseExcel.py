# -*- coding: utf-8 -*-
import datetime
import xlrd
import xlwt
from xlsxwriter import workbook


class BaseExcel:

    def __init__(self, path, sheetName=None):
        self.path = path
        self.workbook = xlrd.open_workbook(self.path)
        if not sheetName:
            self.sheet = self.workbook.sheet_by_index(0)
        else:
            self.sheet = self.workbook.sheet_by_name(sheetName)

    # 获取excel中所有sheet名称
    def getSheetNames(self):
        return self.workbook.sheet_names()

    def getValueByRow(self, row):
        return self.sheet.row_values(row)

    """
        用途：通过行列获取单元格，主要用于判断单元格的内容类型
        类型：ctype : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error 
    """

    def getCell(self, row, col):
        return self.sheet.cell(row, col)

    # 获取所有用例信息，每一行为一个用例
    def getAllCases(self):
        rows = self.sheet.nrows  # 获取sheet的行数
        cases = []
        for r in range(rows):
            # if r == 0: continue  # 去掉第一行标题
            case = self.sheet.row_values(r)  # 获取该行的内容[]
            cases.append(case)
        return cases

    # 获取所有用例信息，每一行为一个用例
    def get_all_rows(self):
        # 所有行数
        rows = self.sheet.nrows
        cases = []
        for r in range(rows):
            # 单行的内容
            case = self.sheet.row_values(r)
            cases.append(case)
        import json
        print(len(cases))  # 列表长度
        return json.dumps(cases, ensure_ascii=False)


def main():
    excel = BaseExcel("./申请单商品.xlsx", 0)
    rows = excel.get_all_rows()
    print(rows)


def main2():
    # excel = BaseExcel("./申请单商品.xlsx", "sheet_one")
    # cases = excel.getAllCases()
    # print(cases)
    # valueList = excel.getValueByRow(3)
    # value = valueList[10]
    # print("type:", type(value), "value:", value)
    # print(value == "")
    # value = {"result": False}
    # if value.get("result"):
    #     print("ok")
    # # 判断值的类型，int自动转为float
    # if type(value) == float:
    #     value = int(value)
    # print(value)
    #
    # """ctype : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error  """
    # cell = excel.getCell(3, 9)
    # print(cell.ctype)
    pass


if __name__ == '__main__':
    main()
