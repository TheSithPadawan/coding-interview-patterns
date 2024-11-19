"""
This problem was asked by Google.

Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.

Integers can appear more than once in the list. You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.
"""

"""
Soln 1: DFS to generate all possible subsets 
All subset sums to a target
"""
def get_subset_sums(nums, target):
    result = []
    def dfs(start, cursum, subset):
        if cursum == target:
            result.append(list(subset))
            return 
        
        # decision to make: add current to the subset or not
        for i in range(start, len(nums)):
            if cursum + nums[i] > target:
                continue
            subset.append(nums[i])
            dfs(i+1, cursum+nums[i], subset)
            subset.pop()
    dfs(0, 0, [])
    return result

"""
Soln 2: dynamic programming
Is there one or more values in the array that has subset sum equals to target knapsack problem
"""
def check_subset_sum(nums, target):
    # subproblem: considering first i values, decide to take current one or do not take
    # current one
    dp = dict()
    dp[(0, 0)] = True
    def memo(i, target):
        # base case
        if i == 0:
            return target == 0
        if (i, target) in dp:
            return dp(i, target)
        # consider current one
        dp[(i, target)] = False
        consider = False
        if target - nums[i-1] >= 0:
            consider = memo(i-1, target - nums[i-1])
        dp[(i, target)] = consider or memo(i-1, target)
        return dp[(i, target)]
    result = memo(len(nums), target)
    # find the subset itself
    # (6, 24) --> (5, 22) True --> (4, 13) True --> (3, 8) False did not include 5, --> (3, 13) True
    return result, dp

def get_result(nums, dp, target):
    subset = []
    def backtrack(i, val):
        if i == 0:
            return
        if (i-1, val-nums[i-1]) in dp and dp[(i-1, val-nums[i-1])]:
            # means that current number is included in the answer
            subset.append(nums[i-1])
            backtrack(i-1, val-nums[i-1])
        else:
            backtrack(i-1, val)
    backtrack(len(nums), target)
    return subset        

if __name__ == '__main__':
    S = [12, 1, 61, 5, 9, 2]
    k = 24
    # print(get_subset_sums(S, k))
    result, dp = check_subset_sum(S, k)
    print(get_result(S, dp, k))

    # test case 2
    S = [1, -1, 2]
    result, dp = check_subset_sum(S, 0)
    print('result', result)
    print(get_result(S, dp, 0))