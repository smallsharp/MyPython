# 比较两个字典的值
a = {"name": "likai", "age": 22, "height": 180}
b = {"height": 177, "sex": "male", "age": 22, "name": "zhangkai"}

if __name__ == '__main__':

    # for m, n in zip(a, b):
    #     if m == n:
    #         if a[m] != b[m]:
    #             print("except {}:{},but get:{}".format(m, a[m], b[m]))
    #             # break

    for k in a.keys() & b.keys():
        if a[k] != b[k]:
            print("except {}:{},but get:{}".format(k, a[k], b[k]))
        # print("key:{},value1:{},value2:{}".format(k,a[k],b[k]))
