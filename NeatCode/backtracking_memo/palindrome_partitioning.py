"""
lc link: 

use backtracking
each time take some substring off the original string, and check if it is
palindrome
"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        results = []
        if not s:
            return results
        
        def dfs(substr, temp):
            if not substr:
                results.append(list(temp))
                return
            
            for end in range(1, len(substr)+1):
                prefix = substr[:end]
                if prefix == prefix[::-1]:
                    temp.append(prefix)
                    dfs(substr[end:], temp)
                    temp.pop()
        
        dfs(s, [])
        return results