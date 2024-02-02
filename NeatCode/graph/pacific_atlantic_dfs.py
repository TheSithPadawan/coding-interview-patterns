# wayyy better solution
# intuition from neat code
# lc link: https://leetcode.com/problems/pacific-atlantic-water-flow/submissions/1163494641/
class Solution:
    # finding reachable position from pacific 
    # finding reachable position from atlantic
    # then intersect 
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        result = []

        def dfs(r, c, visit, prev_):
            # height is in reverse direction
            if (r not in range(ROWS)) or (c not in range(COLS)) or (r, c) in visit or heights[r][c] < prev_:
                return

            visit.add((r, c))
            # in 4 directions
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc, visit, heights[r][c])
        
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS-1, c, atlantic, heights[ROWS-1][c])
        
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS-1, atlantic, heights[r][COLS-1])
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append((r, c))
        return result
