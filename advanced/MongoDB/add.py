from pymongo import MongoClient


class MC():

    def __init__(self, dbName: str):
        self.client = MongoClient('192.168.40.32', 27017)
        self.db = self.client[dbName]

    def connTable(self, table):
        '''
        连接库中的表
        :param table:
        :return:
        '''
        self.table = self.db[table]
        return self.table

    def add(self, data: dict):
        row = self.table.insert_one(data)
        return row.inserted_id

    def find_one_by_oid(self, oid):
        '''
        通过_id,查询数据
        :param oid:
        :return:
        '''
        from bson.objectid import ObjectId
        obj = ObjectId(oid)
        row = self.table.find_one({'_id': obj})
        return row

    def update(self):
        # 修改一条
        # res = self.table.update_one({'name': 'zhangfei'}, {'$inc': {'age': 5}})
        # print('匹配数:{},修改成功数：{}'.format(res.matched_count, res.modified_count))

        # 修改多条
        res = self.table.update_many({}, {'$inc': {'age': 5}})
        print('匹配数:{},修改成功数：{}'.format(res.matched_count, res.modified_count))

    def delete(self):
        # 删除一条数据
        res = self.table.delete_one({'name': 'zhangfei', 'age': 44})
        print('删除成功次数：{}'.format(res.deleted_count))  # 删除成功返回1


def main():
    mc = MC('test')
    uc = mc.connTable('user')
    user = {
        'name': 'zhangfei',
        'age': 33,
        'sex': 'female'
    }
    #
    # # 添加数据
    # uc.insert_one(user)
    #
    # # 查询
    # rows = uc.find({'name': 'zhangfei'})
    # print(list(rows))

    # # 通过_id 查询数据
    # oid = '5c25d7c63d26f01d4ca5457e'
    # row = mc.find_one_by_oid(oid)
    # print(row)

    # 修改
    # mc.update()

    # 删除
    mc.delete()

    # user = {
    #     'name': 'xiaoqiao',
    #     'age': 16,
    #     'sex': 'female'
    # }
    #
    # r = mc.add(user)
    # print(r)


if __name__ == '__main__':
    main()
