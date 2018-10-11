import requests
import json

PREFIX_BETA = 'https://betawx.yunchehome.com'
PREFIX_ONLINE = 'https://xcxapi.yunchehome.com'


class Card:

    def __init__(self):
        self.uid = 8473
        self.openId = "o94HS5PrLEd6AeyLRM5XimFX90tU"
        self.prefix = 'https://betawx.yunchehome.com'

    def integralList(self):

        url = self.prefix + '/Integral/List'
        data = {
            "uid": self.uid,
            "page": 1,
            "type": 0,
            "openId": self.openId
        }
        res = requests.post(url, json=data)
        print(res.text.encode('utf-8').decode('unicode_escape'))

    def addIntegral(self):
        """
        :type
        :return:
        """
        url = 'https://betawx.yunchehome.com/Integral/Set'
        data = {
            "fromId": self.uid,
            "toId": "121",
            "type": 2,
            "openId": self.openId
        }
        res = requests.post(url, json=data)
        print(res.text.encode('utf-8').decode('unicode_escape'))

    def attention(self, toId):
        url = PREFIX_BETA + '/main/attention'
        data = {
            "fromId": self.uid,
            "toId": toId,
            "type": 2,
            "openId": self.openId
        }
        res = requests.post(url, json=data)
        print(res.text.encode('utf-8').decode('unicode_escape'))

    def cardList(self, page):
        url = self.prefix + '/main/userList'
        data = {
            "openId": self.openId,
            "search": "",
            "type": 0,
            "order": 0,
            "page": page
        }

        res = requests.post(url, json=data)
        if res.status_code == 200:
            print(res.text.encode('utf-8').decode('unicode_escape'))
            resJson = json.loads(res.text)
            print(resJson['retData']['list'])
            for uid in resJson['retData']['list']:
                print(uid)


if __name__ == '__main__':
    c = Card()
    c.cardList(1)
