"""
template for topological sort 
link: https://leetcode.com/problems/course-schedule/
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph, indegree = dict(), dict()
        for i in range(numCourses):
            graph[i] = list()
            indegree[i] = 0
        for req in prerequisites:
            indegree[req[0]] += 1
            graph[req[1]].append(req[0])
        src = []
        for k, v in indegree.items():
            if v == 0:
                src.append(k)
        result = set()
        while src:
            node = src.pop(0)
            result.add(node)
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    src.append(nei)
        return len(result) == numCourses