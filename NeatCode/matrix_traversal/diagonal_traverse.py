"""
a common problem for Meta
original problem: lc 498 https://leetcode.com/problems/diagonal-traverse/
"""
def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
      	m, n = len(mat), len(mat[0])
        total = m * n
        result = [0] * total
        i = 0
        up = True
        x, y = 0, 0
        while i < total:
            result[i] = mat[x][y]
            if up:
                # three scenarios, two scenarios at the turning point
                if x == 0 or y == n-1:
                    up = False
                    if y == n-1:
                        x += 1
                    else:
                        y += 1
                else:
                    # normal
                    x -= 1
                    y += 1
            else:
                # three scenarios
                if x == m - 1 or y == 0:
                    up = True
                    if x == m-1:
                        y += 1
                    else:
                        x += 1
                else:
                    x += 1
                    y -= 1
            i += 1
        return result

"""
meta variation: only go up
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
print only:
1 4 2 7 5 3 8 6 9

here I provide two versions of solutions
"""
def up_traverse(mat):
    from collections import defaultdict
    store = defaultdict(list)
    for j in range(len(mat[0])):
        for i in range(len(mat)):
            store[i+j].append(mat[i][j])
    result = []
    for _, v in store.items():
        result += v
    return result

# version 2: queue
def up_traverse_queue(mat):
    def is_valid(x, y):
        return x >= 0 and x < len(mat) and y >= 0 and y < len(mat[0])
    # add first col and last row into queue
    queue = []
    for i in range(len(mat)):
        queue.append((i, 0))
    for j in range(1, len(mat[-1])):
        queue.append((len(mat) - 1, j))
    result = []
    while queue:
        x, y = queue.pop(0)
        result.append(mat[x][y])
        nx, ny = x-1, y+1
        while is_valid(nx, ny):
            result.append(mat[nx][ny])
            nx -= 1
            ny += 1
        
    return result