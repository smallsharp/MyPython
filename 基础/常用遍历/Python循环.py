
# for 常用遍历

num = [1,2,3,4,5]
for n in num: # 遍历list
    print(n)
print("-"*50)

for m in range(len(num)):
    print(m*4)
print("-"*50)

for n in range(0,9,1): #start 不写默认为0；stop 结束的数值，必须填写； step 步长，不写默认为1，尽量写完整
    print(n)
print("-"*50)

for n in range(0,9): # 省略步长
    print(n)
print("-"*50)

for n in range(1,9): # start=1
    print(n)
print("-"*50)

for n in  range(0,9,2): # 步长=2，每个元素等于start  + i*step
    print(n)
print("-"*50)

for n in range(3,100,3):
    print(n,end=" ")