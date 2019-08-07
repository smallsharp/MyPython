#!/usr/bin/env python3
# -*- coding:utf-8 -*-


# 使用方法：在命令行执行
# 1.python 对比文件具体内容差异.py "test.json" "test.txt" >dif.html
# 2.在当前目录生成dif.html
 
import difflib
import sys
 
try:
    textfile1 = sys.argv[1]
    textfile2 = sys.argv[2]
except Exception as e:
    print("Error:" + str(e))
    print("Usage: xxxx.py filename1 filename2")
    sys.exit()
def readfile(filename):
    try:
        fileHandle = open(filename,'r')
        text = fileHandle.read().splitlines()
        fileHandle.close()
        return text
    except IOError as error:
        print('Read file Error:' + str(error))
        sys.exit()
 
if textfile1 == "" or textfile2 == "":
    print("Usage:test.py filename1 filename2")
    sys.exit()
 
text1_lines = readfile(textfile1)
text2_lines = readfile(textfile2)
 
d = difflib.HtmlDiff()
print(d.make_file(text1_lines,text2_lines))