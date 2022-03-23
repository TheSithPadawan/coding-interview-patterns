"""
lc link: https://leetcode.com/problems/permutation-in-string/
Invariant: only chars in s1 will have positive counts
fixed window problem
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        charmap = defaultdict(int)
        for c in s1:
            charmap[c] += 1
        count = len(s1)
        for i, c in enumerate(s2):
            prev = charmap[c]
            charmap[c] -= 1
            if prev > 0:
                count -= 1
            if i - len(s1) + 1 >= 0:
                if count == 0:
                    return True
                # slide the left edge of the window
                left = s2[i - len(s1) + 1]
                charmap[left] += 1
                if charmap[left] > 0:
                    count += 1
        return False