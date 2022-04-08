"""
lc link: https://leetcode.com/problems/word-ladder-ii/

Amazon also asks for a specific solution, that you only use BFS to find all the paths

"""

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return 0
        
        graph = defaultdict(list)
        # build graph takes O(nm)
        for w in wordList:
            for i in range(len(w)):
                pattern = w[:i] + '*' + w[i+1:]
                graph[pattern].append(w)
        queue = deque()
        queue.append((beginWord,0))
        visit = set([beginWord])
        # traverse all nodes take O(n), in each traversal takes O(m^2) due to substring ops
        mindist = 2**31 - 1
        while queue:
            w, dist = queue.popleft()
            if w == endWord:
                # dist edges, dist+1 nodes
                mindist = dist
                break 
            for i in range(len(w)):
                pattern = w[:i] + '*' + w[i+1:]
                for nei in graph[pattern]:
                    if nei in visit:
                        continue
                    queue.append((nei, dist+1))
                    visit.add(nei)
        
        result = []
        self.dfs(beginWord, endWord, mindist, graph, [beginWord], result)
        return result
    
    # this is a dag so there's no cycle
    def dfs(self, node, end, step, graph, path, result):
        if step == 0:
            if node == end:
                result.append(list(path))
            return
        
        for i in range(len(node)):
            pattern = node[:i] + '*' + node[i+1:]
            for nei in graph[pattern]:
                path.append(nei)
                self.dfs(nei, end, step-1, graph, path, result)
                path.pop()


# BFS only solution
# idea is to delete everything in the result if a better path is found
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        
        graph = defaultdict(list)
        # build graph takes O(nm)
        for w in wordList:
            for i in range(len(w)):
                pattern = w[:i] + '*' + w[i+1:]
                graph[pattern].append(w)
        queue = deque()
        # first tuple stores the path, second the distance
        queue.append(([beginWord],0))
        visit = set([beginWord])
        result = []
        mindist = 2**31 - 1
        while queue:
            path, dist = queue.popleft()
            w = path[-1]
            # notice that visit is added here
            visit.add(w)
            if dist > mindist:
                continue
            if w == endWord:
                if dist < mindist:
                    result = []
                    mindist = dist
                result.append(list(path))
                continue
                    
            for i in range(len(w)):
                pattern = w[:i] + '*' + w[i+1:]
                for nei in graph[pattern]:
                    if nei in visit:
                        continue
                    path.append(nei)
                    queue.append((list(path), dist+1))
                    path.pop()

        return result
        
 