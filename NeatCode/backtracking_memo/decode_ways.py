"""
lc link: https://leetcode.com/problems/decode-ways/
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        
        
        def numways(num, store):
            if not num or len(num) == 1:
                if num and num[0] == '0':
                    return 0
                return 1
            if num in store:
                return store[num]
            
            takeone, taketwo = 0, 0
            if num[0] != '0':
                takeone = numways(num[1:], store)
                if int(num[:2]) <= 26:
                    taketwo = numways(num[2:], store)
            store[num] = takeone + taketwo
            return store[num]
        
        return numways(s, dict())