# lc link: https://leetcode.com/problems/maximum-product-subarray/
# revised kadane algorithm
# there are three ways to contribute to curmax for nums[i] 
# nums[i] itself, nums[i] x curmin, nums[i] x curmax, similarly, update curmin. 
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curmax, curmin = nums[0], nums[0]
        globalmax = curmax
        for i in range(1, len(nums)):
            temp = max(nums[i], nums[i] * curmax, nums[i]*curmin)
            curmin = min(nums[i], nums[i] * curmin, nums[i]*curmax)
            curmax = temp
            globalmax = max(curmax, globalmax, curmin)
        return globalmax


