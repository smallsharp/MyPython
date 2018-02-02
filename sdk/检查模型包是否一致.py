#coding=utf-8
'''
根据提供的两个路径，遍历路径下的文件是否一致
@author: cm
'''
import os
import filecmp

dir1 = "C:/Users/cm/Downloads/test1"
dir2 = "C:/Users/cm/Downloads/test2"


# 遍历指定目录下所有文件
def eachFile(filepath):
    # 遍历指定目录下的所有文件名称，如：['Tee001_3D.zip', 'Tee001_3D_bak.zip', 'Tee007_3D.zip']
    pathDir =  os.listdir(filepath)
    file_list = []
    for filename in pathDir:
        # 拼接成完成的路径，如：C:/Users/cm/Downloads/test2/Tee007_3D.zip
        path = os.path.join('%s/%s' % (filepath, filename))
        file_list.append(path)
    return file_list

list1 = eachFile(dir1)
list2 = eachFile(dir2)

for p1 in list1:
    for p2 in list2:
        if(list1.index(p1)==list2.index(p2)):
            print(p1,p2)
            print(filecmp.cmp(p1, p2, shallow=True)) # 文件对比
        else:
            continue

print(os.listdir(dir1))