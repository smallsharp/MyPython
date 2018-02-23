str = "abbr=CN&clientType=android&pageNo=1&pageSize=20&udid=&build=310&imagePixels=1080&imagePHeight=1920&clientVersion=3.1.1&dBrand=OPPO&dModel=OPPO%20R9m&osVersion=2"


l1 = str.split("&")
l2 = []
for l in l1:
    l2.append(l.replace("=",":"))


print(l1)
print(l2)

