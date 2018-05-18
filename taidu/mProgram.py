import requests


def addAddress(shipper, mobile, address):
    url = "https://m.cmall.com/memberSite/memberAddress/addOrUp"
    params = {'isDefault': '0', 'addressId': '', 'shipperName': shipper, 'mobile': mobile, 'address': address,
              'abbr': 'CN', 'clientType': 'mp', 'clientVersion': '1.0.0'}
    headers = {'token': 'b87885f4fee840045a29fac3723'}
    res = requests.post(url, data=params, headers=headers)
    return res.text


def wxGetSign():
    url = 'https://m.cmall.com/orderPaySite/tude/pay/getSign'
    params = {'orderNo': '115258595301210144', 'totalAmount': '1', 'tradeType': 'XCX',
              'body': '%E8%93%9D%E7%89%99%E8%BF%B7%E4%BD%A0%E9%9F%B3%E5%93%8D%2C',
              'openid': 'oJTEi0Ye1zn_ZypQ_C1s6ymCbbCg', 'token': 'b87885f4fee840045a29fac3723',
              'clientId': '365b05fd-fc45-44c3-957f-817c00c716bb',
              'clientSecret': '0d7187d0-d3f0-4204-901b-30ff2fdf3c3c', 'abbr': 'CN', 'clientType': 'mp',
              'userId': 'txhy_dz', 'version': '2.0.0', 'sign': '3449c9e5e332f1dbb81505cd739fbf3f'}
    headers = {'token': '9636147322f55ee0b775e352fe0'}
    # 参数是form
    res = requests.post(url, data=params, headers=headers)
    return res.text


def add2Cart():
    url = 'https://m.taidu.com/goodsSite/userDiy/saveDiyGoodsAndAddShopCart'
    params = {
	"skuniCode": "10081_10081104_10103",
	"productId": 10081,
	"goodsId": "7429",
	"goodsType": 2,
	"clientVersion": "3.0.3",
	"userId": "",
	"buyGoodsInfoVos": [{
		"number": 1,
		"productDetailCode": 10081104,
		"salePrice": 170,
		"skuGroup": "LEVEL,10103#OPTION,10003#SIZE,S"
	}],
	"mchCode": "#36227",
	"words": "[]",
	"imgUri": "[{\"matrix\":\"matrix(0.18795993797196078 0 0 0.18795993797196078 425.0200310140196 431.0200310140196)\",\"height\":1000,\"maskX\":425.0200310140196,\"maskY\":431.0200310140196,\"width\":1000,\"isSuit\":\"N\",\"id\":\"\",\"imgFlag\":2,\"url\":\"diyrelease/cmall/o_1cdeirvvv1occo771a3q118ui59v.png\"}]",
	"opusUri": "https://imgex.cmall.com/imgsrv/nospc/html5/3tQn5Bc2ka2018_5_16_16.png",
	"abbr": "CN",
	"clientType": "H5"
}
    headers = {'token': '762aef2031e44bf29191bbb99b0'}

    # 参数本身是json
    res = requests.post(url, json=params, headers=headers)

    return res.text




if __name__ == '__main__':
    # print(wxGetSign())

    for i in range(100):
        print(i)
        print(add2Cart())
    # for i in range(0, 20):
    #     addAddress('我是收货人{}'.format(i), 18866667777, '这里是收货地址'.format(i))
    #     print(i)
