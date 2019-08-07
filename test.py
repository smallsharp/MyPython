body = {
    "requestTime": "",
    "interfaceType": "",
    "sign":"",
    "methodName":"",
    "version":"",
    "param":""
}

import json

str = json.dumps(body)

print(type(str))
print(str.__len__())
