# coding=utf-8
import requests
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')


response = requests.get('http://www.jianshu.com/404.html')
# 使用request内置的字母判断状态码
if not response.status_code == requests.codes.ok:
    print('404-1')


response = requests.get('http://www.jianshu.com')
# 使用状态码数字判断
if not response.status_code == 200:
    print('404-2')