import time

# 第一步：获取当前时间元组
turple_time = time.localtime()

# 第二步：将时间元组 转化为 格式化日期
date_str = time.strftime('%Y-%m-%d', turple_time)
print(date_str)

# 【关键】第三步：将格式化日期 转化为 时间元组
tuple_time2 = time.strptime(date_str, '%Y-%m-%d')

# 【关键】第四步：将时间元组 转化为 时间戳
tt = time.mktime(tuple_time2)
print(tt)

## --------------------------------基础知识----------------------------------------------------------##

# strftime(format[, tuple]) -> string,接受时间元组，返回指定格式：2018-02-17 16:55:17
date_str = time.strftime("%Y-%m-%d %H:%M:%S", turple_time)
print(date_str, type(date_str))

# strptime(string, format) -> struct_time
turple_time2 = time.strptime(date_str, "%Y-%m-%d %H:%M:%S")

# mktime(tuple)  时间元组--》 时间戳
tt = time.mktime(turple_time2)
print('tt:', tt)



tt = time.localtime(1545667200)
print(tt)