"""
LC 417. pacific atlantic water flow
LC Question link: https://leetcode.com/problems/pacific-atlantic-water-flow/
A bit long but very readable
Just BFS from atlantic and pacific separately, then do intersection to produce answer
"""


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific, atlantic = [[False for j in range(n)] for i in range(m)],  [[False for j in range(n)] for i in range(m)]
        dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
        def is_valid(x, y, curheight):
            if x < 0 or x >= m or y < 0 or y >= n:
                return False
            if heights[x][y] < curheight:
                return False
            return True
        
        def bfs(queue, board):
            seen = set()
            for pos in queue:
                seen.add((pos[0], pos[1]))
                
            while queue:
                cur = queue[0]
                queue.pop(0)
                x, y = cur[0], cur[1]
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if is_valid(nx, ny, heights[x][y]) and (nx, ny) not in seen:
                        queue.append((nx, ny))
                        seen.add((nx, ny))
                        # current position is reachable 
                        board[nx][ny] = True
        queue = []
        for j in range(n):
            queue.append((0, j))
            pacific[0][j] = True
        for i in range(1, m):
            queue.append((i, 0))
            pacific[i][0] = True
        # first check pacific
        bfs(queue, pacific)
        # then check atlantic 
        queue = []
        for i in range(m):
            queue.append((i, n-1))
            atlantic[i][n-1] = True
        for j in range(n-1):
            queue.append((m-1, j))
            atlantic[m-1][j] = True
        bfs(queue, atlantic)            
        # produce result
        result = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    result.append((i, j))
        return result