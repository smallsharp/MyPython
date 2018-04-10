# 1.普通写法

# with open("abc.jpg","rb")as fromFile:
#     with open("abc2.jpg","wb") as toFile:
#         filecontent = fromFile.read()
#         toFile.write(filecontent)

# 2.优雅的写法

with open("abc.jpg", "rb") as fromFile, open("abc2.jpg", "wb") as toFile:
    filecontent = fromFile.read()
    toFile.write(filecontent)
