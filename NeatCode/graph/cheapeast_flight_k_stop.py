class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for source, dest, cost in flights:
            graph[source].append((dest, cost))
        # stores node, cost, stop so far
        minheap = [(0, 0, src)]
        INT_MAX = 2**31 - 1
        stops = [INT_MAX] * n
        while minheap:
            cost, step, node = heapq.heappop(minheap)
            # print ((cost, budget, node))
            if (step > stops[node]) or (step > k + 1):
                # done, no more exploration from here
                continue
            stops[node] = step
            if node == dst:
                return cost
            
            for nei, price in graph[node]:
                heapq.heappush(minheap, (cost + price, step + 1, nei))
        
        return -1

# lc link: https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
# modified dijkstra algo. do not visit the current node if exceeds step requirement
# or we reached the place with lower cost and lower step. lower cost because it is a minheap
# therefore just need to keep track of the steps 
