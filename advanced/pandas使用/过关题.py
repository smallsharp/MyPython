#coding=utf-8
import pandas as pd
import sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 设置控制台显示宽度
pd.set_option("display.width", 1000)

oo = pd.read_csv("olympics.csv",skiprows=4)
# print(oo.head())

"""
1.In which events did Jesse Owens win a medal?，show events he take part in.
"""
# owens = oo[oo.Athlete.str.contains("OWENS, Jesse")]
owens = oo[oo.Athlete=="OWENS, Jesse"]
# print(owens)

# print(owens.Event.value_counts()) # 统计出Owens 参与的项目


"""
2.Which country has won men's gold medals in singles badminton over the years? Sort the results alphabetically by the player's  names.
"""

mbs = oo[(oo.Gender=="Men")&(oo.Sport=="Badminton")&(oo.Event=="singles")&(oo.Medal=="Gold")]

mbs1 = mbs.sort_values(by="Athlete")
# print(mbs1)


"""
3.Which three countries have won the most medals in recent years (from 1984 to 2008)?
"""
noc = oo[(oo.Edition>=1984)&(oo.Edition<=2008)]
most3 = noc.NOC.value_counts().head(3)
print(most3)


"""
4.Display the male gold medal winners for the 100m sprint event over the years. 
List the results starting with the most recent. 
Show the Olympic City, Edition, Athlete and the country they represent.
"""

mgm = oo[(oo.Medal=="Gold")&(oo.Gender=="Men")&(oo.Event=="100m")]
new = mgm.sort_values("Edition",ascending=False)[["City","Edition","Athlete","NOC"]]
print(new)
# print(mgm1)



