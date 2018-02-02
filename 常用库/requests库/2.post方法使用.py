import requests



def cartlist():
    url = "https://m.taidu.com/orderPaySite/tude/cart/cartList"

    params = {"abbr": "CN", "pageNo": "1", "clientType": "H5", "pageSize": 30}

    res = requests.get(url=url, params=params)
    res = requests.post(url=url,json=params)

    print(res.text)




if __name__ == '__main__':
    main()
