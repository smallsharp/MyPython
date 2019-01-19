# coding=utf-8

print("使用formate格式化的三种常见用法")

"""
例1.按顺序格式化字符串
"""
a = 'I’m like a {} chasing {}'.format("dog", "cars")
print(a)

"""
例2.在大括号中指定参数所在位置
"""
b = 'I prefer {1} {0} to {2} {0}'.format('food', 'Chinese', 'American')
print(b)

"""
例3.指定关键字名称
"""
package = "com.tude.android"
cmd = ('pm clear {package}'.format(package=package))
print(cmd)  # pm clear com.tude.android




# >代表右对齐，>前面 是要填充的字符
for i in [1, 19, 256]:
    print('The index is {:0>6d}'.format(i))  # 000001,000019, 000256

# <代表左对齐，依次输出：
# *---------
# ****------
# *******---
for x in ['*', '****', '*******']:
    progress_bar = '{:-<10}'.format(x)
    print(progress_bar)

for x in [0.0001, 1e17, 3e-18]:
    print('{:.6f}'.format(x))  # 按照小数点后6位的浮点数格式
    print('{:.1e}'.format(x))  # 按照小数点后1位的科学记数法格式
    print('{:g}'.format(x))  # 系统自动选择最合适的格式
