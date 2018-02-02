#coding=utf-8

import json
from urllib import request
import urllib
import re

# try:
#     jsonfile = open('homedata.json',encoding='utf-8')
#     jsonData = json.load(jsonfile)
#     print(jsonData['message'])
# finally:
#     if jsonfile:
#         jsonfile.close()

# 和上述写法一致，不用手动关闭文件,注意：encoding要加上
with open('homedata.json','r',encoding='utf-8') as f:
    jsondata = json.load(f)
    skuList = jsondata['result']
    codeList = []
    for s in skuList:
        skuniCode = s['skuniCode']
        goodsurl = """
            http://sandboxapimerch.Python.com/restwsapis/goods/getGoodsInfo?abbr=CN&build=1.0&clientId=d83fcd1f-2ad8-41b5-981d-3342548c768e&clientSecret=0927150e-64fd-4191-85c2-b9b5c34d5a17&clientType=android&clientVersionType=3&country=CN&dBrand=google&osVersion=6.0.1&picHeight=0&picWidth=0&productId=501&sign=12B237B32F3603E4C6867AB9598EC453&skuniCode=%s&st=270&version=3.0
        """%skuniCode
        try:
            res = urllib.request.urlopen(goodsurl)
            print("skuniCode:%s, 返回结果：%s"%(skuniCode,res.getcode()))
            resdata = res.read().decode('utf-8')
            jsonstr = json.loads(resdata)
            result = jsonstr['result']

            if result is not None:
                for r in result:
                    for g in r['goodsInfoVos']:
                        goodsId = g['goodsId']
                        modelurl = """
                            http://sandboxapimerch.Python.com/restwsapis/goods/getModelShow?abbr=CN&build=1.0&clientId=d83fcd1f-2ad8-41b5-981d-3342548c768e&clientSecret=0927150e-64fd-4191-85c2-b9b5c34d5a17&clientType=android&clientVersionType=3&country=CN&dBrand=google&goodsId=%s&osVersion=6.0.1&sign=614D31687B8734B149C7A5525E8F483C&source=1&st=270&version=3.0
                        """%goodsId
                        try:
                            res1 = urllib.request.urlopen(modelurl)
                            print("goodsId:%s,请求getModelShow返回结果：%s"%(goodsId,res1.getcode()))
                            resdata1 = res1.read().decode('utf-8')
                            jsonstr1 = json.loads(resdata1)
                            result1 = jsonstr1['result']
                            if result1 is not None:
                                modelPath = result1['modelPath']
                                match = re.search(r'(\w*)/(\w*)/(\w*)/(\w*)', modelPath)
                                modelName_m = match.group(4)
                                modelName = result1['modelName']
                                if modelName==modelName_m:
                                    print("模型名称匹配成功")
                                else:
                                    print("匹配失败，正则取出的是:%s,实际是:%s"%(modelName_m,modelName),type(modelName),type(modelName_m),len(modelName),len(modelName_m))
                            else:
                                print("result is null")
                        except Exception as e1:
                            print("error,goodsId:%s,请求getModelShow返回结果：%s"%(goodsId,res1.getcode()))
                        
                print("-"*50)
        except Exception as e:
            print("error,skuniCode:%s, 返回结果：%s"%(skuniCode,res.getcode()))
            
        
            
        
        
    
        