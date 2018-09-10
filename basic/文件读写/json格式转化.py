'''
Created on 2017年9月5日
    Python3 中可以使用 json 模块来对 JSON 数据进行编解码，它包含了两个函数：
    json.dumps(): 对数据进行编码。
    json.loads(): 对数据进行解码。
@author: cm
'''
import json

# 原始格式

data = {
    'retCode': 200,
    'retMsg': 'success',
    'retData': ''
}

print(type(data))  # dict
print("data['retCode']: ", data['retCode'])
print("data['retMsg']: ", data['retMsg'])

# --------------------------------------------------------------------------------------#


# dumps：Serialize `obj` to a JSON formatted `str`
jsonStr = json.dumps(data);
print(type(jsonStr))  # str

# ---------------------------------------------------------------------------------------#


# Deserialize ``s`` (a ``str``, ``bytes`` or ``bytearray`` instance containing a JSON document) to a Python object
jsonData = json.loads(jsonStr)
print(type(jsonData))  # dict
print("jsonData['retCode']: ", jsonData['retCode'])
print("jsonData['retMsg']: ", jsonData['retMsg'])

# json格式的字符串，如下


a = """
    {
        "retCode":"10001",
        "retMsg":"fail"
    }
"""

b = json.loads(a) # 反序列化为python dict 对象

print(b['retCode'])
print(b.get('retMsg'))
