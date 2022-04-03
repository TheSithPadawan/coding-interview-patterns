"""
lc: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

state: set (i, j) to record longest increasing path length starting from
position i and j
"""

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        def memo(i, j, prev, store):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS:
                return 0
            if matrix[i][j] <= prev:
                return 0
            if (i, j) in store:
                return store[(i, j)]
            
            dx = [1, 0, -1, 0]
            dy = [0, -1, 0, 1]
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                store[(i, j)] = max(store[(i, j)], 1 + memo(nx, ny, matrix[i][j], store))
                
            return store[(i, j)]
        
        store = defaultdict(int)
        ans = 1
        for i in range(ROWS):
            for j in range(COLS):
                ans = max(memo(i, j, -1, store), ans)
                
        return ans