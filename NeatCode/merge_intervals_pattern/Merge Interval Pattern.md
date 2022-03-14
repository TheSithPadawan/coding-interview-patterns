# Merge Interval Pattern
Given some intervals, perform some operation like finding overlaps / non overlaps, etc.
## Merge Intervals
(1) sort the intervals by start
(2) update interval start and end, for overlap case 
(3) case for no overlap, output
```py
def merge(intervals):
  merged = []
  # sort by start
  intervals = sorted(intervals, key=lambda x: x.start)
  curr = None # curr is a reference point
  for interval in intervals:
    if not curr:
      curr = interval
    else:
      if curr.end > interval.start: # has overlap
        curr.end = max(interval.end, curr.end)
      else: # no overlap, output
        merged.append(Interval(curr.start, curr.end))
        curr = interval
  # remember to handle the last one!
  merged.append(curr)
  return merged
```
## Insert Intervals
[Insert Interval (medium) - Grokking the Coding Interview: Patterns for Coding Questions](https://www.educative.io/courses/grokking-the-coding-interview/3jKlyNMJPEM)
Given an interval and a list of disjoint intervals, insert the new one to the sorted list 
(1) skip over non-overlapping ones 
(2) start merging from index i 
```py 
# high level core code
# first skip all non-overlapping ones 
i = 0
curr = newInterval
while i < len... and curr.start > intervals[i].end:
	result.append(intervals[i])
	i += 1

# perform merging 
# i now points to one that overlaps, perform merge from here
while i < len(intervals):
	if not overlap:
		# output curr
		break
	curr.start = min(...)
	curr.end = max(...)
	i += 1

# finally concatenate
```
## Interval Intersection 
[Intervals Intersection (medium) - Grokking the Coding Interview: Patterns for Coding Questions](https://www.educative.io/courses/grokking-the-coding-interview/JExVVqRAN9D)
Given two lists of sorted intervals, output their intersection 
~ merge 2 list version of intervals 
Intersection c can be found for interval a and interval b if they overlap using this formula:
c.start = max(a.start, b.start)
c.end = min(a.end, b.end)
How to increment I, j pointer? 
Ans: increment whoever’s end is earlier greedily
```py 
# core code
while i < len(intervals_a) and j < len(intervals_b):
    if has_overlap(intervals_a[i], intervals_b[j]):
      # output
    if intervals_a[i][1] < intervals_b[j][1]:
      i += 1
    else:
      j += 1

```
## Employee free time 
[Solution Review: Problem Challenge 3 - Grokking the Coding Interview: Patterns for Coding Questions](https://www.educative.io/courses/grokking-the-coding-interview/RLwKZWgMJ1q)
Given a list of list of disjoint intervals. Find the non-overlapping part.
Tips: in intervals pattern a lot of times Priority Queue is used. *In this case it follows the same way to handle merge k sorted list.* Instead of merge: pq is sorted by start time, so we have a scanning line to track the end time of last processed interval. 
When end and top of queue do not intersect, output the gap —> free time. Whenever an interval is popped from queue, enqueue the next one down the road
```py
# code
def find_employee_free_time(schedule):
    result = []
    minheap = []
    def compute_priority(interval):
        return interval.start
    # initialize minheap
    for i in range(len(schedule)):
      heapq.heappush(minheap, (compute_priority(schedule[i][0]), schedule[i][0], 0, i))
    end = -1
	  # keep on updating end
    while minheap:
        top = heapq.heappop(minheap)
        if end == -1:
            end = max(end, top[1].end)
        elif end < top[1].start: # no overlap, output
            result.append(Interval(end, top[1].start))
            end = max(end, top[1].end)
        else: # case with overlap
            end = max(end, top[1].end)
        list_index = top[3]
        hours = len(schedule[list_index])
        hour_index = top[2] + 1
        if hour_index < hours:
            heapq.heappush(minheap, (compute_priority(schedule[list_index][hour_index]), schedule[list_index][hour_index], list_index, hour_index))

    return result

```

