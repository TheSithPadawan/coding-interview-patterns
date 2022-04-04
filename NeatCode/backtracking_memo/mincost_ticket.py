"""
lc link: 

https://leetcode.com/problems/minimum-cost-for-tickets/

solution similar to jump game II, except that need to skip over the days
that are covered
"""

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # dp[i]: min cost starting at day i
        # note that if a pass is purchased on before, and this day is still covered, we don't need to dfs from here
        dp = dict()
        
        def memo(i):
            if i == len(days):
                return 0
            if i in dp:
                return dp[i]
            
            counts = [1, 7, 30]
            dp[i] = float('inf')
            for k in range(3):
                d, c = counts[k], costs[k]
                j = i 
                # skip over the days that are covered
                while j < len(days) and days[j] < days[i] + d:
                    j += 1
                dp[i] = min(memo(j) + c, dp[i])
                
            return dp[i]
        
        return memo(0)