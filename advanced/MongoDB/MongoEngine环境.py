## 安装 pip install mongoEngine
from mongoengine import connect, Document, EmbeddedDocument, StringField, IntField, FloatField, ListField, \
    EmbeddedDocumentField

## 连接库
connect(db='test', host='192.168.40.32')

SEX_CHOICES = (
    ('male', '男'),
    ('female', '女')
)

# 连接表
connect('students')


# 成绩
class Grade(EmbeddedDocument):
    name = StringField(required=True)
    score = FloatField(required=True)


# 学生
class Student(Document):
    name = StringField(max_length=32, required=True)
    age = IntField(required=True)
    grade = FloatField()
    address = StringField()
    sex = StringField(choices=SEX_CHOICES, required=True)
    grades = ListField(EmbeddedDocumentField(Grade))

    # 设置集合名称，以及排序方式
    meta = {
        'collection': 'students',
        'ordering': ['-age']
    }


class ME(object):
    # 增加一条数据
    def add_one(self):
        yuwen = Grade(
            name='语文',
            score=90
        )
        shuxue = Grade(
            name='数学',
            score=100
        )
        stu_obj = Student(
            name='张三',
            age=16,
            sex='male',
            grades=[yuwen, shuxue]
        )
        stu_obj.save()
        return stu_obj

    # 查询一条数据
    def get_one(self):
        return Student.objects.first()

    # 查询多条数据
    def get_more(self):
        return Student.objects.all()

    # 根据ID获取数据
    def get_from_oid(self, oid):
        return Student.objects.filter(pk=oid)

    # 修改数据
    def update(self):
        # return Student.objects.filter(sex='male', age__ge=16).update(inc__age=10)
        # 修改一条数据
        return Student.objects.filter(sex='male').update_one(inc__age=100)

    # 删除数据
    def delete(self):
        # 删除一条数据
        # return Student.objects.filter(sex='male').first().delete()
        # 删除多条数据
        return Student.objects.filter(sex='female').delete()


if __name__ == '__main__':
    me = ME()

    # print(me.add_one())
    print(me.get_one())
    for i in me.get_more():
        print(i['name'])
