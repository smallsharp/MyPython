import requests




url = 'https://betawx.yunchehome.com/demand/UserDemand'

openId = "o94HS5PrLEd6AeyLRM5XimFX90tU"

data = {
	"page": 1,
	"lon": 121.258545,
	"lat": 31.202341,
	"openId": openId
}


res = requests.post(url,json=data)
print(res.text)