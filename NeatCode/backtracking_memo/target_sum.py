class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def dfs(i, a):
            if i == len(nums):
                return 1 if target == a else 0
            if (i, a) in cache:
                return cache[(i, a)]

            cache[(i, a)] = dfs(i+1, a + nums[i]) + dfs(i + 1, a-nums[i])
            return cache[(i, a)]

        result = dfs(0, 0)
        return result

# the same as coin change 2
# lc link: https://leetcode.com/problems/target-sum/ 
# time com = O(len(nums) x target)
