import pymongo
# # 获得数据库对象
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# # 创建/选择数据库
# mydb = myclient["163spider"]
# # 获取当前所有数据库名字
# dblist = myclient.list_database_names()
# print(dblist)
# # 创建集合
# mycol = mydb["test1"]
# # 获取当前所有集合名字
# collist = mydb.list_collection_names()
# print(collist)
#
# # 增
# # data_dict = {"ID": "435278010", "name": "world.execute (me) ;", "tags": "soft"}
# # x = mycol.insert_one(data_dict)  # 插入一个数据
# # print(x.inserted_id)  # 返回插入结果对象，有inserted_id属性，为 _id 的值
# # data_list = [
# #     {"ID": "435278010", "name": "world.execute (me) 0;", "tags": "soft"},
# #     {"ID": "435278011", "name": "world.execute (me) 1;", "tags": "soft"},
# #     {"ID": "435278012", "name": "world.execute (me) 2;", "tags": "soft"},
# #     {"ID": "435278013", "name": "world.execute (me) 3;", "tags": "soft"},
# #     {"ID": "435278014", "name": "world.execute (me) 4;", "tags": "soft"},
# # ]
# # x = mycol.insert_many(data_list)  # 插入多个数据
# # print(x.inserted_ids)  # 返回插入结果对象，有inserted_ids，为结果列表
#
# # 查询
# x = mycol.find_one()  # 查询第一条数据
# print(x)
# for x in mycol.find():  # 查询所有数据
#     print(x)
# # 查询指定字段的数据，要返回的设置为1，不返回的设置为0
# # 只设置一个字段为1，则其他为0，反之亦然
# # 除了_id 不能同时写1和0
# for x in mycol.find({}, {"ID": 0}):
#     print(x)
# # 过滤数据
# for x in mycol.find({"name": "world.execute (me) 1;"}, {"tags": 0}):
#     print(x)


class MongoDB:
    def __init__(self, url=r'mongodb://localhost:27017/', database_name='music_tag_spider'):
        self.url = url
        self.db_name = database_name
        self.client = pymongo.MongoClient(url)
        self.database = self.client[database_name]
        self.musics = self.database['musics']
        self.need_recreate_index = True

    def insert_one_music(self, name, tags, ssid, extra_info=None):
        """
        :param name: string 音乐的名字/标题
        :param tags: list 音乐标签
        :param ssid: string 音乐的来源的id（special source id）
        :param extra_info: 额外信息
        :return: 插入成功与否的信息
        """
        if extra_info is None:
            extra_info = {}
        data_dict = {}
        data_dict['name'] = name
        data_dict['tags'] = tags
        data_dict['ssid'] = ssid
        data_dict['extra_info'] = extra_info
        rslt = self.musics.insert_one(data_dict)
        self.need_recreate_index = True
        return rslt.inserted_id

    def create_index(self):
        # 建立索引
        self.musics.create_index([('tags', 1)])
        self.need_recreate_index = False

    def empty_musics(self):
        """
        危险操作 清空数据
        :return: Bool 是否清空成功
        """
        return self.musics.drop()

    def find_music_with_tags(self, tags, return_extra=False):
        """
        通过标签查找音乐
        :param tags: list[string,]
        :return: [name, tags, ssid, extra_info]
        """
        if self.need_recreate_index:
            self.create_index()
        rslt_musics = self.musics.find({"tags": i for i in tags})
        return_list = []
        for i in rslt_musics:
            tmp = dict()
            tmp['name'] = i['name']
            tmp['tags'] = i['tags']
            tmp['ssid'] = i['ssid']
            if return_extra:
                tmp['extra_info'] = i['extra_info']
            return_list.append(tmp)
        return return_list


if __name__ == '__main__':
    db = MongoDB()
    db.empty_musics()
    db.insert_one_music('种太阳', ['儿歌', '欢快'], '1298733696')
    db.insert_one_music('RAPSTAR', ['说唱'], '1469628663')
    db.insert_one_music('蜗牛与黄鹂鸟', ['儿歌', '宝宝'], '566436178')
    db.insert_one_music('风的小径', ['轻音乐', '舒缓'], '1455273374')
    x = db.find_music_with_tags(['欢快'])
    print(x)
