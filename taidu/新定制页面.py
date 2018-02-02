'''
Created on 2017年11月2日
@author: cm
'''
import urllib.request
import json

def categoryProductList():
    url = "https://m.taidu.com/goodsSite/home/categoryProductList?abbr=CN"    
    codeDict = {}
    try:
        res = urllib.request.urlopen(url)
        resJson = json.loads(res.read())
        if resJson is not None:
            result = resJson['result']
            if result is not None:
                for r in result:
                    codeDict[r['categroyCode']] = r['categoryName']
            else:
                print('categoryProductList result is null')
    except Exception as e:
        print(e)        
    return codeDict

def getCategoryInfo(categoryId):
    url = "https://m.taidu.com/goodsSite/home/categoryProductInfo?abbr=CN&categoryId=%s"%categoryId;
    cateDict = {}
    try:
        res = urllib.request.urlopen(url)
        resJson = json.loads(res.read())
        if resJson is not None:
            result = resJson['result']
            if result is not None:
                for r in result:
                    cateDict[r['productCode']] = r['productName']
    except Exception as e:
        print(e)
    return cateDict


## productId对应多个商品
def goodsList(productId):
    url = "https://m.taidu.com/goodsSite/home/productGoodsList?abbr=CN&productId=%s"%productId
    itemDictList = []
    try:
        res = urllib.request.urlopen(url)
        resJson = json.loads(res.read())
        if resJson is not None:
            result  = resJson['result']
            if result is not None:
                pageItems = result['pageItems']
                if pageItems is not None:
                    for item in pageItems:
                        itemDict = {}
                        itemDict['productId'] = item['productId']
                        itemDict['goodsId'] = item['goodsId']
                        itemDict['goodsName'] = item['goodsName']
                        itemDict['goodsImagePath'] = item['goodsImagePath']
                        itemDict['salePrice'] = item['salePrice']
                        itemDict['currencySymbol'] = item['currencySymbol']
                        itemDictList.append(itemDict)
                else:
                    return
            else:
                print("goodsList result is None")
                return
    except Exception as e:
        print("goodsList:",e) 
#     print(itemDictList) 
    return itemDictList
    
                

if __name__ == '__main__':
    cateDict = categoryProductList()
    if cateDict is not None:
        for code,codename in cateDict.items():
            print("====>一级分类code:",code,", codeName:",codename)
            cateDictInfo = getCategoryInfo(code)
            if cateDictInfo is not None:
                for productCode,productName in cateDictInfo.items():
                    print("==>二级分类productCode:",productCode,", productName:",productName)
                    goods = goodsList(productCode)
                    if goods is not None:
                        for good in goods:
                            print("goodsId:%s, goodsName:%s, salePrice:%s"%(good['goodsId'],good['goodsName'],good['salePrice']))
                    else:
                        print("goodsList:",goods)
            else:
                print("cateDictInfo:",cateDictInfo)
            print("-"*50)

    else:
        print("cateDict:",cateDict)
        
        
        
        
        
        
    