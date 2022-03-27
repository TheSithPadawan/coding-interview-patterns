"""
Adhoc/ greedy question for meta

lc link: https://leetcode.com/problems/maximum-swap/

Proof:


Thanks to this post: https://leetcode.com/problems/maximum-swap/discuss/185982/Straightforward-O(n)-python
"""

class Solution:
    def maximumSwap(self, num: int) -> int:
        num = [int(x) for x in str(num)]
        max_idx = len(num) - 1
        xi, yi = 0, 0
        for i in range(len(num) - 1, -1, -1):
            if num[i] > num[max_idx]:
                max_idx = i
            elif num[i] < num[max_idx]:
                xi = i
                yi = max_idx
        
        num[xi], num[yi] = num[yi], num[xi]
        return int(''.join([str(x) for x in num]))