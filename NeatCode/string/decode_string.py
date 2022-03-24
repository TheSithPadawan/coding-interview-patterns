# lc link: https://leetcode.com/problems/decode-string/
"""
calculator type of question:
when we encounter [ ==> send to next recursion to get solution
when we encounter ] ==> return current result and index of where to go next
"""

class Solution:
    def decodeString(self, s: str) -> str:
        result, _ = self.decode(s)
        return result
    
    def decode(self, s):
        i, num = 0, 0
        curstr = ''
        while i < len(s):
            c = s[i]
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '[':
                res, j = self.decode(s[i+1:])
                curstr = curstr + res * num
                i += j
                num = 0
            elif c == ']':
                return curstr, i + 1
            else:
                curstr += c
            i += 1
        return curstr, i+1