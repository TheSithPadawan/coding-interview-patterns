"""
lc link: https://leetcode.com/problems/add-strings/
common interview question for MSFT and fb

use common template as string multiplication
"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        m,n = len(num1), len(num2)
        res = [0]*(max(m, n))
        i, j = m - 1, n - 1
        k = len(res) - 1
        
        while i >= 0 or j >= 0:
            if i >= 0:
                res[k] += int(num1[i])
            if j >= 0:
                res[k] += int(num2[j])
            i -= 1
            j -= 1
            k -= 1
        
        # cascade propogating carry
        k = len(res) - 1
        while k:
            if res[k] // 10 > 0:
                res[k-1] += res[k] // 10
            res[k] = res[k] % 10
            k -= 1
        
        ans = ''.join(str(x) for x in res)
        ans = ans.lstrip('0')
        if not ans:
            return "0"
        return ans