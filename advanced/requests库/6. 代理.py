#coding=utf-8
import requests

"""
设置普通代理
"""
proxies = {
    "http": "http:172.16.5.248",
    "http":"140.205.220.96"
}
# 往请求中设置代理(proxies)

response = requests.get("https://www.baidu.com", proxies=proxies)
print(response.status_code)


"""
设置带有用户名和密码的代理
"""

proxies = {
    "http": "http://user:password@127.0.0.1:9743/",
}
# response = requests.get("https://www.taobao.com", proxies=proxies)
print(response.status_code)


"""
设置socks代理 pip3 install 'requests[socks]
"""
proxies = {
    'http': 'socks5://127.0.0.1:9742',
    'https': 'socks5://127.0.0.1:9742'
}
# response = requests.get("https://www.taobao.com", proxies=proxies)
print(response.status_code)