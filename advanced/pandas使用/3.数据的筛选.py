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
2.1 筛选出获得金牌的数据
"""
gold = oo[oo.Medal=="Gold"]
# print(gold)

"""
2.2 筛选出女子 获得金牌的数据
"""
gold_female = oo[(oo.Medal=="Gold")&(oo.Gender=="Women")] # 且
# gold_female = oo[(oo.Medal=="Gold")|(oo.Gender=="Women")] # 或
# print(gold_female.head(20))

# 如果需要排序
gold_female.sort_values(by="Athlete")
gold_female.sort_values(by=["Athlete","Event"])
# print(gold_female.head(20))



"""
3. 字符串筛选
"""

con = oo.Athlete.str.contains("Florence") # Boolean
# print(con)
# print(oo[con])