# coding=utf-8

import requests
import json
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

GET = "get"
POST = "post"


def req():
    """
    请求下级数据
    :return:
    """
    url = "https://innermerch.cmall.com/merchantSupportSite/user_op/getChildUser"
    # data = """
    #     {"token":"XDDFEADSSFE"}
    # """
    # res = requests.post(url=url, json=json.loads(data))

    data = {"token":"XDDFEADSSFE"}
    res = requests.post(url,data)

    try:
        for item in res.json()["result"]:
            if item.get("userName") == "t3":
                print("结果通过！")
            else:
                print("失败了！")
    except Exception as e:
        print("接口返回错误:",e)


def show():
    url = "https://apimerch.cmall.com/restwsapis/goods/getModelShow"

    header = {"Content-Type": "application/json"}
    data = {
        "abbr": "CN",
        "clientType": "web",
        "goodsId": "4053",
        "modelClassId": "2451",
        "clientId": "d83fcd1f-2ad8-41b5-981d-3342548c768e",
        "productDesignType": "2",
        "clientSecret": "0927150e-64fd-4191-85c2-b9b5c34d5a17",
        "skuniCode": "501_501100_0",
        "source": "1",
        "sign": "7E84E5BF6C2CFF54735BE3AD5A117706",
        "clientVersion": ""
    }

    # res = requests.get(url, data, headers=header)
    res = requests.get(url, params=data, headers=header)
    print(res.text)


def goods():
    url = "https://www.taidu.com/goodsSite/home/productGoodsList"
    header = {"Content-Type": "application/json"}
    param = {"abbr": "CN", "clientType": "web", "productId": "501", "skuGroup": "", "clientVersion": ""}
    # res = requests.get(url, param, headers=header)
    res = requests.get(url, param, headers=header)
    print(res.text)


def cate_goods():
    url = "https://www.taidu.com/goodsSite/home/categoryGoodsList"
    param = {"abbr": "CN", "categoryCode": "101", "clientType": "web", "clientVersion": ""}
    # res = requests.get(url,param)
    # print(res.text)
    print(con(url, param).text)


def con(url, params, method="get", **kwargs):
    """
    请求
    :param url:
    :param params:
    :param method:
    :param kwargs:
    :return:
    """
    if method.lower().strip() == "get":
        return requests.get(url, params, **kwargs)
    elif method.lower().strip() == "post":
        return requests.post(url, data=params, **kwargs)
    else:
        raise KeyError("暂不支持的请求方式！")


if __name__ == '__main__':
    # cate_goods()
    req()
