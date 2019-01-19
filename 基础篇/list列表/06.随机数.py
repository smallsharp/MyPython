import random
items = [8, 23, 45, 12, 78]

while items:
    ran = random.choice(items)
    print("ran:",ran)
    if items:
        items.remove(ran)
    print(items)