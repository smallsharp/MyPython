# coding=utf-8
import requests

url = "https://m.taidu.com/goodsSite/home/categoryProductList"

# 传递参数
params = {"abbr": "CN", "clientType": "H5", "clientVersion": None}

# 添加header
headers = {'content-type': 'application/json'}

res = requests.get(url=url, params=params, headers=headers)

"""
响应内容
"""
# 响应的状态码
print("status_code：",res.status_code)

# 文本
print("response text：",res.text)

# 字节的方式访问请求响应体
print("response content:",res.content)

with open(file="res_content.json",mode="wb") as f:
    f.write(res.content)

# 返回结果编码
print("response encoding:",res.encoding)

# 转成json格式
print("response json:",res.json())

print("response headers:",res.headers)

print("response cookies:",res.cookies)

for k,v in res.cookies.items():
    print("cookies:{}={}".format(k,v))

print("response url:",res.url)

print("response history:",res.history)
