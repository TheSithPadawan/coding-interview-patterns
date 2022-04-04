"""
lc link: https://leetcode.com/problems/combination-sum-iv/

same question as coin change -- unbounded knapsack
"""

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {}
        nums.sort()
        def memo(value):
            if value == 0:
                return 1
            
            if value in dp:
                return dp[value]
            
            dp[value] = 0
            for i, n in enumerate(nums):
                if n > value:
                    break
                dp[value] += memo(value - n)
                
            return dp[value]
        return memo(target)