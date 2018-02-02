'''
Created on 2017年9月13日

在Python中，推荐用上下文管理器（with-as）来打开文件，IO资源的管理更加安全

@author: cm
'''

"""
open()的第一个参数是文件名，第二个参数是模式
文件的模式一般有四种，读取(r)，写入(w)，追加(a)和读写(r+)
如果希望按照二进制数据读取，则将文件模式和b一起使用（wb, r+new…）
"""
def readFile(file):
    with open(file, "r") as f:
        lines = f.readlines()
        for line in lines:
            name,age = line.rstrip().split(",")
            print("{} is {} years old.".format(name,age))


"""
读写结合
要读取文件内容，并把年龄和名字的顺序交换
存成新文件age_name.txt，这时可以同时打开两个文件
"""
def read_write(oldfile,newfile):
    with open(file=oldfile,mode="r") as fread,open(file=newfile,mode="w") as fwrite:
        line = fread.readline()
        while line:
            name,age = line.rstrip().split(",")
            fwrite.write("{},{}\n".format(age,name)) # 写的核心代码
            line = fread.readline()
    return newfile



if __name__ == '__main__':
    file = './name_age.txt'

    newfile = "age_name.txt"
    # readFile(file=file)
    new = read_write(file,newfile)
    # readFile(new)
    with open(new,"r") as f:
        lines = f.readlines()
        print(lines)