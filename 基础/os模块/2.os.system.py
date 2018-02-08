# coding=utf-8
import os
import subprocess

cmd = "adb devices"

res = os.system(cmd)
print("res:", res)

print("-" * 50)

# subprocess.call用于代替os.system
res2 = subprocess.call(cmd, shell=True)
print("res2:", res2)

print("-" * 50)

# 执行结果保存在文件
dst = open("devices.txt", "w")
pipe = subprocess.Popen(cmd, shell=True, stdout=dst)
print(pipe.stdout)
dst.close()
print("-" * 50)

pipe = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
print
pipe.read()
