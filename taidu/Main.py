# coding=utf-8
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
    requests.adapters.DEFAULT_RETRIES = 5
    session.get(url=login_url, params=login_params)
    return session


def all_user_diy():
    diy_url = "https://m.taidu.com/goodsSite/userDiy/queryAllUserDiy"
    params = {"abbr": "CN", "clientType": "h5", "pageNo": 1, "pageSize": 20}
    res = requests.get(url=diy_url, params=params, cookies=session.cookies)
    return res.json()


def main():
    get_session()
    print(all_user_diy())


if __name__ == '__main__':
    main()
