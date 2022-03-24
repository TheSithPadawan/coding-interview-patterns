"""
lc link: https://leetcode.com/problems/generalized-abbreviation/
commonly asked questions in FB
"""

class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        result = []
        self.dfs(word, 0, '', 0, result)
        return result
    
    def dfs(self, word, index, prefix, count, result):
        if index == len(word):
            prefix = prefix + str(count) if count > 0 else prefix
            result.append(prefix)
            return
        
        # option 1: abbrevate current letter
        self.dfs(word, index + 1, prefix, count+1, result)
        
        # option 2: not to abbrevate
        if count > 0:
            newstr = prefix + str(count) + word[index]
        else:
            newstr = prefix + word[index]
        self.dfs(word, index+1, newstr, 0, result)