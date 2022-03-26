"""
lc link: https://leetcode.com/problems/custom-sort-string/

this is to quiz you if you know how to write cmp function
for sorting
"""

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_dict = defaultdict(lambda: 2**31)
        for i, c in enumerate(order):
            order_dict[c] = i
        chars = []
        for c in s:
            chars.append((order_dict[c], c))
        chars = sorted(chars)
        ans = ''
        for pair in chars:
            ans += pair[1]
        return ans