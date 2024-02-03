class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = 2147483647
        q = deque()
        ROWS, COLS = len(rooms), len(rooms[0])
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append((r, c, 0))
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q:
           num = len(q)
           for _ in range(num):
                r, c, dist = q.popleft()
                for dr, dc in directions:
                    if ((r + dr) not in range(ROWS)) or ((c + dc) not in range(COLS)) or (rooms[r + dr][c + dc] == -1) or rooms[r+dr][c+dc] < dist + 1:
                        continue
                    q.append((r + dr, c + dc, dist + 1))
                    rooms[r + dr][c + dc] = dist + 1
# lc link: https://leetcode.com/problems/walls-and-gates/
# slow BFS solution, there must be better solution
