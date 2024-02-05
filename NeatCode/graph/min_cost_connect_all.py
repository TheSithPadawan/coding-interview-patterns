class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        graph = {i: [] for i in range(N)}  # i : list of [cost, node]
        # O(N^2) to construct graph
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                graph[i].append([dist, j])
                graph[j].append([dist, i])
        visit = set()
        minheap = [[0, 0]]
        total = 0
        while len(visit) < N:
            cost, p = heapq.heappop(minheap)
            if p in visit:
                continue
            visit.add(p)
            total += cost
            for dist, nei in graph[p]:
                if nei not in visit:
                    # minheap can contain duplicated vertices
                    heapq.heappush(minheap, [dist, nei])
        return total

# Prim's min spanning tree algo
# https://leetcode.com/problems/min-cost-to-connect-all-points/description/
