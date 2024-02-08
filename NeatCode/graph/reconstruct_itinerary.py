class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = defaultdict(list)
        count = len(tickets)
        for source, dest in tickets:
            adj[source].append(dest)
        
        res = ['JFK']
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False
            temp = list(adj[src])
            for i, v in enumerate (temp):
                adj[src].pop(i)
                res.append(v)
                if (dfs(v)): return True
                adj[src].insert(i, v)
                res.pop()
            return False
        dfs('JFK')
        return res

# lc link: https://leetcode.com/problems/reconstruct-itinerary/description/
# DFS + Backtracking soln -- TLE time complexity is exponential

# Better solution: post order DFS traversal, only output to the result when a node is a sink.
# meaning that we have visited all the outgoing edges
