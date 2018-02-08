# coding=utf-8
import requests
from requests.packages import urllib3


requests.adapters.DEFAULT_RETRIES = 5

# 在请求https时，request会进行证书的验证，如果验证失败则会抛出异常
response = requests.get('https://www.12306.cn')
print(response.status_code)

# 关闭验证，但是仍然会报出证书警告
response = requests.get('https://www.12306.cn',verify=False)
print(response.status_code)

# 关闭警告
urllib3.disable_warnings()
response = requests.get('https://www.12306.cn',verify=False)
print(response.status_code)

# 设置本地证书
response = requests.get('https://www.12306.cn', cert=('/path/server.crt', '/path/key'))