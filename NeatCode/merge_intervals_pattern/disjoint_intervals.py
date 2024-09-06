# lc link: https://leetcode.com/problems/data-stream-as-disjoint-intervals/description/
# use BST to solve this problem

from sortedcontainers import SortedSet

class SummaryRanges:

    def __init__(self):
        self.bst = SortedSet()        

    # add value to the collection
    def addNum(self, value: int) -> None:
        self.bst.add(value)
        
    # construct intervals on demand
    def getIntervals(self) -> List[List[int]]:
        result = []
        # iterate over sorted set
        for val in self.bst:
            if result and result[-1][-1] + 1 == val:
                result[-1] = [result[-1][0], val]
            else:
                result.append([val, val])
        return result

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
