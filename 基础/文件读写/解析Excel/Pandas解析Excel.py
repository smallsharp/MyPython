import pandas as pd


df  = pd.read_excel(io="2018_02_03.xlsx",sheetname=0, encoding = "gb18030")

# print(df.head(20))
# print(df.columns)
# print(df.head())

df.fillna(value="Kong")
