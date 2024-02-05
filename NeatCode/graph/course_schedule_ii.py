class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph, indegree = dict(), dict()
        for i in range(numCourses):
            graph[i] = list()
            indegree[i] = 0
        for req in prerequisites:
            indegree[req[0]] += 1
            graph[req[1]].append(req[0])
        src = deque()
        for k, v in indegree.items():
            if v == 0:
                src.append(k)
        result = list()
        # edge conditions
        # 1. no source 
        # 2. has cycle
        # 3. has disconnected components
        while src:
            for _ in range(len(src)):
                node = src.popleft()
                result.append(node)
                for nei in graph[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        src.append(nei)
        return result if len(result) == numCourses else []

# lc link: https://leetcode.com/problems/course-schedule-ii/
# using soln from course schedule 1 except to output result
