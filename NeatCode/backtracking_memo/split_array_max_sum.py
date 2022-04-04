"""
lc link: 

dp state: (start index, budget)
base case: budget = 1, return the postfix
"""

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        store = defaultdict(int)
        
        postfix = [0] * len(nums)
        postfix[-1] = nums[-1]
        for j in range(len(nums)-2, -1, -1):
            postfix[j] = postfix[j+1] + nums[j]
        
        def memo(start, budget):
            if budget == 1:
                if start >= len(nums):
                    return 0
                return postfix[start]
            
            if (start, budget) in store:
                return store[(start, budget)]
            
            res, prefix = float('inf'), 0
            for i in range(start, len(nums)):
                prefix += nums[i]
                maxsum = max(memo(i+1, budget-1), prefix)
                res = min(res, maxsum)
                if prefix > res:
                    break
                
            store[(start, budget)] = res
            return store[(start, budget)]
        
        return memo(0, m)