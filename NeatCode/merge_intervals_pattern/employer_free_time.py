"""
solution using priority queue 
interview ready!
This is a parallel problem to merge k sorted list, instead of integer type,
each item that needs to be sorted is an interval. We only find gap when there is *no overlap*
when an item is processd (popped out of the queue), enqueue the next item ahead.
"""
# this is defined in LC already, but won't compile if I don't put this in soln.py
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
        
class ListInterval(Interval):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.index = -1
        self.listid = -1
    
    # this is a good pattern to use to define an < operator for heapq in python
    def __lt__(self, other):
        return self.start < other.start

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        result = []
        # sorted by start
        minheap = []
        for i, intervalList in enumerate(schedule):
            interval = ListInterval(intervalList[0].start, intervalList[0].end, 0, i)
            minheap.append(interval)
        heapq.heapify(minheap)
        cur = None
        while minheap:
            top = heapq.heappop(minheap)
            if not cur:
                cur = top.end
            else:
                if cur < top.start: # if not overlap
                    result.append(Interval(cur, top.start))
                cur = max(top.end, cur)
            # add the next to the minheap
            if top.index + 1 < len(schedule[top.listid]):
                next = ListInterval(schedule[top.listid][top.index + 1].start, schedule[top.listid][top.index + 1].end, top.index + 1, top.listid)
                heapq.heappush(minheap, next)
        return result