class Solution:
    def checkValidString(self, s: str) -> bool:
        # dp solution: dp state: (position, left count) N^2 dp state, each DP state enumerate s to get the value
        # total time complexity = o(n^3)
        # encounter left parenthese ==> left count + 1
        # encounter right parenthese ==> left count - 1
        # encounter wildcard ==> enumerate
        dp = {(len(s), 0): True}
        def dfs(i, left):
            if i == len(s) or left < 0:
                return left == 0
            if (i, left) in dp:
                return dp[(i, left)]
            if s[i] == '(':
                dp[(i, left)] = dfs(i + 1, left + 1)
            elif s[i] == ')':
                dp[(i, left)] = dfs(i + 1, left - 1)
            else:
                dp[(i, left)] = (
                    dfs(i + 1, left + 1) or dfs(i + 1, left - 1) or dfs(i + 1, left)
                )
            return dp[(i, left)]
        return dfs(0, 0)

# lc link: https://leetcode.com/problems/valid-parenthesis-string/description/
