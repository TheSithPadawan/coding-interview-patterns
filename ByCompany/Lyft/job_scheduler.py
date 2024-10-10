"""
Coding:
given a list of overlapping job schedules, find minimal number of workers that can process them.
Note: you can create worker if worker is available, worker id starts with 0
requirements:
if there are multiple workers available, use the worker with the smallest index
assumption:
no two jobs have same start time
Output: job and its worker id. sorted by job ID
有几个variation: 求最少需要多少个worker

Example 
3
0134 25
0055 456
2108 145
3指有三个task
每个task 有两部分：起始时间（HHMM格式） 和持续时间(in min)
2108 45 意思是 一个21:08开始的task 持续了45分钟
可以假设 所有task都在0000 and 2359之间开始以及结束
"""

"""
Algo:
1. sort intervals by start time
2. minheap [endtime, workeridx]
3. free = []
for start, end in jobs:
    # delete jobs from min heap that is already ended
    while minheap and minheap[0][0] <= start:
        heapq.heappop()... 
    if no free worker, allocate:
        workeridx += 1
        heapq.heappush(free, workeridx)
    # get next avaialble workeridx
    workeridx = heapq.heappop(free)
    heapq.heappush(minheap, ...)

max number of workers = workeridx + 1
"""

import heapq
import sys

def convert_to_min(hr, min):
    return hr * 60 + min

def assign_workers(jobs):
    jobs.sort()
    minheap = []
    free = []
    worker = 0
    result = []
    jobId = 0
    for start, duration in jobs:
        while minheap and minheap[0][0] <= start:
            t, workerIdx =heapq.heappop(minheap)
            heapq.heappush(free, workerIdx)
        if not free:
            worker += 1
            heapq.heappush(free, worker)
        # get free worker index 
        workerIdx = heapq.heappop(free)
        # assign current job to this worker
        heapq.heappush(minheap, (start + duration, workerIdx))
        result.append((jobId, workerIdx))
        jobId += 1
    # minimum number of workers = workerIdx
    print('min number of workers needed', worker)
    return result

if __name__ == '__main__':
    content = sys.stdin.read()
    lines = content.splitlines()
    jobs = []
    for i, line in enumerate(lines):
        if i > 0:
            line = line.split()
            jobs.append(((convert_to_min(line[0][:2], line[0][2:])), line[1]))
    result = assign_workers(jobs)
    print(result)    