class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        day, fresh = 0, 0
        q = deque()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q:
            num = len(q)
            for i in range(num):
                r, c = q.popleft()
                for dr, dc in directions:
                    if ((r + dr) not in range(ROWS)) or ((c + dc)) not in range(COLS) or grid[r + dr][c + dc] != 1:
                        continue
                    # only enqueue the qualifying ones
                    q.append((r + dr, c + dc))
                    # visit current node
                    grid[r+dr][c+dc] = 2             
                    fresh -= 1
            day += 1
        if fresh > 0:
            return -1
        return day - 1 if day > 0 else 0

# lc link: https://leetcode.com/problems/rotting-oranges/
