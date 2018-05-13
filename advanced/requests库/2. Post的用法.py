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
    login_params = {'loginAccount': '18521035133', 'password': '111111', 'code': '', 'rememberMe': '1', 'clientType': 'H5', 'abbr': 'CN', 'clientVersion': '', 'sign': '87823FC7334C13955C8B451B48027954'}
    session = requests.Session()
    # session.keep_alive=False
    requests.adapters.DEFAULT_RETRIES = 5
    session.get(url=login_url, params=login_params)
    cookies = session.cookies
    return session


# 第一种：post 提交form表单数据
def login_with_data():
    login_url = "https://app.cmall.com/memberSite/sso/loginJson"
    login_params = {"loginAccount": "18855550001", "password": "111111", "clientType": "ios", "abbr": "CN"}
    res = requests.post(url=login_url, data=login_params)
    return res


# 第二种：post 提交json格式数据
def login_with_json():
    login_url = "https://app.cmall.com/memberSite/sso/loginJson"
    login_params = {"loginAccount": "18855550001", "password": "111111", "clientType": "ios", "abbr": "CN"}
    res = requests.post(login_url,json=login_params)
    return res


def cartlist():
    url = "https://app.cmall.com/orderPaySite/tude/cart/cartList"
    params = {'pageSize': '100', 'currPage': '1', 'status': '0%2C21%2C22', 'clientType': 'H5', 'abbr': 'CN', 'clientVersion': '', 'sign': '2E269FE54CF9E1C08396EA94F056DEE9'}

    # 通过带 session的cookies 请求

    for k,v in get_session().cookies.items():
        print(k,v)
    res = requests.post(url=url, data=params, cookies=get_session().cookies)

    # 通过带cookies 请求
    # res = requests.post(url=url, data=params, cookies=login_with_data().cookies)
    print(res.text)
    print(res.cookies)


def main():
    # get_session()
    cartlist()


if __name__ == '__main__':
    # print(login_with_json())
    # print(login_with_data())
    main()
