# lc link: https://leetcode.com/problems/permutations/description/
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        def dfs(values, temp):
            if len(temp) == len(nums):
                result.append(copy.deepcopy(temp))
                return
            
            for i in range(len(values)):
                temp.append(values[i])
                dfs(values[:i] + values[i+1:], temp)
                temp.pop()
        dfs(nums, [])
        return result
