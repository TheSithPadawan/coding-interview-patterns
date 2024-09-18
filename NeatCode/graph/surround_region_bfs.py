"""
reverse thinking. 
those connected from the non-regions are kept as O
"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # BFS soln: start from O not on the edge if they are connected to other O, replace with X
        M, N = len(board), len(board[0])
        def bfs(source):
            que = deque(source)
            while que:
                r, c = que.popleft()
                # mark
                board[r][c] = 'T'
                dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
                for i in range(4):
                    x, y = r + dx[i], c + dy[i]
                    if x not in range(0, M) or y not in range(0, N):
                        continue
                    if board[x][y] == 'O':
                        que.append((x, y))
        
        edge = []
        for j in range(0, N):
            if board[0][j] == 'O':
                edge.append((0, j))
            if board[M-1][j] == 'O':
                edge.append((M-1, j))
        
        for i in range(1, M-1):
            if board[i][0] == 'O':
                edge.append((i, 0))
            if board[i][N-1] == 'O':
                edge.append((i, N-1))
        
        bfs(edge)
        
        for i in range(0, M):
            for j in range(0, N):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        for i in range(0, M):
            for j in range(0, N):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
        

