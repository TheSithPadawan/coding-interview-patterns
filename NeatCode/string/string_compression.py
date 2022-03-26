"""
lc link: https://leetcode.com/problems/string-compression/
"""
class Solution:
    def compress(self, chars: List[str]) -> int:
        itr = 0
        start, end = 0, 0
        while start < len(chars):
            end = start + 1
            while end < len(chars) and chars[end] == chars[start]:
                end += 1
            runlen = end - start
            chars[itr] = chars[start]
            itr += 1
            if runlen > 1:
                value = str(runlen)
                for i in range(len(value)):
                    chars[itr] = value[i]
                    itr += 1
            start = end
        return itr