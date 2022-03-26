"""
lc link: https://leetcode.com/problems/multiply-strings/

see line 20 - 25 that's a common pattern for performing
string operation, cascade propogation of carry.
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        
        m,n = len(num1), len(num2)
        res = [0]*(m+n)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                x = int(num1[i]) * int(num2[j])
                res[i+j+1] += x
                
        k = len(res) - 1
        while k:
            if res[k] // 10 > 0:
                res[k-1] += res[k] // 10
            res[k] = res[k] % 10
            k -= 1
        
        ans = ''.join(str(x) for x in res)
        ans = ans.lstrip('0')
        return ans