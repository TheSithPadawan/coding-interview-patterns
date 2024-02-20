# the difference is in asking number of ways for exchange
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = dict()
        def memo(i, n):
            if n == 0:
                return 1
            if i < 0 or n < 0:
                return 0
            if (i, n) in dp:
                return dp[(i, n)]
            # take the current one: (i, n-coins(i))
            # do not take the current one: (i-1, n)
            dp[(i, n)] = memo(i, n - coins[i]) + memo(i-1, n)
            return dp[(i, n)]
        result = memo(len(coins) - 1, amount)
        return result
# lc link: https://leetcode.com/problems/coin-change-ii/
