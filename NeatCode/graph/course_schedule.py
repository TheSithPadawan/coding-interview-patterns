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


# DFS solution
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # DFS soln 
        preMap = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            preMap[course].append(prereq)

        seen = set()
        def dfs(crs):
            if crs in seen:
                return False
            if preMap[crs] == []:
                return True
            seen.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            seen.remove(crs)
            preMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True

