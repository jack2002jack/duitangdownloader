import xlrd
xl = xlrd.open_workbook("test1.xls")
table = xl.sheet_by_index(0)
print(table.cell_value(0,0))