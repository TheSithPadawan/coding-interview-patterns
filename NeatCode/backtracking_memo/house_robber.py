class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = dict()
        def memo(i):
            if i < 0:
                return 0
            if i == 0:
                return nums[0]
            if i in dp:
                return dp[i]
            dp[i] = nums[i]
            for j in range(i-2, -1, -1):
                dp[i] = max(memo(j) + nums[i], dp[i])
            return dp[i]
        return max(memo(len(nums) - 1), memo(len(nums) - 2))

# solution using memo 
# lc link: https://leetcode.com/problems/house-robber/description/
