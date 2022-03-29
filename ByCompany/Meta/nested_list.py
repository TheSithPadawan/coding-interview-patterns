"""
Meta high frequency

lc link: https://leetcode.com/problems/nested-list-weight-sum/
track depth and recursively sum up the values
"""

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        return self.get_results(nestedList, 1)
        
    def get_results(self, nestedList, depth):
        res = 0
        for NI in nestedList:
            if NI.isInteger():
                res += NI.getInteger() * depth
            else:
                res += self.get_results(NI.getList(), depth+1)
        return res