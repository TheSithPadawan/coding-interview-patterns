class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = dict()
        def memo(i, j):
            if i < 0 or j < 0:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            dp[(i, j)] = 0
            if text1[i] == text2[j]:
                dp[(i, j)] = max(dp[(i, j)], memo(i-1, j-1) + 1)
            else:
                dp[(i, j)] = max([dp[(i, j)], memo(i, j-1), memo(i-1, j)])
            return dp[(i, j)]
        return memo(len(text1) - 1, len(text2) - 1)

# lc link: https://leetcode.com/problems/longest-common-subsequence/description/
