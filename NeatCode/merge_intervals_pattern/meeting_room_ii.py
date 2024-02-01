class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # two solutions 
        # solution # 1, sort + count
        # solution 2: priority queue --> answer = queue.size 
        points = []
        for interval in intervals:
            points.append((interval[0], 0))
            points.append((interval[1], -1))
        points = sorted(points, key=lambda x: (x[0], x[1]))
        room = 0
        maxroom = 0
        for p in points:
            if p[1] == 0:
                room += 1
            else:
                room -= 1
            maxroom = max(room, maxroom)
        return maxroom

# lc link: https://leetcode.com/problems/meeting-rooms-ii/
