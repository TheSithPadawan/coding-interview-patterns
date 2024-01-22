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

# solution 2
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        needs = collections.defaultdict(int)
        for char in s1:
            needs[char] += 1
        target = len(s1)
        i, j = 0, 0
        while i < len(s2):
            while j < len(s2) and j - i < len(s1):
                needs[s2[j]] -= 1
                # original string can have multiple the same character
                if needs[s2[j]] >= 0:
                    target -= 1
                j += 1
            if j - i == len(s1) and target == 0:
                return True
            # update left edge
            needs[s2[i]] += 1
            if needs[s2[i]] > 0:
                target += 1
            i += 1
        return False
