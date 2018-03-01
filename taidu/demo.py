# coding=utf-8

import requests
import json


def req():
    """
    请求下级数据
    :return:
    """
    url = "https://innermerch.cmall.com/merchantSupportSite/user_op/getChildUser"
    data = """
        {"token":"XDDFEADSSFE"}
    """
    res = requests.post(url=url, json=json.loads(data))

    try:
        for item in res.json()["result"]:
            if item.get("userName") == "t3":
                print("结果通过！")
            else:
                print("失败了！")
    except Exception:
        print("接口返回错误！")


if __name__ == '__main__':

    for i in range(100):
        req()
