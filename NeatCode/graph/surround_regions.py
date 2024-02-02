class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        visit = set()

        def dfs(r, c, visit, prev_):
            if r not in range(ROWS) or c not in range(COLS) or (r, c) in visit or board[r][c] == 'X':
                return

            visit.add((r, c))
            if board[r][c] == 'O' and prev_ == 'N':
                board[r][c] = 'N'
            
            # in 4 directions
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc, visit, board[r][c])

        for r in range(ROWS):
            if board[r][0] == 'O':
                board[r][0] = 'N'
                dfs(r, 0, visit, board[r][0])
            if board[r][COLS-1] == 'O':
                board[r][COLS-1] = 'N'
                dfs(r, COLS-1, visit, board[r][COLS-1])
        
        for c in range(COLS):
            if board[0][c] == 'O':
                board[0][c] = 'N'
                dfs(0, c, visit, board[0][c])
            if board[ROWS-1][c] == 'O':
                board[ROWS-1][c] = 'N'
                # print ('calling from position', ROWS-1, c)
                # print ('size of visit', len(visit))
                dfs(ROWS-1, c, visit, board[ROWS-1][c])
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'N':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'

# lc link: https://leetcode.com/problems/surrounded-regions/
