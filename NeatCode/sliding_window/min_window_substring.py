# https://leetcode.com/problems/minimum-window-substring/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''
        needs = collections.Counter(t)
        target = len(t)
        i, j = 0, 0

        min_win_leng = len(s) + 1
        ans = ''
        while j < len(s):
            needs[s[j]] -= 1
            if needs[s[j]] >= 0:
                target -= 1
            j += 1
            # update left edge
            while i < j and target == 0:
                if j - i < min_win_leng:
                    min_win_leng = j - i
                    ans = s[i: j]
                
                needs[s[i]] += 1
                if needs[s[i]] > 0:
                    target += 1
                i += 1
        return ans
