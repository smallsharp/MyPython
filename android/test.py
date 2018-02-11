#coding=utf-8



res = ['List of devices attached\n', 'LE67A06310143950\tdevice\n', '\n']


for i in res:
    # print("a:",i)
    if "attached" not in i and len(i)>1:
        print("===",i,len(i))
        print(i.split()[0])

    # if len(i)>0 and i.rfind("device")==0:
    #     print(i)

# d = [i.split()[0] for i in res if 'devices' not in i and len(i) > 5]


# print(d)