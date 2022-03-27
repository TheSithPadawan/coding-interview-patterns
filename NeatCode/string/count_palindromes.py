"""
lc link: https://leetcode.com/problems/palindromic-substrings/

expand from center
same template as lc 5 longest palindromic substring
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        # centered at a single character, odd length substrings
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        
        # centered at a pair, even length substrings
        for i in range(len(s) - 1):
            if s[i] != s[i+1]:
                continue
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        return count