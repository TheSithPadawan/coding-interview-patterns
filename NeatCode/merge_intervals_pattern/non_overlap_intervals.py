class Solution:
    # greedy solution: keep intervals with earlier end time
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[0])
        result = []
        for interval in intervals:
            if not result:
                result.append(interval)
                continue
            current = result[-1]
            if current[1] > interval[0]: # has overlap 
                if current[1] > interval[1]:
                    result.pop()
                    result.append(interval)
            else:
                result.append(interval)
        return len(intervals) - len(result)

# lc link: https://leetcode.com/problems/non-overlapping-intervals/
