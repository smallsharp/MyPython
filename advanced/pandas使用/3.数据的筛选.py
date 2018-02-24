# coding=utf-8
import pandas as pd
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# 设置控制台显示宽度
pd.set_option("display.width", 1000)

"""
1.读取csv文件
"""
oo = pd.read_csv("olympics.csv", skiprows=4)


"""
2.1 根据文本内容筛选-单个条件
"""
gold = oo[oo.Medal=="Gold"]
# print(gold)

"""
2.2 根据文本内容筛选-多个条件
"""
gold_female = oo[(oo.Medal=="Gold")&(oo.Gender=="Women")] # 且
# gold_female = oo[(oo.Medal=="Gold")|(oo.Gender=="Women")] # 或
# print(gold_female.head(20))

# 如果需要排序
gold_female.sort_values(by="Athlete")
gold_female.sort_values(by=["Athlete","Event"])
# print(gold_female.head(20))

"""
2.3 根据默认索引筛选[0,1,2,…]:iloc
"""
line2 = gold_female.iloc[1]
lines1 = gold_female.iloc[1,3,4,6]
lines2 = gold_female.iloc[5:10]


"""
2.4 包含字符串筛选
"""

con = oo.Athlete.str.contains("Florence") # Boolean
# print(con)
# print(oo[con])