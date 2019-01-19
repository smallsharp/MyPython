# coding=utf-8

import pandas as pd  # 引入pandas

"""
1.读取csv文件
"""
oo = pd.read_csv("olympics.csv", skiprows=4)  # 略过前4行
# print(pd.__version__) # 0.20.3
# print(pd.show_versions()) # 依赖的库 也会打印出来


"""
2.DataFrames
"""
type(oo)  # <class 'pandas.core.frame.DataFrame'>

"""
2.1 选取其中的某几列数据
多列时，数据类型为：<class 'pandas.core.frame.DataFrame'>
只一列，数据类型为：<class 'pandas.core.series.Series'>
"""
n1 = oo[["City", "Sport", "Event"]]  # <class 'pandas.core.frame.DataFrame'>
n2 = oo["City"]  # <class 'pandas.core.series.Series'>
print(type(n1), type(n2))

# print(n1.tail())
# print(n2.tail())


"""
3.Series
每一列都是Series，每一行也都是Series，类似数组序列
 - 3.1 获取其中一列数据,两种方式
如：oo.City 或 oo["City"]
"""
# print(oo.City)
# print(oo["City"])
type(oo.City)  # <class 'pandas.core.series.Series'>

"""
 - 3.2 获取其中一行数据，如：row = oo.iloc[2] 获取索引为2的一行数据
"""
row = oo.iloc[2]  # 获取其中一行数据,索引为列名称，值为行内容
"""
City                                Athens
Edition                               1896
Sport                             Aquatics
Discipline                        Swimming
Athlete                  DRIVAS, Dimitrios
NOC                                    GRE
Gender                                 Men
Event           100m freestyle for sailors
Event_gender                             M
Medal                               Bronze
Name: 2, dtype: object"""

type(row)  # <class 'pandas.core.series.Series'>

"""
4. 显示文件内容，使用head(),tail()
两个方法适用于 DataFrame 和 Series
"""
# print(oo.head())  # 默认前5行
# print(oo.tail())  # 默认后五行

"""
5. info() 获取数据的类型，entries,columns
"""
oo.info()

"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 29216 entries, 0 to 29215
Data columns (total 10 columns):
City            29216 non-null object
Edition         29216 non-null int64
Sport           29216 non-null object
Discipline      29216 non-null object
Athlete         29216 non-null object
NOC             29216 non-null object
Gender          29216 non-null object
Event           29216 non-null object
Event_gender    29216 non-null object
Medal           29216 non-null object
dtypes: int64(1), object(9)
memory usage: 2.2+ MB
None"""

"""
6.Shape
"""
print(oo.shape)  # (29216, 10) 行,列
oo.shape[0]
oo.shape[1]
