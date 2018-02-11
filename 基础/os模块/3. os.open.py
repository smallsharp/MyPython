#coding=utf-8
import os

# 使用os.popen(cmd)获取返回结果
res = os.popen("adb devices")
print(res.read()) # List of devices attached


# 使用os.popen(cmd)获取返回结果
res = os.popen("adb shell monkey 100")
print(res.read())



