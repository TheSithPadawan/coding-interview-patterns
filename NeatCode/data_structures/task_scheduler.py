# priority queue + deque
# lc link: https://leetcode.com/problems/task-scheduler/

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        maxHeap = [-cnt for cnt in counts.values()]
        # this one is frequency based
        heapq.heapify(maxHeap)
        # this one is time based 
        q = deque()
        time = 0
        
        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            
            if q and time == q[0][1]:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time
