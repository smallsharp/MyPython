# -*- coding: UTF-8 -*-
import urllib.request
import http.cookiejar

url = 'https://imgex.Python.com/imgsrv/1237/o_19qlfvlr0opi5bb2f51rs61lah24.jpg'


print("第一种测试方法")

response1 = urllib.request.urlopen(url)

print(response1.getcode())

print(len(response1.read()))


print("第二种测试方法")

request = urllib.request.Request(url)

request.add_header('user-agent', 'Mozilla/5.0')

resopnse2 = urllib.request.urlopen(request)

print(resopnse2.getcode())

print(len(resopnse2.read()))


print("第三种测试方法")

cj = http.cookiejar.CookieJar()

opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

urllib.request.install_opener(opener)

resopnse3 = urllib.request.urlopen(url)

print(resopnse3.getcode())
print(len(resopnse3.read()))
print(cj)