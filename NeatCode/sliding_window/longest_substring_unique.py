"""
lc link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        counts = set()
        ans = 1
        i, j = 0, 0
        while j < len(s):            
            while s[j] in counts:
                counts.remove(s[i])
                i += 1
            counts.add(s[j])
            # found valid window again, update answer
            ans = max(ans, j - i + 1)
            j += 1
        return ans
