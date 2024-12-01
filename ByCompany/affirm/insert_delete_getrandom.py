"""
{
    'a': 'apple',
    'b': 'banana',
    'c': 'peach',
    'd': 'pear
}
要求是等概率返回 VALUES
initial requirements:
insert -> O(1)
delete -> O(n)
get random -> O(1)

思路：
dict -> key: value
list -> key 
insert: just insert
delete: pop from list -> o(n)
get_random: get any key from list, then return value from dict
followups:
1. VALUE 等概率 如果有多个相同的 VALUE 的时候
self.values = list()
self.values_counts = dict()
when adding an existing value, update counts, but do not update self.values list
when deleting, reduce count in self.values_counts, if count is zero, remove from dict, and remove value from self.values
2. delete优化到 O（1）同时满足以上的办法
dict STORES key: index, and list stores (key, value)
this way delete takes o(1) by swapping and updating index
still keep the 
self.values = list()
self.values_counts = dict()
self.values_index = dict(): record the value and its position in self.values
3. https://leetcode.com/company/affirm/discuss/1591333/Affirm-or-phone-interview-or-Insert-Delete-GetRandom-O(1)
PUT can replace existing values if alraedy in the map
dict -> {key: index}
list -> [(key, value)]
"""

from collections import defaultdict
from random import choice


class RandomizedDict:
    def __init__(self) -> None:
        self.dict = dict()
        self.kvs = list()
        self.values = list()
        self.values_count = dict()
        self.values_index = dict()

    def insert(self, key, value) -> bool:
        if key in self.dict:
            return True
        self.kvs.append((key, value))
        self.dict[key] = value
        if value not in self.values_count:
            self.values_count[value] = 1
            self.values.append(value)
            self.values_index[value] = len(self.values) - 1
        else:
            self.values_count[value] += 1
        return False
    
    def delete(self, key) -> bool:
        if key not in self.dict:
            return False
        
        index = self.dict[key]
        value = self.kvs[index][1]
        self.kvs[index], self.kvs[-1] = self.kvs[-1], self.kvs[index]
        update_key = self.kvs[index][0]
        self.dict[update_key] = index
        self.dict.pop(key)
        self.kvs.pop()
        # deletion flow for value
        self.values_count[value] -= 1
        # remove the unique value
        if self.values_count == 0:
            self.values_count.pop(value)
            # remove value from self.values
            i = self.values_index[value]
            self.values[i], self.values[-1] = self.values[-1], self.values[i]
            self.values_index[self.values[i]] = i
            self.values_index.pop(value)
            self.values.pop()
        return True

    def get_random(self):
        return choice(self.values)
        


if __name__ == '__main__':
    pass