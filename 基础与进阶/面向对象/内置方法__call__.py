class PenFactory:

    def __init__(self, p_type):
        self.p_type = p_type

    # 　覆写作用：类的实例对象可以被调用
    def __call__(self, p_color):
        print("这是一个:{},颜色是:{}".format(self.p_type, p_color))


gangbiFac = PenFactory("钢笔")
gangbiFac("红色")
gangbiFac("蓝色")
gangbiFac("黑色")

print("-" * 50)

fenbiFac = PenFactory("粉笔")
fenbiFac("红色")
fenbiFac("黄色")
fenbiFac("紫色")
