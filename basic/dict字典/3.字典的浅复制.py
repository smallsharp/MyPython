# coding=utf-8

print("")
"""
copy()
"""

student1 = {'小智': '1002', "info": ["man", "20", "177"]}
student2 = student1.copy()

# 注意1：替换副本中的值时，原始字典不受影响
student2["小智"] = 1005
print(student1) # {'小智': '1002', 'info': ['man', '20', '177']}
print(student2) # {'小智': 1005, 'info': ['man', '20', '177']}


# 注意2：如果修改了某个值（原地修改，不是替换），原始字典就会收到影响，因为同样的值也在原字典中
student2["info"].remove("man")
print(student1) # {'小智': '1002', 'info': ['20', '177']}
print(student2) # {'小智': 1005, 'info': ['20', '177']}

# del student2["小智"]
# print(student1)
# print(student2)
