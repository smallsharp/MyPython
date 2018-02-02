import urllib.request
import json
import  xml.dom.minidom
from builtins import str
from script.MySqlHelper import SqlHelper
# from script.MySqlHelper import SqlHelper

'''
    1.解析getModelShow接口中返回的modelJson，提取关键数据，存放到svglist中
    2.解析tude_goods_merchant_relation表中 svg_content字段，提取关键数据，存放到svglist中
    3.对比两个svglist
'''

def getProductList():
    url = "https://m.taidu.com/goodsSite/home/categoryProductList?abbr=CN"
    try:
        res = urllib.request.urlopen(url)
        resJson = json.loads(res.read())
        result = resJson.get("result")
        product = []
        for r in result:
            categoryCode = r.get('categroyCode')
            categoryName = r.get('categoryName')
            productList = r.get("productList")
            for p in productList:
                productDict = {}
                productDict['categoryCode'] = categoryCode
                productDict['categoryName'] = categoryName
                productDict['productCode'] = p.get("productCode")
                productDict['productName'] = p.get("productName")
                product.append(productDict)
    except Exception as e:
        print("getProductList:",e)
    return  product

# productGoodsList
def productGoodsList(productId):
    url = "https://m.taidu.com/goodsSite/home/productGoodsList?abbr=CN&productId=%s&skuGroup="%productId
    res = urllib.request.urlopen(url)
    resJson = json.loads(res.read())
    result = resJson.get("result")
    pageItems = result.get("pageItems")
    goods = []
    if pageItems is not None:
        for p in pageItems:
            goodsDict = {}
            goodsDict['modelClassId'] = p.get('modelClassId')
            goodsDict['goodsId'] = p.get('goodsId')
            goodsDict['goodsName'] = p.get('goodsName')
            goodsDict['productDesignType'] = p.get('productDesignType')
            goodsDict['goodsImagePath'] = p.get('goodsImagePath')
            goodsDict['salePrice'] = p.get('salePrice')
            goodsDict['skunicode'] = p.get('skunicode')
            goods.append(goodsDict)    
    return goods

# 根据接口返回的modeljson，解析成可以对比的格式，如果是原3d的modelJson则返回空[]
def getModelShow(modelClassId,goodsId,productDesignType):
    url = '''https://apimerch.Python.com/restwsapis/goods/getModelShow?clientId=d83fcd1f-2ad8-41b5-981d-3342548c768e&clientSecret=0927150e-64fd-4191-85c2-b9b5c34d5a17&clientType=ios&goodsId=%s&modelClassId=%s&productDesignType=%s&sign=8277D05C3130FA2E03699B82213A31E7&skuniCode=10041_0_0&source=1'''%(goodsId,modelClassId,productDesignType)
    res = urllib.request.urlopen(url)
    svgList = []
    prefix = 'http://image.Python.com/imgsrv/'
    resJson = json.loads(res.read())
    # 接口返回中出现的code 和 result
    if(resJson.get('code')=="200"):
        result = resJson.get("result")
        modelStr = result['modelJson'] #获取接口中的modelJson数据 需要重新loads
        if modelStr is not None:
            modelJson = json.loads(modelStr)
            if modelJson.get('svgModelImgVo') is not None and modelJson.get('svgImgVo') is not None:
                svgModelImgVo = modelJson['svgModelImgVo']
                svgImgVo = modelJson['svgImgVo']
                for s1 in svgModelImgVo:
                    s1Dict = {}
                    s1Dict['id'] = s1.get('id')
                    s1Dict['width'] = str(s1.get('width'))
                    s1Dict['height'] = str(s1.get('height'))
                    s1Dict['href'] = prefix + s1.get('href')
