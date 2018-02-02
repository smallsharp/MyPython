import json
import urllib
import certifi
import urllib3
import time
from urllib import request

http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())

prefix_imgex = 'https://imgex.Python.com/imgsrv/'
prefix_image = 'https://image.Python.com/imgsrv/'

# 根据code_list，遍历code对应的数据，key:productId  value:二级目录的图片
def getProductDict(codeList):
    productDict = {}
    for code in codeList:
        url = 'https://m.taidu.com/goodsSite/home/productImageList?abbr=CN&categoryCode=%s'%code
        try:
            response = urllib.request.urlopen(url)
        except Exception:
            print("请求出现异常："+url)
        responseData = response.read().decode('utf-8')
        jsonStr = json.loads(responseData)
        resultList = jsonStr['result']
        if resultList != None:
            for re in resultList:
                productDict[re['productCode']] = prefix_imgex+re['imagePath']
    return productDict
# 根据product_id，取出商品中的图片
def getGoodsDict(productId):
    url = "https://android.Python.com/goodsSite/home/goodsList?clientType=android&productId=%s"%productId
    result_list = getResult(url)
    goodsDict = {}
    if result_list != []:
        pageItemsList = result_list['pageItems']
        for re in pageItemsList:
            goodsDict[re['goodsId']] = prefix_imgex + re['goodsImagePath']
    return goodsDict

def getMaterialDict():
    materialDict = {}
    url = "https://apimerch.Python.com/material/getMaterialCategoryList"
    result = getResult(url)
    if result != None or result != []:
        for re in result:
            materialDict[re['code']] = re['name']
    return materialDict


def getMaterialImg(code:"素材的code",pageSize:"一页显示的条数"):
    materialList = []
    url = "https://apimerch.Python.com/material/materialList?code=%s&pageNo=1&pageSize=%s&parentCode=0"%(code,pageSize)
    result = getResult(url)
    if result != None or result != []:
        pageItems = result['pageItems']
        if pageItems != None or pageItems != []:
            for p in pageItems:
                path = prefix_imgex + p['path']
                materialList.append(path)
    return materialList
    
        
# 根据url链接，返回响应中的result 节点数据
def getResult(url):
    reponse = urllib.request.urlopen(url)
    result = []
    try:
        if reponse.getcode() == 200:
            jsonData = json.loads(reponse.read().decode('utf-8'))  # 解析成json数据
            result = jsonData['result']
        else:
            return None
    except Exception:
        print("请求出现异常",url)
    return result

def startJob():
    
    # 第一步，遍历所有二级目录的图片
    print("开始测试")
    codeList = [101, 100, 113, 103, 104, 102, 114, 115, 112]
    productDict = getProductDict(codeList)
        
    print("开始遍历:所有二级目录的图片")
    for productId,url in productDict.items():
        try:
            urllib.request.urlopen(url)
        except Exception:
            print("[Error]==>productId:%s,url:%s"%(productId,url))
        
    # 第二步，遍历所有商品图片
    print("开始遍历:所有商品预览页面的图片")
    for productId in productDict.keys():
        print("当前正在执行==>productId:%s"%productId)
        goodsDict = getGoodsDict(productId)
        for goodsId,goodsImageUrl in goodsDict.items():
            try:
                urllib.request.urlopen(goodsImageUrl)
            except Exception:
                print("[Error]==>productId:%s,goodsId:%s,url:%s"%(productId,goodsId,goodsImageUrl))
        
    # 第三步，遍历所有在线素材图片
    print("开始遍历:所有在线素材的图片")
    materialDict = getMaterialDict()
    for code,name in materialDict.items():
        imgList = getMaterialImg(code, "10")
        print("当前正在执行==>素材名称:%s,素材code:%s,条数:%s"%(name,code,len(imgList)))
        for img in imgList:
            try:
                urllib.request.urlopen(img)
            except Exception:
                print("[Error]第%d条,%s"%(list.index(img),img))
    print("执行完毕！！！！")
        
if __name__ == '__main__':
    
    ticksBegin = time.time()
    print ("当前时间戳:", ticksBegin)    
    startJob()
    ticksEnd = time.time()
    print ("结束时间戳:", ticksEnd)
    print("总用时：",ticksEnd-ticksBegin)