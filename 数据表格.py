import pandas as pd

pd.set_option("display.width", 1000)
import os

# =============数据导入-授信清单&被执行记录=============
# pth1="C:\\python\\x变量中诚信数据处理"
# pth2="C:\\python\\x变量中诚信数据处理\\中诚信（327）-12.25"
#
#
# cust_all=pd.read_excel(pth1+'\\Cust_all_CR_SB12.27.xlsx')
# enforced=pd.read_excel(pth2+'\\被执行.xlsx')
#
#
# # 授信清单&被执行记录关联
# enforced_all=pd.merge(cust_all,enforced,on='id',how='left')
# enforced_all.to_excel("过程表1.xlsx")

# # 转日期类型
# enforced_all['SubmitTime']=pd.to_datetime(enforced_all['SubmitTime'])
# enforced_all['regdateclean']=pd.to_datetime(enforced_all['regdateclean'])
# # 筛选审批日期>=立案时间的记录
# enforced_all2 = enforced_all[enforced_all['SubmitTime'] >= enforced_all['regdateclean']]
# print(enforced_all2)


cust = pd.read_excel('Cust_all_CR_SB12.27.xlsx')
enforced = pd.read_excel('被执行.xlsx')

# 转化为统一日期格式
cust['SubmitTime'] = pd.to_datetime(cust['SubmitTime'], format="%Y-%m-%d", errors='coerce').dt.date
enforced['regdateclean'] = pd.to_datetime(enforced['regdateclean'], format="%Y-%m-%d", errors='coerce').dt.date

# for i in cust['SubmitTime'].head(5):
#     print(i, type(i))
#
# print('-' * 100)
#
# for i in enforced['regdateclean'].head(5):
#     print(i, type(i))

enforced_all = pd.merge(cust, enforced, on='id', how='left')
enforced_all2 = enforced_all[enforced_all['SubmitTime'] >= enforced_all['regdateclean']]
enforced_all2.to_excel("临时表4.xlsx")
