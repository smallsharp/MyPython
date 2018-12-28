from bs4 import BeautifulSoup

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

soup = BeautifulSoup(html, features='html.parser')

t = soup.find(name='input',attrs={'name':'user'})
t = soup.select_one(selector='input[type="text"]')
print(t)