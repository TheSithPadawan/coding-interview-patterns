class Solution:
    def alienOrder(self, words: List[str]) -> str:
        indegree = defaultdict(int)
        graph = defaultdict(list)
        charset = {char for word in words for char in word}
        for char in charset:
            indegree[char] = 0
        for i in range(len(words) - 1):
            current, next_ = words[i], words[i+1]
            minlen = min(len(current), len(next_))
            # edge case: abc ab
            if len(current) > len(next_) and current[:minlen] == next_[:minlen]:
                return ""
            for j in range(min(len(current), len(next_))):
                if current[j] == next_[j]:
                    continue
                # current[j] -> next_[j]
                graph[current[j]].append(next_[j])
                indegree[next_[j]] += 1
                break
        q = deque()
        result = []
        for k, v in indegree.items():
            if v == 0:
                q.append(k)
        while q:
            node = q.popleft()
            result.append(node)
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        if len(result) != len(charset):
            return ""
        return "".join(result)

# build graph + topological sort, output order
# lc link: https://leetcode.com/problems/alien-dictionary/description/
