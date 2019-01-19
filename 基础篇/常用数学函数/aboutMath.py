# -*- coding:utf-8 -*-
import math

# 返回数字的绝对值，如abs(-10)返回10
print(abs(-10))

# 返回数字向上取整的结果
print(math.ceil(1.3))


# 比较两个数
import operator
print(operator.eq(1, 1))
print(operator.ne(1, 1))
print(operator.ge(1, 1))
print(operator.gt(1, 1))
print(operator.le(1, 1))
print(operator.lt(1, 1))

# 返回e的x次幂
print(math.exp(2))
# 浮点数的形式返回绝对值
print(math.fabs(-10.5))
# 返回向下取整的结果
print(math.floor(3.3))
# 返回以e为底的对数结果
print(math.log(math.e))
# 返回以10为底的对数结果
print(math.log10(10))
# 返回以2为底的对数结果
print(math.log2(2))


# 最大值
print(max(1, 2, 3, 4, 5))
# 最小值
print(min(1, 2, 3, 4, 5))


# 返回模除以后的商和余数
print(divmod(5, 2))
# 返回一个浮点数的小数部分和整数部分
print("modf", math.modf(2.33))
# 返回模运算后的余数部分
print("fmod", math.fmod(5, 2))
# 求x的y次方，同x**y
print(pow(2, 3))
# 四舍五入，后面指定位数
print(round(3.222, 2))
# 求平方根
print(math.sqrt(16))

"""三角函数"""
# 反余弦
print(math.acos(0.5))
# 反正弦
print(math.asin(0.5))
"""
atan2(y, x)是4象限反正切，它的取值不仅取决于正切值y/x，还取决于点 (x, y) 落入哪个象限：
当点(x, y) 落入第一象限时，atan2(y, x)的范围是 0 ~ pi/2;
当点(x, y) 落入第二象限时，atan2(y, x)的范围是 pi/2 ~ pi;
当点(x, y) 落入第三象限时，atan2(y, x)的范围是 －pi～－pi/2;
当点(x, y) 落入第四象限时，atan2(y, x)的范围是 -pi/2～0.
而 atan(y/x) 仅仅根据正切值为y/x求出对应的角度 （可以看作仅仅是2象限反正切）：
当 y/x > 0 时，atan(y/x)取值范围是 0 ~ pi/2；
当 y/x < 0 时，atan(y/x)取值范围是 -pi/2～0.
"""
# 反正切
print(math.atan(0.5))
# 四象限反正切
print(math.atan2(0.5, 0.5))
print(math.sin(math.pi / 2))
print(math.cos(math.pi / 2))
print(math.tan(math.pi / 2))
# 返回欧几里得范数，也就是x*x+y*y的值
print(math.hypot(2, 3))
# 弧度转角度
print(math.degrees(math.pi / 2))
# 角度转弧度
print(math.radians(90))