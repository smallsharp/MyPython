#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import pymysql.cursors
import certifi
import urllib3

# 访问数据库
# 定义配置信息
config = {
          'host':'100.114.31.253', # 线上ip
          'port':3306,
          'user':'artsfetch',
          'password':'artsfetchpassword',
          'db':'goods',
          'charset':'utf8mb4',
          'cursorclass':pymysql.cursors.DictCursor,
          }
SQL = 'select image_path from tude_goods_user_diy;'


# The PoolManager will automatically handle certificate verification and will raise SSLError if verification fails:
http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())


def getReponseData(sql):
    conn = pymysql.connect(**config)
    with conn.cursor() as cursor:
        cursor.execute(sql)
        data = cursor.fetchall()
        # print(data)
        cursor.close()
        conn.close()
    return data

# 将数据库取出的字段，加上前缀，拼接成可以访问的地址，并且放到imgUrlList中
imgUrlList=[]
for i in getReponseData(SQL):
    imgUrl = "https://imgex.Python.com/imgsrv/" + (i['image_path'])
    imgUrlList.append(imgUrl)

# 访问url地址，并获取返回值
def getImgCode(url):
    r = requests.get(url)
    return r.status_code


# 开始执行
if __name__ == '__main__':
    errorImgList = []
    length = len(imgUrlList) # 获取总条数
    for url in imgUrlList:
        print("一共有%s条记录，正在读取第%s条记录"%(length,imgUrlList.index(url)))
        print(url)
        if  getImgCode(url)!=200:
            print(url,"Fail",getImgCode(url))
            errorImgList.append(url)

    for img in errorImgList:
        print(img)
