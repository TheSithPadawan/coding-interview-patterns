class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        position_map = defaultdict(deque)
        result = [0] * len(queries)
        for i, q in enumerate(queries):
            position_map[q].append(i)
        queries.sort()
        minheap = []
        i = 0
        for num in queries:
            while i < len(intervals) and num >= intervals[i][0]:
                # store (segment length, segment ending) in min heap
                heapq.heappush(minheap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1
            # do not look at the segments that do not qualify
            while minheap and minheap[0][1] < num:
                heapq.heappop(minheap)
            index = position_map[num].popleft()
            if not minheap:
                result[index] = -1
            else:
                minlen, _ = minheap[0]
                result[index] = minlen
        return result

# lc link: https://leetcode.com/problems/minimum-interval-to-include-each-query/
# dynamically updating the heap
