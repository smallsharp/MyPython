# coding=utf-8
"""
@Time:2018-03-1019:19
@Author:lfl5207
"""
import requests


def str2dict(str_f):
    dictF = dict()
    list_one = str_f.split('&')
    for l in list_one:
        list_t = l.split("=")
        key, value = list_t[0], list_t[1]
        dictF[key] = value
    return dictF

def login():
    login_url = "https://app.cmall.com/memberSite/sso/loginJson"
    login_params = {"loginAccount": "18833330001", "password": "111111", "clientType": "ios", "abbr": "CN"}
    res = requests.post(url=login_url, data=login_params)
    # print(res.text)
    return res


if __name__ == '__main__':

    res = login()
    str = "payableAmount=6&orderUrl=nospc%2FiOS%2Frandom%2F6014EE38302E994FE030EACFF0DFD4E7.jpg"

    str = str2dict(str)

    url = "https://app.cmall.com/orderPaySite/merchant/pay/offlineRecharge"
    res = requests.post(url=url, data=str,cookies= res.cookies)

    print(res.text)
