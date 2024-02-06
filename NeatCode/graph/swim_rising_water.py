class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        minheap = [(grid[0][0], 0, 0)]
        visit = set()
        while minheap:
            maxh, r, c = heapq.heappop(minheap)
            if (r, c) == (ROWS - 1, COLS - 1):
                return maxh
            if (r, c) in visit:
                continue
            visit.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                if r + dr not in range(ROWS) or c + dc not in range(COLS) or (r + dr, c + dc) in visit:
                    continue
                cost = max(maxh, grid[r + dr][c+dc])
                heapq.heappush(minheap, (cost, r+dr, c+dc))
        return -1

# lc link: https://leetcode.com/problems/swim-in-rising-water/
# Dijkstra's algo. this question actually asks about minimizing the maximum height along the path
# choose the best path
