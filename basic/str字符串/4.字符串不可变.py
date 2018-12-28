"""
字符串本身一旦声明，不可改变
"""
name = "likai"
name[0:2] = "zhang"  # TypeError: 'str' object does not support item assignment
