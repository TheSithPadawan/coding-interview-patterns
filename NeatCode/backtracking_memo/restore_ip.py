"""
lc: https://leetcode.com/problems/restore-ip-addresses/
"""

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = set()
        self.dfs(s, 0, 0, [], result)
        return result
    
    def dfs(self, s, start, cur, tmp, result):
        if start == len(s) and len(tmp) == 4:
            tmp = [str(x) for x in tmp]
            result.add('.'.join(tmp))
            return
        
        if start == len(s):
            return
        
        # use the new digit for a new segment
        n = int(s[start])
        tmp.append(n)
        self.dfs(s, start+1, n, tmp, result)
        tmp.pop(-1)
        
        # join the new digit for existing segment if possible
        if cur * 10 + n <= 255:
            if not tmp:
                tmp.append(cur*10+n)
                self.dfs(s, start+1, cur * 10 + n, tmp, result)
                tmp.pop(-1)
            elif tmp[-1] > 0:
                tmp[-1] = cur *10 + n
                self.dfs(s, start+1, cur * 10 + n, tmp, result)
                tmp[-1] //= 10