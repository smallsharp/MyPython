import requests
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

session = None

def get_session():
    """
    通过登录 获取session
    :return:
    """
    global session
    login_url = "https://m.taidu.com/memberSite/sso/loginJson"
    login_params = {"loginAccount": "18521035133", "password": "111111", "clientType": "Android", "abbr": "CN"}
    session = requests.Session()
    # session.keep_alive=False
    requests.adapters.DEFAULT_RETRIES = 5
    session.get(url=login_url, params=login_params)
    cookies = session.cookies
    return session

"""
第一种：post 提交form表单数据
"""
def login():
    login_url = "https://app.cmall.com/memberSite/sso/loginJson"
    login_params = {"loginAccount": "18855550001", "password": "111111", "clientType": "ios", "abbr": "CN"}
    res = requests.post(url=login_url, data=login_params)
    # print(res.text)
    return res

"""
第二种：post 提交json格式数据
"""

def  xxxx():
    import json
    jsondata = {"name":"xxx","xx":"xxx"}
    res = requests.post(url="xxx",json=json.loads(jsondata))
    print(res)


def cartlist():
    url = "https://app.cmall.com/orderPaySite/tude/cart/cartList"
    params = {"abbr": "CN", "pageNo": "1", "clientType": "H5", "pageSize": 30}


    # 通过带 session的cookies 请求
    # res = requests.post(url=url, data=params, cookies=session.cookies)

    # 通过带cookies 请求
    res = requests.post(url=url, data=params, cookies=login().cookies)
    print(res.text)
    print(res.cookies)


def main():
    get_session()
    cartlist()


if __name__ == '__main__':
    # main()
    # login()
    cartlist()