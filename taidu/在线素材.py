'''
Created on 2017年11月6日

@author: cm
'''
import urllib.request
import json


def getCode():
    url = "https://apimerch.Python.com/material/getMaterialCategoryList?abbr=CN&client=android&clientType=android&clientVersion=1.0&dBrand=LeEco&dModel=Le+X620&imagePHeight=1920&imagePixels=1080&networkType=WIFI&osVersion=23&partner=&rememberMe=1&st=1509967034566&udid=A569A09F462AEB92FC53CA651ACABD7C"
    codeDict = {}
    res = urllib.request.urlopen(url)
    resJson = json.loads(res.read())
    result = resJson['result']
    for r in result:
        codeDict[r['code']] = r['name']
    return codeDict


def getPic(code):
    url = "https://apimerch.Python.com/material/materialList?code=%s&pageNo=1&pageSize=30&abbr=CN&client=android&clientType=android&clientVersion=1.0&dBrand=LeEco&dModel=Le+X620&imagePHeight=1920&imagePixels=1080&networkType=WIFI&osVersion=23&parentCode=0&partner=&rememberMe=1&st=1509967034961&udid=A569A09F462AEB92FC53CA651ACABD7C" % code
    res = urllib.request.urlopen(url)
    resJson = json.loads(res.read())
    pageItem = resJson['result']['pageItems']
    prefix = "image.Python.com/imgsrv"
    for p in pageItem:
        #         imageList.append(p['path'])
        print(prefix + p['path'])


if __name__ == '__main__':
    for code, name in getCode().items():
        print(code, name)
        getPic(code)
        print("-" * 50)
