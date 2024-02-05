class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        def dfs(node, dest, visit):
            if node == dest:
                return True

            for nei in graph[node]:
                if nei not in visit:
                    visit.add(nei)
                    if dfs(nei, dest, visit):
                        return True
            return False
        
        # reverse 
        for start, end in edges[::-1]:
            # remove start - end, if still reachable, then it is the redundant connection
            graph[start].remove(end)
            result = dfs(start, end, set())
            if result:
                return [start, end]
            graph[start].add(end)

        return []

# lc link: https://leetcode.com/problems/redundant-connection/description/
