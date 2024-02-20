class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = dict()

        # state: (i, buy) buy means if you're eligible to buy in this state
        def dfs(i, buy):
            if i >= len(prices):
                return 0
            if (i, buy) in dp:
                return dp[(i, buy)]
            # cooldown is always an option
            cooldown = dfs(i+1, buy)
            if buy:
                curmax = dfs(i+1, not buy) - prices[i]
                dp[(i, buy)] = max(curmax, cooldown)
            else:
                curmax = dfs(i+2, True) + prices[i]
                dp[(i, buy)] = max(curmax, cooldown)
            return dp[(i, buy)]
        return dfs(0, True)

