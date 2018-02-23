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
post 用法
"""
def cartlist():
    url = "https://m.taidu.com/orderPaySite/tude/cart/cartList"
    params = {"abbr": "CN", "pageNo": "1", "clientType": "H5", "pageSize": 30}
    res = requests.post(url=url,data=params,cookies=session.cookies)
    print(res.text)
    print(res.cookies)

def main():
    get_session()
    cartlist()

if __name__ == '__main__':
    main()
