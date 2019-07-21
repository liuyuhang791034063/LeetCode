"""
使用一个字典记录密钥和值的关系
使用一个队列记录密钥使用的前后 来确定最近最少使用
"""


class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.maxlength = capacity
        self.array = {}
        self.array_list = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        value = self.array.get(key)
        # 如果密钥存在 将该密钥移到队列首
        if value is not None and self.array_list[0] is not key:
            index = self.array_list.index(key)
            self.array_list.pop(index)
            self.array_list.insert(0, key)

        value = value if value is not None else -1
        return value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # 如果重复
        if self.array.get(key) is not None:
            index = self.array_list.index(key)
            self.array.pop(key)
            self.array_list.pop(index)

        # 如果队满
        if len(self.array_list) >= self.maxlength:
            key_t = self.array_list.pop(self.maxlength-1)
            self.array.pop(key_t)

        # 插入队首
        self.array[key] = value
        self.array_list.insert(0, key)


"""
另一种方法使用collections中OrderedDict
"""
from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dic = OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dic:
            val = self.dic[key]
            del self.dic[key]
            self.dic[key] = val
            return val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dic:
            del self.dic[key]
        elif len(self.dic) == self.capacity:
            # popitem方法 如果True 则删除最后一个 如果False 则删除第一个
            self.dic.popitem(False)
        self.dic[key] = value


if __name__ == '__main__':
    test = LRUCache(2)
    test.put(2,1)
    test.put(1,1)
    test.get(2)
    test.put(4,1)
    test.get(1)
    test.get(2)
