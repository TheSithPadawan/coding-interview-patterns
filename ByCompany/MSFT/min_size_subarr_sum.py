"""
lc link: https://leetcode.com/problems/minimum-size-subarray-sum/
sliding window pattern
Follow up question is: what if there are negative numbers in the array
target = 6
[    , -5 , 1, 10,  ]
follow up question link: https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, j = 0, 0
        prefix = 0
        ans = 2**31 - 1
        while j < len(nums):
            prefix += nums[j]
            j += 1
            while i < j and prefix >= target:
                ans = min(ans, j - i)
                prefix -= nums[i]
                i += 1
        if ans == 2**31 - 1:
            return 0
        return ans

"""
Follow up question Solution. 
Intuition credited to CodeForce Discussion here: https://codeforces.com/blog/entry/60512
Key idea here:
- For the second while loop pop front operation, the rationale is: 
to delete the useless elements in the front. Because if I don't use them here, and use 
them later, I would not have achieved a better solution, because later my index is larger
so the subarray is longer.
- For the first while loop, use it to maintain the "order" of the dequeue
"""
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        stack = []
        i, j = 0, 0
        prefix = 0
        ans = 2**31 - 1
        # to handle the edge case where the first number in the array is the target
        # For example: [167, 84,-37,32,40,95], target = 167
        stack.append((-1, 0)) 
        while j < len(nums):
            prefix += nums[j]
            while stack and prefix <= stack[-1][1]:
                stack.pop(-1)
            stack.append((j, prefix))
            while stack and stack[0][1] <= prefix - k:
                ans = min(ans, j - stack[0][0])
                stack.pop(0)
            j += 1
        if ans == 2**31 - 1:
            return -1
        return ans