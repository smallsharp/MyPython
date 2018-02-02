#coding=utf-8
import requests

"""
pip install requests
pip install BeautifulSoup4
"""
url = "https://m.taidu.com/goodsSite/home/categoryProductList"

# 传递参数
payload = {"abbr":"CN","clientType":"H5","clientVersion":None}

# 添加header
headers = {'content-type': 'application/json'}

res = requests.get(url=url,params=payload,headers=headers)

# 响应内容
print(res.text)

# 字节的方式访问请求响应体
print(res.content)

# 返回结果编码
print(res.encoding)

# 转成json格式
print(res.json())



