# encoding=gbk
import requests
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')


def login():
    login_url = "https://m.taidu.com/memberSite/sso/loginJson"
    login_params = {"loginAccount": "18521035133", "password": "111111", "clientType": "Android", "abbr": "CN"}
    session = requests.Session()
    session.get(url=login_url, params=login_params)
    return session


def all_user_diy(session):
    diy_url = "https://m.taidu.com/goodsSite/userDiy/queryAllUserDiy"
    session.params = {"abbr": "CN", "clientType": "h5", "pageNo": 1, "pageSize": 20}
    session.headers = {
        'Connection': 'keep-alive'
    }
    r = session.get(url=diy_url, json=session.params, headers=session.headers, )
    return r.json()


def parse_all_user_diy(response):
    result = response.get("result", None)
    res = []
    if result:
        page_items = result.get("pageItems")
        if page_items:
            for item in page_items:
                diy_dict = {}
                diy_dict["goodsId"] = item.get("goodsId")
                diy_dict["goodsName"] = item.get("goodsName")
                diy_dict["goodsType"] = item.get("goodsType")
                diy_dict["productDesignType"] = item.get("productDesignType")
                res.append(diy_dict)
            return res


def main():
    session = login()
    js = all_user_diy(session)
    res = parse_all_user_diy(js)
    print(res)


if __name__ == '__main__':
    main()
