import requests

cookies = None

def updateCookies():
    '''
    通过登录的方式获取cookies
    :return:cookies
    '''
    global cookies
    url = 'https://apibeta.yunchehome.com/user/login'
    data = {"mobile": "18516213133", "password": "123456", "captcha": ""}
    res = requests.post(url, json=data)
    cookies = res.cookies
    return cookies


def getCookies():
    if not cookies:
        print('update')
        return updateCookies()
    return cookies


def addIncome():
    url = 'https://apibeta.yunchehome.com/newCost/bill/doAdd'

    data = {
        "billType": 1,
        "data": "{\"startTime\":\"2018-10-01\",\"totalMoneyE2\":\"8000\",\"feeTypeId\":\"2375\",\"companyName\":\"北京百度网讯科技有限公司\",\"companyTypeId\":\"2441\",\"paymentTime\":\"2018-10-12\"}",
        "routerName": "incomeTally"
    }

    res = requests.post(url, json=data, cookies=getCookies())
    print(res.text)


for i in range(101):
    print(i)
    addIncome()
