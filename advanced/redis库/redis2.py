import redis


class RedisList(object):

    def __init__(self):
        self.r = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)

    def push(self):
        t = ('Amy', 'Lili', 'John')
        res = self.r.lpush('line_shopping', *t)
        print(res)
        line = self.r.lrange('line_shopping', 0, -1)
        print(line)
        return res


class RedisSet(object):

    def __init__(self):
        self.r = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)

    def sadd(self):
        l1 = ['Cat', 'Dog']
        res = self.r.sadd('zoo', *l1)

        l2 = ['Cat', 'Tiger', 'Snake']
        res = self.r.sadd('zoo2', *l2)

        row = self.r.smembers('zoo')
        print(row)

    def srem(self):
        # 移除某个元素
        res = self.r.srem('zoo', 'Dog')
        return res

    def sinter(self):
        # 求交集
        res = self.r.sinter('zoo', 'zoo2')
        return res

    def sunion(self):
        res = self.r.sunion('zoo','zoo2')
        return res


if __name__ == '__main__':
    # r = RedisList()
    # r.push()

    r = RedisSet()
    r.sadd()
    r.srem()
    print(r.sinter())
    print(r.sunion())
