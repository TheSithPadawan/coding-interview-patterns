# soln using union find 
# lc link: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
"""
0 - 1
   /
  2 - 3
"""
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * (n)

        # union find stuff
        def find(node):
            p = node
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        def union(a, b):
            p1, p2 = find(a), find(b)
            if p1 == p2:
                return 0
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return 1

        # call 
        cnt = 0
        for a, b in edges:
            cnt += union(a, b)
        
   
        # count
        return n - cnt
