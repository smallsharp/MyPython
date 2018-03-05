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

res = os.popen("adb shell getprop ro.product.model")
print(res.read())