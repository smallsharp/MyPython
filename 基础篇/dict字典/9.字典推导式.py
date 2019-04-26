prices = {
    'nokia': 2000,
    'meizu': 1800,
    'huawei': 1200,
    'xiaomi': 1600,
    'oppo': 300
}

newdict = {k: v for k, v in prices.items() if v > 1500}
print(newdict)  # {'nokia': 2000, 'meizu': 1800, 'xiaomi': 1600}

brands = {
    'nokia', 'meizu', 'xiaomi'
}

newdict2 = {k: v for k, v in prices.items() if k in brands}
print(newdict2)  # {'nokia': 2000, 'meizu': 1800, 'xiaomi': 1600}
