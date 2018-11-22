# coding=utf-8


# 问题
a = 4.2
b = 2.1
print(a + b == 6.3)  # False
a + b  # 6.300000000000001

# 实现精确的计算
from decimal import Decimal

a = Decimal('4.2')
b = Decimal('2.1')
print(a + b == Decimal('6.3'))  # True

import math

print(math.isnan(float('inf')))
