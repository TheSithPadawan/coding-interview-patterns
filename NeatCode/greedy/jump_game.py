class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # greedy thinking: we can shift the goal from the end to beginning
        # anything after the goal post is reachable. ~ optimal substructure, it is continuous
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1 ,-1):
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False

# lc link: https://leetcode.com/problems/jump-game/
