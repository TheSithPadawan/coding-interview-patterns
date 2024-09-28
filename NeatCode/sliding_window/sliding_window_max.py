# lc link: https://leetcode.com/problems/sliding-window-maximum/description/
# soln 1: decreasing queue 
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # decreasing queue solution O(n)
        """
        window size is maintained by r, l index, it doesn't have anything to do with deleting elements in queue
        """
        queue = collections.deque()
        l = r = 0
        result = []
        for r in range(len(nums)):
            # delete values less than the current one
            while queue and nums[r] > nums[queue[-1]]:
                queue.pop()
            queue.append(r)

            if l > queue[0]:
                queue.popleft()
            if r - l + 1 == k:
                result.append(nums[queue[0]])
                l += 1
        return result


# soln 2: bst solution O(n lgk)
from sortedcontainers import SortedList
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        sl = SortedList()
        result = []
        for r in range(len(nums)):
            sl.add(nums[r])
            if r - l + 1 == k:
                # get the largest elemtn
                result.append(sl[-1])
                sl.remove(nums[l])
                l += 1
        return result
