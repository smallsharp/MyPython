#coding=utf-8

import datetime
import xlrd
import xlwt
from xlsxwriter import workbook

class BaseExcel:

    # 两个参数必传
    def __init__(self, path, sheetName):
        self.path = path
        self.sheetName = sheetName
        try:
            self.workbook = xlrd.open_workbook(self.path)
            self.sheet = self.getSheetByName(self.sheetName)
        except Exception as e:
            print("请检查Excel文件是否存在，文件格式是否正确,提供的路径：",self.path)

    # 获取excel中所有sheet名称
    def getSheetNames(self):
        return self.workbook.sheet_names()

    # 根据sheet名称获取sheet
    def getSheetByName(self, sheetName):
        sheet = None
        try:
            sheet = self.workbook.sheet_by_name(sheetName)
        except Exception as e:
            print("没有找到sheet：",sheetName)
        return sheet

    def get_rows(self,row):
        return self.sheet.row_values(row)

    """
        用途：通过行列获取单元格，主要用于判断单元格的内容类型
        类型：ctype : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error 
    """
    def getCell(self,row,col):
        return self.sheet.cell(row,col)

    # 获取所有用例信息，每一行为一个用例
    def getAllCases(self):
        rows = self.sheet.nrows # 获取sheet的行数
        cases = []
        for r in range(rows):
            if r == 0: continue #去掉第一行标题
            case = self.sheet.row_values(r) # 获取该行的内容[]
            cases.append(case)
        return cases

if __name__ == '__main__':
    excel = BaseExcel("./2018_02_03.xlsx", "产品")
    # lines = excel.getAllCases()
    print(excel.get_rows(9))