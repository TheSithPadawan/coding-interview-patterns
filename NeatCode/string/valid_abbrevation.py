"""
lc link: https://leetcode.com/problems/valid-word-abbreviation/

another commonly asked question in meta interview

the pattern is really similar to the greedy solution for wildcard matching
see code for confluent preparation, link to the optimal solution: 
https://leetcode.com/problems/wildcard-matching/discuss/17810/Linear-runtime-and-constant-space-solution

use state (i, j) to represent pointer in word and abbr respecitvely
(1) when j is a number, advance j
(2) when number > 0, advance i to match (here the number is the wildcard)
(3) when number = 0, advance i and j
(4) in the end we should match the rest of word with wildcard, and both word and abbr
should be fully consumed.
"""

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        m, n = len(word), len(abbr)
        num = 0
        i, j = 0, 0
        while i < m or j < n:
            if j < n and abbr[j].isdigit():
                # handles leading zero and replacing empty string case
                if num == 0 and int(abbr[j]) == 0:
                    return False
                num = num * 10 + int(abbr[j])
                j += 1
            elif num > 0:
                # prevents timeout for big test cases
                if num > m - i + 1:
                    return False
                i += 1
                num -= 1
            elif i < m and j < n and word[i] == abbr[j]:
                i += 1
                j += 1
            else:
                # no match, and no abbreviation
                return False
        # match with remaining chars if possible
        while num > 0:
            i += 1
            num -= 1
        return i == m and j == n