class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # two ways to solve this: (1) prefix sum (2) kadane's algorithm
        current_max, global_max = nums[0], nums[0]
        for num in nums[1:]:
            # update current max ==> decide new subarray starts from num, or extend to num
            current_max = max(num, num + current_max)
            global_max = max(global_max, current_max)
        return global_max

# lc link: https://leetcode.com/problems/maximum-subarray/
