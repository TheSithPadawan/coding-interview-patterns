"""
link: https://www.geeksforgeeks.org/rotate-matrix-elements/

Basically:
Input
1    2    3
4    5    6
7    8    9

Output:
4    1    2
7    5    3
8    9    6

For 4*4 matrix
Input:
1    2    3    4    
5    6    7    8
9    10   11   12
13   14   15   16

Output:
5    1    2    3
9    10   6    4
13   11   7    8
14   15   16   12
"""

def rotate_matrix(matrix):
    top, bottom = 0, len(matrix)
    left, right = 0, len(matrix[0])
    while top + 1 < bottom and left + 1 < right:
        # rotate top row
        # save the start of the ring
        prev = matrix[top][left]
        print ('left', left, 'right', right)
        for i in range(left+1, right):
            temp = matrix[top][i]
            matrix[top][i] = prev
            prev = temp
        top += 1
        # right most column
        for i in range(top, bottom):
            temp = matrix[i][right-1]
            matrix[i][right-1] = prev
            prev = temp
        right -= 1

        if not (top + 1 < bottom or left + 1 < right):
            break

        # bottom row 
        for i in range(right-1, left-1, -1):
            temp = matrix[bottom-1][i]
            matrix[bottom-1][i] = prev
            prev = temp
        bottom -= 1

        # left most column
        for i in range(bottom - 1, top-1, -1):
            temp = matrix[i][left]
            matrix[i][left] = prev
            prev = temp
        left += 1

        # do the top left corner at the end of the ring
        matrix[top-1][left-1] = prev
    return matrix



test_matrix = [[1,2,3],[4,5,6],[7,8,9]]
new_matrix = rotate_matrix(test_matrix)
for i in range(len(new_matrix)):
	print(new_matrix[i])


