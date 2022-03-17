"""
lc problem link: https://leetcode.com/problems/4sum/
solving n-sum problems with this pattern
"""
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        
        def ksum(start, target, k):
            results = []
            if k > 2:
                for i in range(start, len(nums)):
                    # only consider uniques
                    if (i > 0 and i > start and nums[i] == nums[i-1]):
                        continue
                    result = ksum(i+1, target - nums[i], k-1)
                    if result:
                        for r in result:
                            r.append(nums[i])
                        results += result
                return results
            
            # reduce to two sum problem
            l, r = start, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    results.append([nums[l], nums[r]])
                    l += 1
                    # only consider uniques
                    while l < len(nums) and nums[l] == nums[l-1]:
                        l += 1
            return results
        return ksum(0, target, 4)