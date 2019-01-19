import redis

# 连接
# r = redis.StrictRedis(host='192.168.40.32',port=6379,db=0)
r = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)


# print(r.get('上海雷凌信息科技有限公司'))


class RedisString(object):

    def __init__(self):
        self.r = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)

    def set(self):
        res = self.r.set('name', 'lili')
        return res

    def get(self):
        return self.r.get('name')

    def mset(self):
        d = {
            'name': 'mimi',
            'age': 22,
            'sex': 'female'
        }
        return self.r.mset(d)

    def mget(self):
        # 设置多个值
        l = ['name', 'age', 'sex']
        return self.r.mget(l)

    def dele(self):
        res = self.r.delete('age')  # 删除age
        return res


if __name__ == '__main__':
    r = RedisString()
    print(r.set())
    print(r.get())
    print(r.mset())
    print(r.mget())

    print(r.dele())
    print(r.mget())
