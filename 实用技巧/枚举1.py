## 定义类型的方式

# 1
yellow = 1
green = 2

# 2
color = {'yello': 1, 'green': 2}


# 3

class Color():
    yellow = 1
    green = 2


## 使用枚举

# 优势1：定义的变量不可任意更
# 优势2：不可重复定义变量

from enum import Enum


class ColorEnum(Enum):
    YELLOW = 1
    GREEN = 2
    # YELLOW = 3 # TypeError: Attempted to reuse key: 'YELLOW' ，不可重复定义变量


# ColorEnum.YELLOW = 3  # AttributeError: Cannot reassign members.

print(ColorEnum.YELLOW, type(ColorEnum.YELLOW))  # 枚举类型 <enum 'ColorEnum'>
print(ColorEnum.YELLOW.name, type(ColorEnum.YELLOW.name))  # 枚举的名字 YELLOW
print(ColorEnum.YELLOW.value, type(ColorEnum.YELLOW.value))  # 枚举的值 1
