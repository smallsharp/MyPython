# coding=utf-8
import pandas as pd
import sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 设置控制台显示宽度
pd.set_option("display.width", 1000)

""" 读取csv文件 """
oo = pd.read_csv("olympics.csv", skiprows=4)

"""
1.设置索引 set_index() 
"""

ath = oo.set_index("Athlete")  # 将运动员姓名作为索引
# print(ath.head())

"""
2.按照索引排序 inplace 是否修改原数据 ascending 是否升序
"""
ath.sort_index(inplace=True, ascending=True)  # 按照字符顺序升序
print(ath.head())

"""
3.根据默认索引，筛选一行或多行数据 loc iloc
"""
line1 = oo.loc[1]  # 选取一行数据
# line1 = oo.loc[[1, 3, 4]]  # 选取多行数据
line1 = oo.loc[1:4]  # 选取多行数据
# line1 = oo[oo.Athlete=="MALOKINIS, Ioannis"] # 根据具体内容，筛选数据
print(line1)

# line2 = oo.iloc[[1, 3, 4]]
line2 = oo.iloc[1:4]
print(line2)

"""
4.根据自定义索引，筛选数据 loc
"""

# print(ath.head())
# s = ath.loc["AABYE, Edgar"]
s = ath.loc[["AABYE, Edgar", "AALTONEN, Arvo Ossian"]]
# s = ath.iloc[["AABYE, Edgar", "AALTONEN, Arvo Ossian"]] # iloc不能这么用
# print(s)


"""
总结： iloc 和 loc 的区别
iloc[1:4] 前包 后不包
loc[1:4] 前包 后包

iloc["自定义索引"] 不可用
loc["自定义索引"] 可用
"""