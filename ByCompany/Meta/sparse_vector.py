"""
lc link: https://leetcode.com/problems/dot-product-of-two-sparse-vectors/

this is the only soln that meta recruiting is looking for
because they somehow think that hashmap is a waste of resource...
lmao... premature optimization.. but let's cater to their taste
"""

class SparseVector:
    def __init__(self, nums: List[int]):
        self.vec = []
        for i, val in enumerate(nums):
            if val != 0:
                self.vec.append((i, val))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, other: 'SparseVector') -> int:
        i, j = 0, 0
        sum = 0
        m, n = len(self.vec), len(other.vec)
        while i < m and j < n:
            if self.vec[i][0] == other.vec[j][0]:
                sum += self.vec[i][1] * other.vec[j][1]
                i += 1
                j += 1
            elif self.vec[i][0] < other.vec[j][0]:
                i += 1
            else:
                j += 1
        return sum