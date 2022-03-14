"""
LC problem link: https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/

A bit long but super neat for cpp programmer writing python
Node obj: facilitates access to element directly with value and position
in a vector
removal operation: swap then pop back;
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.index = -1

class RandomizedCollection:

    def __init__(self):
        self.store = defaultdict(list)
        self.bucket = []

    def insert(self, val: int) -> bool:
        node = Node(val)
        node.index = len(self.bucket)
        ans = not (node.val in self.store)
        self.store[val].append(node)
        self.bucket.append(node)
        return ans

    def remove(self, val: int) -> bool:
        if val not in self.store:
            return False
        evictnode = self.store[val][-1]
        backnode = self.bucket[-1]
        self.swap(evictnode, backnode)
        self.bucket.pop(-1)
        self.store[val].pop(-1)
        if not self.store[val]:
            self.store.pop(val)
        return True

    def getRandom(self) -> int:
        randidx = random.randint(0, len(self.bucket)-1)
        return self.bucket[randidx].val
    
    def swap(self, nodei, nodej):
        indexi, indexj = nodei.index, nodej.index
        tmp = self.bucket[indexi]
        self.bucket[indexi] = self.bucket[indexj]
        self.bucket[indexj] = tmp
        # reset the index to be correct
        self.bucket[indexi].index = indexi
        self.bucket[indexj].index = indexj