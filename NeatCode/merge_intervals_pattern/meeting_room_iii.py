# lc link: https://leetcode.com/problems/meeting-rooms-iii/
"""
1. track end time, that determines free room
2. since free room requires assigning to min index, thats 
why we have a second pq for that
"""

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        # (end time, room number)
        minheap = []
        rooms = [i for i in range(n)]
        heapq.heapify(rooms)
        counts = [0] * n

        for start, end in meetings:
            # delete already ended meeings
            while minheap and minheap[0][0] <= start:
                _, room = heapq.heappop(minheap)
                heapq.heappush(rooms, room)
            # if no available one, make one available
            endtime = 0
            if not rooms:
                # print(minheap)
                endtime, room = heapq.heappop(minheap)
                heapq.heappush(rooms, room)
            idx = heapq.heappop(rooms)
            # assign
            if endtime > 0:
                heapq.heappush(minheap, (endtime + end - start, idx))
            else:
                heapq.heappush(minheap, (end, idx))
            counts[idx] += 1
        return counts.index(max(counts))
