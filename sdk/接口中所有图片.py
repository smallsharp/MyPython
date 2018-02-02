
from urllib import request
import certifi
import json
import requests
import time
import urllib
import urllib3
http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())

prefix_imgex = 'https://imgex.Python.com/imgsrv/'
prefix_image = 'https://image.Python.com/imgsrv/'
        
def skuniCodeList():
    url = "https://apimerch.Python.com/restwsapis/product/getSkuProductList?clientId=d83fcd1f-2ad8-41b5-981d-3342548c768e&clientSecret=0927150e-64fd-4191-85c2-b9b5c34d5a17&sign=7DEOBTAINREUSLTOBTAINREUSLTC6489BOBTAINREUSLTCBDDD141B3756F08D8E2";
    try:
        res = urllib.request.urlopen(url)
        if res is not None:
            resJson = json.loads(res.read())
            result = resJson['result']
            skuiCode = []
            for re in result:
                for r in result[re]:
                    skuiCode.append(r['skuniCode'])
        else:
            print("res is none")
    except:
        print("error","sku")
    return skuiCode

def goodsInfo(skuniCode):
    url = "https://apimerch.Python.com/restwsapis/goods/getGoodsInfo?clientId=d83fcd1f-2ad8-41b5-981d-3342548c768e&clientSecret=0927150e-64fd-4191-85c2-b9b5c34d5a17&osVersion=6.0&sign=06D266220OBTAINREUSLTD0C2OBTAINREUSLT35486FC5CF1172058&skuniCode=%s"%skuniCode
    res = urllib.request.urlopen(url)
    resJson = json.loads(res.read())
    dict = {}
    if resJson is not None:
        try:
            goodsInfoVos = resJson['result'][0]['goodsInfoVos'] # result节点中只有1个节点，取出goodsInfoVos数据
            goodsImgList = []
            for goods in goodsInfoVos:
                img = goods['goodsImagePath']
                goodId = goods['goodsId']
                goodsImgList.append(img)
                dict[goodId] = img
        except Exception as e:
            print("res:",resJson,e)
    else:
        print("goodsInfo is none")
    return dict

# {'appJson': {'nodeName': 'S090QM001', 'backgroundColor': '', 'outLineMaskUrl': 'stag/model/upload/Tee001_3D/Temp/S090QM001.png', 'thumbilUrl': 'diyrelease/user/h5_3d_1503484843668.png', 'texts': [{'text': 'ATTITUDE', 'defaultText': '我是默认的文本', 'fontName': 'NotoSansHans-Black', 'textColor': '#ffffff', 'fontSize': 111.09813974586993, 'dy': 0, 'isLocked': 1, 'matrix': {'translateX': 39.24500751293988, 'translateY': 313.4146201299649, 'scale': 0.7879915688587728, 'rotate': 0}, 'matrixString': 'matrix(0.7879915688587728,0,0,0.7879915688587728,39.24500751293988,313.4146201299649)'}], 'materials': [{'orig_width': 394, 'orig_height': 150, 'remoteImageUrl': 'diyrelease/Python/o_1bo7aqhlno4o15hnrc3usc7de3a.png', 'remoteOriginalImageUrl': 'diyrelease/Python/o_1bo7aqhlno4o15hnrc3usc7de3a.png', 'matrix': {'translateX': 15.577348637297405, 'translateY': 164.468533745164, 'scale': 1.22041955006448, 'rotate': 0}, 'matrixString': 'matrix(1.22041955006448,0,0,1.22041955006448,15.577348637297405,164.468533745164)', 'isLocked': 1}], 'userImage': {'orig_width': 564, 'orig_height': 564, 'remoteImageUrl': 'diyrelease/Python/o_1bo7aq869s44cmfou7t07pv7g.jpg', 'remoteOriginalImageUrl': 'diyrelease/Python/o_1bo7aq869s44cmfou7t07pv7g.jpg', 'matrix': {'rotate': 0, 'scale': 0.9078014184397163, 'translateX': 0, 'translateY': 0}, 'matrixString': 'matrix(0.9078014184397163,0,0,0.9078014184397163,0,0)'}}}
def getModelShow(skuniCode,goodId):
    url = "https://apimerch.Python.com/restwsapis/goods/getModelShow?clientId=d83fcd1f-2ad8-41b5-981d-3342548c768e&clientSecret=0927150e-64fd-4191-85c2-b9b5c34d5a17&goodsId=%s&sign=1757B4D7OBTAINREUSLT1CE3FOBTAINREUSLT2094857D9745FC340&skuniCode=%s&source=1"%(goodId,skuniCode)
    try:
        res = urllib.request.urlopen(url)
        print(url)
        if res is not None:
            resJson = json.loads(res.read())
            modelData = resJson['result']['modelJson'] # 截取modelJson
            modelJson = json.loads(modelData) # 返回的是json数据，需要再次解析
            nodes = modelJson['TDModel']['nodes']
            imgList = []
            for n in nodes:
                dict = n
                back = dict.get('appJson').get('backgroundColor')
                out = dict.get('appJson').get('outLineMaskUrl')
                thum = dict.get('appJson').get('thumbilUrl')
                if back != '' and back is not None and back not in imgList:
                    imgList.append(back)
                if out != ''and out is not None and out not in imgList:
                    imgList.append(out)
                if thum != '' and thum is not None and thum not in imgList:
                    imgList.append(thum)
                    
                materials = dict.get('appJson').get('materials') # 取出materials节点下的数据，materials是个list
                if materials is not None:
                    for m in materials:
                        remoteMater = m.get('remoteImageUrl')
                        remoteOrigMater = m.get('remoteOriginalImageUrl')
                        if remoteMater != '' and remoteMater is not None and remoteMater not in imgList:
                            imgList.append(remoteMater)
                        if remoteOrigMater != '' and remoteOrigMater is not None and remoteOrigMater not in imgList:
                            imgList.append(remoteOrigMater)
                            
                userImage = dict.get('appJson').get('userImage')
                if userImage is not None:
                    remoteUser = userImage.get('remoteImageUrl')
                    remoteOriUser = userImage.get('remoteOriginalImageUrl')
                    if remoteUser != '' and remoteUser is not None and remoteUser not in imgList:
                        imgList.append(remoteUser)
                    if remoteOriUser != '' and remoteOriUser is not None and remoteOriUser not in imgList:
                        imgList.append(remoteOriUser)
    except Exception as e:
        print("Error:",e)
    return imgList

def run():
    for skuniCode in skuniCodeList():
        for goodsId,img in goodsInfo(skuniCode).items():
            imgPath = prefix_imgex + img
                # 访问goodsInfo中的所有图片
#                 res = urllib.request.urlopen(imgPath)
#                 print(imgPath,goodsId)
                # 访问getModelShow,获取modelJson中的所有图片资源
            try:
                print("开始请求, ",'skuniCode:',skuniCode,', goodsId:',goodsId)
                imgList2 = getModelShow(skuniCode,goodsId)
#                 print('图片集合：',imgList2)
                for imgPath in imgList2:
                    if imgPath.find('http')==-1:
                        imgPath = prefix_imgex + imgPath
                    try:
                        response = urllib.request.urlopen(imgPath)
#                         print('Ok:',imgPath)
                    except Exception as e:
                        print("Error1:",imgPath)
#                 print('*'*90)
            except Exception as e:
                print("ERROR:",imgPath,e)

   
if __name__ == '__main__':
    startTime = time.time()
    print("开始执行脚本，当前时间：",startTime)
    run()
    endTime = time.time()
    print("全部执行完毕，结束时间：",endTime)
    print("总耗时:",endTime-startTime)
    
      

        
    
    