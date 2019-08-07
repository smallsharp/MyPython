'''
Created on 2017年9月13日

在Python中，推荐用上下文管理器（with-as）来打开文件，IO资源的管理更加安全

@author: cm
'''

# f = open('name_age.txt')
# content = f.read()  # 文件的内容一次性读完，大文件有风险
# print(content)
# f.close()
#
# fw = open('hello.txt', 'w')
# fw.write('Hello World')
# fw.close()


def readFile(file):
    with open(file, "r") as f:
        """
        open()的第一个参数是文件名，第二个参数是模式
        文件的模式一般有四种，读取(r)，写入(w)，追加(a)和读写(r+)
        如果希望按照二进制数据读取，则将文件模式和b一起使用（wb, r+new…）
        """
        lines = f.readlines()
        for line in lines:
            name, age = line.rstrip().split(",")
            print("{} is {} years old.".format(name, age))


"""
读写结合
要读取文件内容，并把年龄和名字的顺序交换
存成新文件age_name.txt，这时可以同时打开两个文件
"""


def read_write(oldfile, newfile):
    with open(file=oldfile, mode="r") as file_read, open(file=newfile, mode="w") as file_write:
        line = file_read.readline()
        while line:
            name, age = line.rstrip().split(",")
            file_write.write("{},{}\n".format(age, name))  # 写的核心代码
            line = file_read.readline()
    return newfile


# with open("name_age.txt", "r") as f:
#     lines = f.readlines()
#     for line in lines:
#         name, age = line.rstrip().split(",")
#         print("{} is {} years old.".format(name, age))

read_write("age_name.txt","name_age.txt")
