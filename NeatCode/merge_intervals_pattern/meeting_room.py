"""
lc link: https://leetcode.com/problems/meeting-rooms-ii/

key takeaway:
for python heapq, compute priorty value on the fly
using inline function. and pass into heapq in the form of tuple
(priority value, key)
"""
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        def compute_priority(interval):
            return interval[1]
        intervals.sort(key=lambda x: x[0])
        minheap = []
        minroom = 0
        for interval in intervals:
            while minheap and interval[0] >= minheap[0][1][1]:
                heapq.heappop(minheap)
            heapq.heappush(minheap, (compute_priority(interval), interval))
            # minheap stores all active meetings at a time, we need all of them 
            # to compute the maximum
            minroom = max(minroom, len(minheap))
        return minroom