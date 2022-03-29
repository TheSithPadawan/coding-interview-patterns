"""
lc link: https://leetcode.com/problems/word-break-ii/

use dfs approach to check for prefix and breakdown the postfix
store results in dict
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # store: <string: [list of lists]>
        wordDict = set(wordDict)
        def dfs(s, store):
            if not s:
                return [[]]
            
            if s in store:
                return store[s]
            
            # enumerate prefix length
            for end in range(1, len(s) + 1):
                prefix = s[:end]
                if prefix in wordDict:
                    posts = dfs(s[end:], store)
                    for sublist in posts:
                        store[s].append([prefix] + sublist)
            return store[s]
        store = defaultdict(list)
        dfs(s, store)
        return [' '.join(word) for word in store[s]]