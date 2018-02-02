#encoding=utf-8
from bs4 import BeautifulSoup

html_sample ="""
<html>
<head>
<meta charset="UTF-8">
<title>HTML学习</title>
</head>
<body style="background-color: PowderBlue">
<h1 id="test" class="myTest" align="left">自动化测试平台</h1>
<a href="www.baidu.com" class="link">百度</a>
<a href="www.taobao.com" class="link">淘宝</a>

</body>
</html>
"""
# print(res.text)
soup = BeautifulSoup(html_sample,"html.parser")
# print(soup.text)
title = soup.select("h1") # 1.通过标签<h1>提取
print(title) # [<h1 align="left" class="myTest" id="test">自动化测试平台</h1>]
print(title[0]) # <h1 align="left" class="myTest" id="test">自动化测试平台</h1>
print(title[0]["align"],title[0]["class"],title[0]["id"]) # 提取标签中的属性

print(title[0].text) # 自动化测试平台

title2 = soup.select(selector="#test") # 2.通过ID提取
# print(title2)
# print(title2[0])
print(title2[0].text)


title3 = soup.select(selector=".myTest") # 3.通过class提取
# print(title3)
# print(title3[0])
print(title3[0].text)

alink = soup.select(selector=".link") # 有多个值时
# print(alink)
for link in alink:
    print(link)
    print(link['href'],link.text)