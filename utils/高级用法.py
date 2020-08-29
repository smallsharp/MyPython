from collections import defaultdict

d = defaultdict(list)

d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

print(d)

for k, v in d.items():
    print(k, v)



items = [i for i in range(0,7)]
print(items)

a = slice(2,4)
print(items[2:4])

items[a] = [10,11]
print(items)

del items[a]
print(items)

print(a.start)
print(a.stop)
print(a.step)