"""
LC Problem link: https://leetcode.com/problems/regular-expression-matching/

Idea:
- base case: s has chars left, but p does not have -> returns False
- other situations
(1) current one is not * or ., if doesn't match, return False
(2) current one is ., give it a try, moving forward
(3) next one is *, take 2 decisions: use it (i, j) -> transfers to (i+1, j)
do not use it: (i, j) -> (i, j+2)
(4) normal match workflow, no *: (i, j) -> (i+1, j+1)
"""
def isMatch(self, s: str, p: str) -> bool:
    store = dict()
    def dfs(sptr, pptr):
        if (sptr, pptr) in store:
            return store[(sptr, pptr)]
        if sptr >= len(s) and pptr >= len(p):
            return True
        if pptr >= len(p): # means s has chars left, but p doesn't have
            return False
        match = sptr < len(s) and (s[sptr] == p[pptr] or p[pptr] == '.')
        # check for the next char 
        if pptr + 1 < len(p) and p[pptr+1] == '*':
            store[(sptr, pptr)] = dfs(sptr, pptr+2) or (match and dfs(sptr + 1, pptr))
            return store[(sptr, pptr)]
        if match:
            store[(sptr, pptr)] = dfs(sptr + 1, pptr + 1)
            return store[(sptr, pptr)]
        return False # catch all
    return dfs(0, 0)