# lc link: https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        [1, 2] and [1, 2] cannot be repeated
        but [2, 2] can be repeated
        """
        nums.sort()
        result = []
        def dfs(start, cur):
         
            result.append(copy.deepcopy(cur))
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                cur.append(nums[i])
                dfs(i+1, cur)
                cur.pop()
        
        dfs(0, [])
        return result
