# coding=utf-8
import requests

# 1.请求的url
url = "https://m.taidu.com/goodsSite/home/categoryProductList"
# url = "https://m.taidu.com/goodsSite/home/categoryProductList?abbr=CN&clientType=H5&clientVersion="

# 2.请求参数
params = {"abbr": "CN", "clientType": "H5","clientVersion":""}

# 3.请求header
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

# 4.发送请求
res = requests.get(url,params,headers = headers)


# 5.响应的状态码
print("status_code：",res.status_code)

# 6.响应的文本
print("response text：",res.text)

# 7.响应的文本（字节）
print("response content:",res.content)

with open(file="res_content.json",mode="wb") as f:
    f.write(res.content)

# 8.响应的结果编码
print("response encoding:",res.encoding)

# 转成json格式
# print("response json:",res.json())

# 9.响应的头信息
print("response headers:",res.headers)

# 10.响应的cookies
print("response cookies:",res.cookies)

for k,v in res.cookies.items():
    print("cookies:{}={}".format(k,v))

# 11.响应的url
print("response url:",res.url)

# 12.响应的请求历史
print("response history:",res.history)
