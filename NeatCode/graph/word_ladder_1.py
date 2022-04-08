"""
lc link: https://leetcode.com/problems/word-ladder/
commonly asked in amazon interview
"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
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
        while queue:
            w, dist = queue.popleft()
            if w == endWord:
                # dist edges, dist+1 nodes
                return dist+1 
            for i in range(len(w)):
                pattern = w[:i] + '*' + w[i+1:]
                for nei in graph[pattern]:
                    if nei in visit:
                        continue
                    queue.append((nei, dist+1))
                    visit.add(nei)
        return 0