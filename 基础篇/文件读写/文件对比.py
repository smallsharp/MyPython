'''
Created on 2017年9月26日

@author: cm
'''
#coding=utf-8
import filecmp

# cmp 只对比文件内容是否相同
r1 = filecmp.cmp("C:/Users/cm/Downloads/Tee001_3D/Tee001_3D.obj","C:/Users/cm/Desktop/Tee001_3D/Tee001.obj",shallow=True)
print("不同目录下，不同文件名称，内容相同的文件,结果：",r1)

r2 = filecmp.cmp("C:/Users/cm/Downloads/Tee001_3D.zip","C:/Users/cm/Downloads/Tee001_3D_bak.zip",shallow=True)
print("同目录下，不同文件名称，内容相同的文件，结果：",r2)

dir1 = "C:/Users/cm/Downloads/Tee001_3D"
dir2 = "C:/Users/cm/Downloads/Tee001_3D_bak"

# 参数dir1是目录1，参数dir2是目录2，参数common是比较的 文件 列表,返回三个文件名列表：相同列表、不相同列表、错误列表
r3 = filecmp.cmpfiles(dir1, dir2,['Tee001_3D.DAE','Tee001_3D.obj'],shallow=True)
print("对比两个目录中，文件列表，结果：",r3)

filecmp.clear_cache()
