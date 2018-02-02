'''
Created on 2017年11月9日

cookie.save的参数说明：

ignore_discard的意思是即使cookies将被丢弃也将它保存下来；

ignore_expires的意思是如果在该文件中cookies已经存在，则覆盖原文件写入。

在这里，我们将这两个全部设置为True。

@author: cm
'''
from urllib import request
from http import cookiejar

if __name__ == '__main__':

    #设置保存cookie的文件，同级目录下的cookie.txt
    filename = 'cookie.txt'
    #声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
    cookie = cookiejar.MozillaCookieJar(filename)
    #利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
    handler=request.HTTPCookieProcessor(cookie)
    #通过CookieHandler创建opener
    opener = request.build_opener(handler)
    #此处的open方法打开网页
    response = opener.open('http://www.baidu.com')
    #保存cookie到文件
    cookie.save(ignore_discard=True, ignore_expires=True)