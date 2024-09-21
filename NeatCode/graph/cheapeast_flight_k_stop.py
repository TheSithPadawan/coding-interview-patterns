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


"""
BFS solution: Fix step, minimize cost
""" 
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # BFS: perform k steps from src, and update the min prices 
        INF = 2 ** 31 - 1
        adj = defaultdict(list)
        for a, b, price in flights:
            adj[a].append((b, price))
        costs = [INF] * n
        costs[src] = 0
        que = deque()
        que.append((src, 0))
        seen = set()
        step = 0
        while que:
            for i in range(len(que)):
                node, cost = que.popleft()
                if node in seen:
                    continue
                if step > k:
                    continue
                for nei, p in adj[node]:
                    if cost + p < costs[nei]:
                        costs[nei] = cost + p
                        que.append((nei, costs[nei]))
            step += 1
        return -1 if costs[dst] == INF else costs[dst]

