# coding=utf-8

import subprocess

command1 = "adb devices"
command2 = r"D:\nodejs\new_modules\appium.cmd"

# res = subprocess.call("adb devices",timeout=5) # 控制台自动打印程序结果
# print("res:",res) # 只返回运行的状态码 0

# res = subprocess.check_call("adb devices")
# print("res:",res)

# res = subprocess.check_output(command1, shell=True)
# print(res.decode())
# print(type(res))

# res = subprocess.check_output(command2, shell=True)
# print(res.decode())
# print(type(res))

# res = subprocess.Popen(command2,shell=True,stdout=subprocess.PIPE).stdout.readlines()
# print(res,type(res))

import os
res = os.popen(command2)
# res = os.system(command2)
print(type(res),type(res.read()))
print(res.read())
