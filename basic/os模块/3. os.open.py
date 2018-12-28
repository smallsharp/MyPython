#coding=utf-8
import os
import subprocess

# 使用os.popen(cmd)获取返回结果
res = os.popen("adb devices")
# print(res.read()) # List of devices attached


# 使用os.popen(cmd)获取返回结果
# res = os.popen("adb shell monkey 100")
# print(res.read())


"""
例1.使用文件 接收 输出结果
"""
cmd = "adb shell dumpsys meminfo com.tude.android"
fhandle = open(r"meminfo.txt", "w")
pipe = subprocess.Popen(cmd, shell=True, stdout=fhandle).stdout
fhandle.close()


"""
例2.使用管道输出执行结果
"""
pipe1 = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE).stdout.readlines()
# s = bytes.decode(pipe.read(),encoding="gbk")
# print(pipe1)

