class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {0: 0}
        INT_MAX = 2**31 - 1
        for coin in coins:
            dp[coin] = 1
        def memo(target):
            if target in dp:
                return dp[target]
            dp[target] = INT_MAX
            for coin in coins:
                if coin < target:
                    dp[target] = min(dp[target], 1 + memo(target - coin))
            return dp[target]
        
        memo(amount)
        if dp[amount] == INT_MAX:
            return -1
        return dp[amount]

# lc link: https://leetcode.com/problems/coin-change/
# time complexity: O(amount x coins)
