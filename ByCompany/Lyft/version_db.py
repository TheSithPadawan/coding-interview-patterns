"""
第三题：versioned key value datastore
虽然是globalized version，大家看看这篇文章也知道怎么实现了https://martinfowler.com/article ... ersioned-value.html，只要在datastore加一个version class member就可以了。
需要实现
int put(k, value) // 返回version,
int get(k) // 返回last associated value,
int get(k, version) // 返回该version或者version之前最接近的值
int get (k, version)

需要确认的东西: SortedList里面 key, value 怎么排序的

如果这个加上transaction -- 
begin: self.tx.append({})
transaction 不能增加version number 只有commit的时候才能增加version number
begin的时候: put, k, value transaction 这个number只是一个placeholder
"""


import bisect
from collections import deque
import sys

class Database:
    def __init__(self):
        self.db = dict()
        # implement transaction using stack
        """
        put (k, v): {key: list(version number, value)}
        """
        self.version = 0

    def put(self, k, value):
        self.version += 1
        if k not in self.db:
            self.db[k] = []
        self.db[k].append((self.version, value))
    
    def get(self, k):
        if k not in self.db:
            return None
        return self.db[k][-1][-1]
    
    def get(self, k, version):
        if k not in self.db:
            return None
        versioned_values = self.db[k]
        # float("inf") guarantees that we do not use the second value for comparison for things in the list
        index = bisect.bisect_right(versioned_values, (version, float("inf"))) - 1
        if index < 0:
            return -1
        return versioned_values[index][-1]
    


if __name__ == '__main__':
    db = Database()
    db.put('key1', -1)
    db.put('key1', 4)
    db.put('key2', 10)
    db.put('key3', 1)
    db.put('key1', 2)
    print(db.db)
    print(db.get('key1', 4))
    print(db.get('key1', 0))