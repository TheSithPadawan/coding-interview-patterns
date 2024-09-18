# lc link: https://leetcode.com/problems/graph-valid-tree/
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # build graph
        # run dfs to detect cycle
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        seen = set()
        visit = []
        # is tree if no loop + connected
        def dfs(node, prev):
            if node in seen:
                return False
            seen.add(node)
            for nei in graph[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            seen.remove(node)
            visit.append(node)
            return True
        
        res = dfs(0, -1)
        if not res:
            return False
        return len(visit) == n

            
