import pickle

lines = [
    "I'm like a dog chasing cars.",
    "I wouldn't know what to do if I caught one...",
    "I'd just do things."
]

"""
ע��:���л���ʱ���ʹ��bģʽ
"""

with open(file="lines.pkl",mode="wb") as f:
    pickle.dump(obj=lines,file=f) # ���л���������ļ�

with open("lines.pkl","rb") as f: # ���ļ���ȡ�������л�
    lines_back = pickle.load(f)

print(lines_back) # ��linesһ��