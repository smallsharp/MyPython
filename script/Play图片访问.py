#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
import requests
import json
#from test_excel import color
import time

# reload(sys)
# sys.setdefaultencoding('utf-8')
#获取首页分类的数据
def getHomeCategory():
    url="https://android.Python.com/gdCategorySite/category/getHomeCategory?clientVersionType=2&abbr=CN&client=android&clientType=android&clientVersion=1.0&osVersion=22&page=index"
    r = requests.get(url,verify=False)
    rlt = json.loads(r.text)
    if rlt['result']==None or rlt['result']=='':
        return None
    else:
        #获取分类的一级code,一级首页的分类图片
        list=[]
        for i in rlt['result']:
            list.append(i['icon'])
        return  list
# code =[101,100,113,103,104,102,114,115,112]
# print getHomeCategory()

#根据一级分类code，查询二级分类的产品code和imagePath
def productImageList(categoryCode):
    url="https://m.Python.com/goodsSite/home/productImageList?abbr=CN&categoryCode=%s"%categoryCode
    r = requests.get(url,verify=False)
    rlt = json.loads(r.text)
    if rlt['result']==None or rlt['result']=='':
        return None
    else:
        #获取产品code和产品对应的封面图片
        dict={}
        for i in rlt['result']:
            dict[i['productCode']]=i['imagePath']
        return  dict

# print productImageList(101)

#根据产品id，查询所有产品下的商品列表
def goodslist(productId):
    url = "https://android.Python.com/goodsSite/home/goodsList?clientVersionType=2&abbr=CN&client=android&clientType=android&clientVersion=1.0&productId=%s"%productId
    r = requests.get(url,verify=False)
    rlt = json.loads(r.text)
    if len(rlt['result']['pageItems'])==0:
        return None
    else:
        dic = {}
        for j in rlt['result']['pageItems']:
            dic[j['goodsId']]=j['goodsImagePath']
        return dic

# print goodslist(501)
#获取模型里面的所有图片数据
def gotoUserDiy(goodsId):
    parmas = {'loginAccount': 'double', 'password': '111111', 'rememberMe': '1'}
    base_url = "https://www.Python.com/memberSite/sso/loginForOutsideJson"
    s = requests.Session()
    r1 = s.post(base_url, parmas,verify=False)

    hd = {"Content-Type":"application/json"}
    url = "https://android.Python.com/goodsSite/userDiy/gotoUserDiy"
    data = {"clientType":"android","abbr":"CN","userId":"320755","source":"1","goodsId":goodsId}
    r = s.post(url,data=json.dumps(data),headers = hd,verify=False)

    rlt = json.loads(r.text)
    if  rlt['result']=='':
        return None
    else:
        str1=str(rlt['result']['modelJson'])
        #匹配所有""中间的所有字符
        r = r'(?<=").*?(?=")'
        reg = re.compile(r)
        text = re.findall(reg,str1)
        list = []
        for i in text:
            if i.endswith('.jpg') or i.endswith('.png'):
                list.append(i)
            else:
                continue
        return list
#print gotoUserDiy(1283)
#查询所有档次图片
def getLevelSkuList(goodsId):
    url="https://android.Python.com/goodsSite/play/getLevelSkuList?clientVersionType=2&abbr=CN&client=android&clientType=android&clientVersion=1.0&goodsId=%s&goodsType=2&osVersion=22"%goodsId
    r = requests.get(url,verify=False)
    rlt = json.loads(r.text)
    if rlt['result']['colorList']==None or rlt['result']['colorList']=='':
        return None
    else:
        list=[]
        for j in rlt['result']['colorList']:
            list.append(j['skuValue'])
        return  list

#处理图片
def handleImg(img):
    if img.find('http://')==0 or img.find('https://')==0:
        return img
    elif img[0]=='/':
        return "http://imgex.Python.com/imgsrv"+img
    return "http://imgex.Python.com/imgsrv/"+ img

#获取图片返回code
def getImgCode(url):
    r = requests.get(url, verify=False)
    return r.status_code

def imgurlCode(img):
    list_error=[]
    img = handleImg(img)
    if  getImgCode(img)==200:
        #continue
        # sys.stdout.write(color.GREEN)
        print ("*"*50)
        print (img+">>>>>>>200")
    else:
        #list_error.append(img)
        # sys.stdout.write(color.RED)
        print ("#" * 50)
        print (img+">>>>>>>>"+str(getImgCode(img)))


#处理所有图片
def dome():
    LIST=[]
    codelist = [101, 100, 113, 103, 104, 102, 114, 115, 112]
    for img in getHomeCategory():
        LIST.append(img)
        # print "首页分类列表图片处理"
        # imgurlCode(img)
    for code in codelist:
        for productId, imagePath in productImageList(code).items():
            LIST.append(imagePath)
            # print "二级产品分类列表图片处理，产品图片是%s"%productId
            # imgurlCode(imagePath)
        if goodslist(productId)==None:
            print ("产品id是%s的goodslist为空"%productId)
            continue
        else:
            for goodsId,goodsimg in goodslist(productId).items():
                #LIST.append(goodsimg)
                print ("开始处理goodslist")
                print ("产品id是%s的goodsid是%s处理"%(productId,goodsId))
                imgurlCode(goodsimg)
                if gotoUserDiy(goodsId)==None:
                    print ("产品id是%s的goodsid是%s的gotoUserDiy结果为空"%(productId,goodsId))
                else:
                    for i in gotoUserDiy(goodsId):
                        #LIST.append(i)
                        print ("开始处理gotoUserDiy")
                        print ("产品id是%s的goodsid是%s处理" %(productId, goodsId))
                        imgurlCode(i)

print (time.ctime())
dome()
print (time.ctime())
