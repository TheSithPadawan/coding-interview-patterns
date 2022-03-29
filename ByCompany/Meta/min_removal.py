"""
lc link: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
constant space solution specifically tailored for Meta

Note that py string doesn't support assignment, so I turned it into a list
Therefore it's not really a constant space..
"""
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        count = 0
        s = list(s)
        for i in range(len(s)):
            if s[i] == '(':
                count += 1
            elif s[i] == ')':
                if count > 0:
                    count -= 1
                else:
                    # replace
                    s[i] = '#'
        
        count = 0
        # iterate from the end 
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ')':
                count += 1
            elif s[i] == '(':
                if count > 0:
                    count -= 1
                else:
                    s[i] = '#'
        
        result = ''
        for i in range(len(s)):
            if s[i] != '#':
                result += s[i]
        return result