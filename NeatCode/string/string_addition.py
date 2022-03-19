"""
lc link: https://leetcode.com/problems/add-strings/
common interview question for MSFT and fb
"""

class Solution:
    def addStrings(self, s1: str, s2: str) -> str:
        maxsize = max(len(s1), len(s2)) + 1
        result = [0] * maxsize
        if len(s2) > len(s1):
            s1, s2 = s2, s1 
        i, j = len(s1) - 1, len(s2) - 1
        k = maxsize - 1
        while i >= 0 or j >= 0:
            if j >= 0:
                curr = int(s1[i]) + int(s2[j])
                j -= 1
            else:
                curr = int(s1[i])
            temp = (curr + result[k]) % 10
            if (curr + result[k]) // 10 > 0:
                result[k-1] +=  (curr + result[k]) // 10
            result[k] = temp
            i -= 1
            k -= 1
        # construct answer, skip leading zeros
        i = 0
        while i < maxsize and result[i] == 0:
            i += 1
        if i == maxsize:
            return '0'
        return ''.join(str(x) for x in result[i:])