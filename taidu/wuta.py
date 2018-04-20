import requests


def addAddress():

    param = {'name': 'ws', 'phone': '13355557777', 'zipCode': '223333', 'shippingAddress': '收货地址001', 'isDefault': '0', 'clientType': 'H5', 'abbr': 'CN', 'version': '2.0.0', 'clientId': 'cd467887-40a1-4ff4-84e9-f2729999a1b5', 'clientSecret': 'e983822c-bb98-4d82-aa5e-b209104f811a', 'userId': 'wuta-1', 'sign': '8055F7C31F5A8CBA98134646FFC3BF19'}

    url =  'https://sandboxapimerch.cmall.com/restwsapis/saveAddress'

    res = requests.post(url,data=param)

    print(res.text)

    return res


addAddress()