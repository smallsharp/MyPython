'''
Created on 2017年9月5日
    Python3 中可以使用 json 模块来对 JSON 数据进行编解码，它包含了两个函数：
    json.dumps(): 对数据进行编码。
    json.loads(): 对数据进行解码。
@author: cm
'''
import json
 
data = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'http://www.runoob.com'
}

print("读取字符串:")

# 第一步：对给定数据dict，进行编码,序列化为json格式
jsonStr = json.dumps(data); 
print(jsonStr)

# 第二步：对编码后的json数据，进行解码
jsonData = json.loads(jsonStr) 
print ("jsonData['name']: ", jsonData['name'])
print ("jsonData['url']: ", jsonData['url'])


js = {'appJson': {'nodeName': 'S090QM001', 'backgroundColor': '', 'outLineMaskUrl': 'stag/model/upload/Tee001_3D/Temp/S090QM001.png', 'thumbilUrl': 'diyrelease/user/h5_3d_1503484843668.png', 'texts': [{'text': 'ATTITUDE', 'defaultText': '我是默认的文本', 'fontName': 'NotoSansHans-Black', 'textColor': '#ffffff', 'fontSize': 111.09813974586993, 'dy': 0, 'isLocked': 1, 'matrix': {'translateX': 39.24500751293988, 'translateY': 313.4146201299649, 'scale': 0.7879915688587728, 'rotate': 0}, 'matrixString': 'matrix(0.7879915688587728,0,0,0.7879915688587728,39.24500751293988,313.4146201299649)'}], 'materials': [{'orig_width': 394, 'orig_height': 150, 'remoteImageUrl': 'diyrelease/Python/o_1bo7aqhlno4o15hnrc3usc7de3a.png', 'remoteOriginalImageUrl': 'diyrelease/Python/o_1bo7aqhlno4o15hnrc3usc7de3a.png', 'matrix': {'translateX': 15.577348637297405, 'translateY': 164.468533745164, 'scale': 1.22041955006448, 'rotate': 0}, 'matrixString': 'matrix(1.22041955006448,0,0,1.22041955006448,15.577348637297405,164.468533745164)', 'isLocked': 1}], 'userImage': {'orig_width': 564, 'orig_height': 564, 'remoteImageUrl': 'diyrelease/Python/o_1bo7aq869s44cmfou7t07pv7g.jpg', 'remoteOriginalImageUrl': 'diyrelease/Python/o_1bo7aq869s44cmfou7t07pv7g.jpg', 'matrix': {'rotate': 0, 'scale': 0.9078014184397163, 'translateX': 0, 'translateY': 0}, 'matrixString': 'matrix(0.9078014184397163,0,0,0.9078014184397163,0,0)'}}}
jsonS = json.loads(json.dumps(js))
print(jsonS['appJson']['outLineMaskUrl'])


