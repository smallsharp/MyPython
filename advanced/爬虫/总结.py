"""
参考博客：https://www.cnblogs.com/wupeiqi/articles/6283017.html

	需求：
		1. 爬取汽车之家新闻咨询
			- 什么都不带
		2. 爬抽屉新热榜
			- 带请求头
			- 带cookie
			- 登录：
				- 获取cookie
				- 登录：携带cookie做授权
				- 带cookie去访问
		3. 爬取GitHub
			- 带请求头
			- 带cookie
			- 请求体中：
				commit:Sign in
				utf8:✓
				authenticity_token:hmGj4oS9ryOrcwoxK83raFqKR4sFG1yC09NxnDJg3B/ycUvCNZFPs4AxTsd8yPbm1F3i38WlPHPcRGQtyR0mmw==
				login:asdfasdfasdf
				password:woshiniba8

		4. 登录拉勾网
			- 密码加密
				- 找js，通过python实现加密方式
				- 找密文，密码<=>密文

			- Referer头， 上一次请求地址，可以用于做防盗链。

	总结：
		请求头：
			user-agent
			referer
			host
			cookie
			特殊请起头，查看上一次请求获取内容。
				'X-Anit-Forge-Code':...
				'X-Anit-Forge-Token':...
		请求体：
			- 原始数据
			- 原始数据 + token
			- 密文
				- 找算法
				- 使用密文

		套路：
			- post登录获取cookie，以后携带cookie
			- get获取未授权cookie，post登录携带cookie去授权，以后携带cookie
"""
