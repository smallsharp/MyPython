'''
Created on 2017年9月26日

@author: cm
'''
import os

# 模块os中的walk()函数可以遍历文件夹下所有的文件
def file_name(file_dir):
    for root,dirs,files in os.walk(file_dir):
#         print(root) #当前目录路径
#         print(dirs) #当前路径下的所有子目录
        print(files) #当前路径下所有非目录子文件        

# 遍历指定目录，显示目录下的所有文件名
def eachFile(filepath):
    pathDir =  os.listdir(filepath)
    for p in pathDir:
        child = os.path.join('%s/%s' % (filepath, p))
        print(child)

# 读取文件内容并打印
def readFile(filename):
    fname = open(filename, 'r') # r 代表read
    for eachLine in fname:
        print (eachLine)
    fname.close()
    
# 输入多行文字，写入指定文件并保存到指定文件夹
def writeFile(filename):
    fopen = open(filename, 'w')
    print ("\r请任意输入多行文字"," ( 输入 .号回车保存)")
    while True:
        aLine = input()
        if aLine != ".":
            fopen.write('%s%s' % (aLine, os.linesep))
        else:
            print ("文件已保存!")
            break
    fopen.close()

if __name__ == '__main__':
    dir1 = "C:/Users/cm/Downloads/Tee001_3D"
    eachFile(dir1)
    readFile("C:/Users/cm/Downloads/Tee001_3D/Tee001_3D.mtl")