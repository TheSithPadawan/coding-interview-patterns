"""
lc link: https://leetcode.com/problems/jump-game-ii/
1 dimension dp just need to keep track of index as state
"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = dict()
        def memo(index):
            if index >= len(nums) - 1:
                return 0
            
            if index in dp:
                return dp[index]
            
            dp[index] = float('inf')
            for step in range(nums[index] + 1):
                dp[index] = min(dp[index], 1+memo(index+step))
            return dp[index]
        return memo(0)