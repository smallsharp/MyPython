#coding=utf-8


import os



"""
ro.build.version.sdk=22
ro.build.version.release=5.1
ro.product.device=mx5
ro.product.model=MX5 
ro.product.name=meizu_mx5
ro.serialno
ro.sf.lcd_density
"""

cmd1 = "adb shell getprop ro.product.model"
cmd2 = "adb shell getprop ro.product.name"


model = os.popen(cmd1)
# print(res.read())

name =os.popen(cmd2)
print(name.read())

