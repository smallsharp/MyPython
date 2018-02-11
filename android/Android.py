'''
Created on 2017年9月27日

@author: cm
'''

import os
import random
import time
# from mobileDetecting import get_serialno

# deviceName = get_serialno()
deviceName = "06694a9b006097fb"
packageName = "com.taidu.andorid.example3d"

#统计pss值（实际使用的物理内存（比例分配共享库占用的内存）
def meminfo(deviceName,apk_package_name):
    try:
#         mem = os.popen(
#             "adb -s {0} shell dumpsys mem {1} | findstr TOTAL".format(deviceName,apk_package_name)
#             ).read()
        mem = os.popen(
            "adb -s %s shell dumpsys mem %s | findstr TOTAL"%(deviceName,apk_package_name)
            ).read()
        print(mem)
        pss = mem.split()[1]
        pss_int = int(pss)
        print(round(pss_int/1024,2))
    except IndexError:
        pss = ""
    return pss


#获取内存pss值，并写入到文件
with open("mem.txt",'w+') as m:  
    for i in range(100): 
        pss_value = meminfo(deviceName,packageName)
        time.sleep(2)
        m.write(pss_value +"\n")