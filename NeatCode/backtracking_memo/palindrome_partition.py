# lc link: https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def __init__(self):
        self.palindromic_substrings = set()

    def partition(self, s: str) -> List[List[str]]:
        result = []
        # the same problem as subset
        def solve(s, temp):
            if len(s) == 0:
                # end of all partition 
                result.append(copy.deepcopy(temp))
                return 
            
            for i in range(1, len(s) + 1):
                s1 = s[:i]
                if not self.is_palindrome(s1):
                    # current partition is not successful 
                    continue
                temp.append(s1)
                solve(s[i:], temp)
                temp.pop()
        solve(s, [])
        return result
    
    def is_palindrome(self, s):
        if s in self.palindromic_substrings:
            return True
        if s == s[::-1]:
            self.palindromic_substrings.add(s)
            return True
        return False
