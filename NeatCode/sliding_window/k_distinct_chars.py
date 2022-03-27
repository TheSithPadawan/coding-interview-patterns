"""
lc link: https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
top fb question
see how I apply the normalized pattern
"""

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        i, j = 0, 0
        count = 0
        freq = defaultdict(int)
        ans = 0
        while j < len(s):
            c = s[j]
            freq[c] += 1
            if freq[c] == 1:
                count += 1
            
            while i <= j and count > k:
                c = s[i]
                freq[c] -= 1
                if freq[c] == 0:
                    count -= 1
                i += 1
            
            ans = max(ans, j - i + 1) 
            j += 1
        return ans