"""
lc link: https://leetcode.com/problems/flatten-nested-list-iterator/

Pattern for iterator questions: 
- can always populate some data structure (queue / stack)
"""

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.queue = []
        self.nestedList = nestedList
        self.populate_queue()
    
    def next(self) -> int:
        ans = self.queue.pop(0)
        self.populate_queue()
        return ans
        
    
    def hasNext(self) -> bool:
        return len(self.queue) > 0
    
    def populate_queue(self):
        if not self.nestedList:
            return
        NI = self.nestedList.pop(0)
        result = []
        self.flatten_NI(NI, result)
        if not result:
            self.populate_queue()
        self.queue += result
    
    def flatten_NI(self, NI, result):
        if NI.isInteger():
            result.append(NI.getInteger())
            return
        for item in NI.getList():
            self.flatten_NI(item, result)