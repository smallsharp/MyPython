# encoding=utf-8
from bs4 import BeautifulSoup

print("BeautifulSoup使用实例")

html = """
<html>
	<head>
		<meta charset="UTF-8">
		<title>HTML学习</title>
	</head>
	<body style="background-color: PowderBlue">
		<h1 id="test" class="myTest" align="left">自动化测试平台</h1>
		<a href="www.baidu.com" class="link">百度</a>
		<a href="www.taobao.com" class="link">淘宝</a>
		
		<div class="mdiv">
			<form action="">
				<span>用户名：</span>
				<input type="text" name="user" id="user" value="" />
				<span>密码：</span>
				<input type="password" name="pwd" id="pwd" value="" />
				<input type="submit" name="" id="" value="登录L" />
			</form>
			
		</div>
	</body>
</html>

"""

""" 0.初始化soup对象 """
soup = BeautifulSoup(html, "html.parser")
# print(soup.text)

""" 1.通过标签<h1>提取 """
title = soup.select("h1")
print(title)  # [<h1 align="left" class="myTest" id="test">自动化测试平台</h1>]

print(title[0])  # <h1 align="left" class="myTest" id="test">自动化测试平台</h1>

print(title[0]["align"], title[0]["class"], title[0]["id"])  # 提取标签中的属性

print(title[0].text)  # 自动化测试平台

""" 2.通过ID提取,需要加个 # """
title2 = soup.select(selector="#test")
# print(title2)
# print(title2[0])
print(title2[0].text)

""" 3.通过class提取,需要加个 . """
title3 = soup.select(selector=".myTest")
# print(title3)
# print(title3[0])
print(title3[0].text)

""" 4.多个值时 """
alink = soup.select(selector=".link")
# print(alink)
for link in alink:
    print(link)
    print(link['href'], link.text)
