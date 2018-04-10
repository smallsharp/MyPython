#coding=utf-8
import requests
import sys
import io
from requests.packages import urllib3
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
    urllib3.disable_warnings()
    session.get(url=login_url, params=login_params,verify=False) # verify=False 关闭证书验证，但是仍然会报出证书警告
    cookies = session.cookies
    for c,v in cookies.items():
        print(c,v)
    return session


def all_user_diy():
    diy_url = "https://m.taidu.com/goodsSite/userDiy/queryAllUserDiy"
    params = {"abbr": "CN", "clientType": "h5", "pageNo": 1, "pageSize": 20}
    res = requests.get(url=diy_url,params=params,cookies=session.cookies)
    return res.json()

def main():
    get_session()
    print(all_user_diy())

if __name__ == '__main__':
    main()