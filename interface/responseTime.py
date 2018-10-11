import requests


def getLogs():
    url = 'https://xcxapi.yunchehome.com/main/getLogs'

    params = {
        "openId": "o94HS5PrLEd6AeyLRM5XimFX90tU"
    }


    res = requests.post(url,json=params)

    print(res.elapsed.total_seconds())


getLogs()