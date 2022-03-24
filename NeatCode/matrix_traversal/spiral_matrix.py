"""
lc link: 
use 4 pointers to manage position 
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])
        result = []
        while top < bottom and left < right:
            # go from left to right
            for i in range(left, right):
                result.append(matrix[top][i])
            top += 1
            
            # go from top to bottom 
            for i in range(top, bottom):
                result.append(matrix[i][right-1])
            right -= 1
            
            if not (top < bottom and left < right):
                break
                
            # go from right to left 
            for i in range(right-1, left - 1, -1):
                result.append(matrix[bottom-1][i])
            bottom -= 1
            
            # go from bottom to top
            for i in range(bottom-1, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
        
        return result