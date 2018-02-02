import pickle

lines = [
    "I'm like a dog chasing cars.",
    "I wouldn't know what to do if I caught one...",
    "I'd just do things."
]

"""
注意:序列化的时候得使用b模式
"""

with open(file="lines.pkl",mode="wb") as f:
    pickle.dump(obj=lines,file=f) # 序列化并保存成文件

with open("lines.pkl","rb") as f: # 从文件读取并反序列化
    lines_back = pickle.load(f)

print(lines_back) # 和lines一样