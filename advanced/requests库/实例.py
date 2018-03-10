# coding=utf-8
"""
@Time:2018-03-1017:56
@Author:lfl5207
"""

import requests
from configparser import ConfigParser

host = ''

def get_host():
    global host
    parser = ConfigParser()
    parser.read('interface.prop')
    host = parser.get("server", "host_ios")
    return host

def req(url, param, method, **kwargs):
    if method == "get":
        requests.get(url=url, params=param, **kwargs)
    elif method == 'post':
        requests.post(url=url, data=param, **kwargs)
    pass


def login():
    login_url = "https://app.cmall.com/memberSite/sso/loginJson"
    login_params = {"loginAccount": "18833330001", "password": "111111", "clientType": "ios", "abbr": "CN"}
    res = requests.post(url=login_url, data=login_params)
    # print(res.text)
    return res


if __name__ == '__main__':

    host = get_host()
    uri = "/memberSite/sso/loginJson"
    url = host + uri
    login_params = {"loginAccount": "18844440003", "password": "0003taidu", "clientType": "ios", "abbr": "CN"}

    res = requests.post(url,login_params)
    print(res.text)