#                     s1Dict['url'] = s.get('url')
                    svgList.append(s1Dict)
                for s2 in svgImgVo:
                    s2Dict = {}
                    s2Dict['id'] = s2.get('id')
                    s2Dict['width'] = str(s2.get('width'))
                    s2Dict['height'] = str(s2.get('height'))
                    s2Dict['href'] = prefix + s2.get('href')
                    svgList.append(s2Dict)
                # 第三个元素和第四个元素互换位置
                svgList[2],svgList[3] = svgList[3],svgList[2]
                print(url)
            else:
                print('[解析modelJson失败，modelJson格式不符]:',modelJson)
                print('[请求url]:',url)
        else:
            print("Error:",modelStr)
    else:
        print("[接口数据返回异常] ",resJson.get('code'),"result:",resJson.get('result'),'goodsId:',goodsId,'modelClassId:',modelClassId)
        print(url)
    return svgList

def getSvgContentFromDB(db,sql,goodsId):
    sql = "SELECT svg_content FROM tude_goods_merchant_relation where goods_id = %s AND mch_code = '7E454682492A'"
    result = db.runQuery(sql, goodsId)
    svg_content = ''
    for r in result:
        svg_content = r.get('svg_content')
#         print(r.get('svg_content'))
    return svg_content

# 将文本 写入文件后，再次解析文件
def parseXml(string):
    path = "./test.svg"
    file = open(path,'w')
    file.write(string)
    file.close()
    # 解析文件
    dom = xml.dom.minidom.parse('./test.svg') 
    # 得到文档元素对象
    root = dom.documentElement
#     print (root.nodeName)
#     print(root.nodeValue)
#     print(root.nodeType)
#     print(root.ELEMENT_NODE)    
    imagelist = root.getElementsByTagName("image")
    svg = []
    for image in imagelist:
        imageDict = {}
        imageDict['id'] = image.getAttribute("id")
        imageDict['width'] = image.getAttribute("width")
        imageDict['height'] = image.getAttribute("height")
        imageDict['href'] = image.getAttribute("xlink:href")
        svg.append(imageDict)
    return svg
    
if __name__ == '__main__':
    ## 读取goods库tude_goods_merchant_relation表中，svg_content内容
#     db = SqlHelper(host='10.24.192.147', user='artsuser', password='artspassword', database='goods', charset='utf8')
    db = SqlHelper(host='100.114.31.253', user='artsfetch', password='artsfetchpassword', database='goods', charset='utf8')
    db.open()
    productList = getProductList()
    print(productList)
    for p in productList:
        categoryName = p.get('categoryName')
        productId = p.get('productCode')
        productName = p.get('productName')
        print('====','categoryName:',categoryName, 'productId:',productId,'productName:',productName,"====")
        print('*'*80)
        goods = productGoodsList(productId)
        for g in goods:
            goodsId = g.get('goodsId')
            modelClassId = g.get('modelClassId')
            goodsName = g.get('goodsName')
            productDesignType = g.get('productDesignType')
            print('modelClassId:',modelClassId,'goodsId:',goodsId,'goodsName:',goodsName,' productDesignType:',productDesignType)
            #### 第一步：根据getmodelshow接口modelJson，解析成svg list
            svgcontent_model = getModelShow(modelClassId=modelClassId,goodsId=goodsId,productDesignType=productDesignType)
            
            ## 读取goods库tude_goods_merchant_relation表中，svg_content内容
            sql = "SELECT svg_content FROM tude_goods_merchant_relation where goods_id = %s"
             
            #### 二步：取出数据库中的svg_content 并解析xml格式的svg
            svgcontent = getSvgContentFromDB(db, sql, goodsId)
            if len(svgcontent)!= 0:
                svgcontent_db = parseXml(svgcontent) # 根据读取到的str,解析成svg list
                if svgcontent_db==svgcontent_model:
                    print("svglist对比结果:","True")
                else:
                    print("svglist对比结果:","False")
                    print("sql:",sql)
                    print("svgcontent_db:",svgcontent_db)
                    print('svgcontent_model:',svgcontent_model)
                print("-"*50)
            else:
                print('[Error]数据库中svgcontent字段为空,sql:',sql,'goodsId:',goodsId)
                print('svgcontent_model:',svgcontent_model)
                print("-"*50)

    db.close()