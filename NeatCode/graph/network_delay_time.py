class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        minheap = [(0, k)]
        mincost = defaultdict(lambda: 1000)
        mincost[k] = 0
        visit = set()
        while minheap:
            cost, node = heapq.heappop(minheap)
            visit.add(node)
            adj = graph[node]
            for nei, w in adj:
                if nei in visit:
                    continue
                # edge relaxation
                if cost + w < mincost[nei]:
                    mincost[nei] = cost + w
                heapq.heappush(minheap, (cost + w, nei))
        if len(mincost) == n:
            return max(mincost.values()) 
        return -1

# dijkstra py soln 
# lc link: https://leetcode.com/problems/network-delay-time/
