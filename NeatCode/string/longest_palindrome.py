"""
lc link: https://leetcode.com/problems/longest-palindromic-substring/

use the template to expand from two different centers
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = 1
        substr = s[0]
        
        # centered at a single character, odd length substrings
        for i in range(len(s)):
            l, r = i-1, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > length:
                    length = r - l + 1
                    substr = s[l:r+1]
                l -= 1
                r += 1
        
        # centered at a pair, even length substrings
        for i in range(len(s) - 1):
            if s[i] != s[i+1]:
                continue
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > length:
                    length = r - l + 1
                    substr = s[l:r+1]
                l -= 1
                r += 1
        return substr