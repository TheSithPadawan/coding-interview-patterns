"""
Long solution but it's human-capable solution
No trick, no greedy, plain simple ... and solid

idea:
Cases that def need to return False
(1) s has chars left, p is empty
(2) s doesn't have chars left, p's remaining chars contain things other than '*'
(3) current char of p != '*' and also != current char of s
---
case to continue look at:
(1) current char of p == current char of s ==> move forward
(2) current char of p == '*'. enumerate the # of chars * can represent, which is [0, len(s) - sptr]

finally add cache to turn into a dp 
"""

def isMatch(s, p):
    store = dict()  # <key, value> = <(sptr, pptr), bool>

    def check(s, p, sptr, pptr,):
        if (sptr, pptr) in store:
            return store[(sptr, pptr)]

        # perfect match
        if sptr == len(s) and pptr == len(p):
            store[(sptr, pptr)] = True
            return True
        if sptr < len(s) and pptr == len(p):
            store[(sptr, pptr)] = False
            return False
        if sptr == len(s) and pptr < len(p):
            substr = p[pptr:]
            for i in range(len(substr)):
                if substr[i] != '*':
                    store[(sptr, pptr)] = False
                    return False
            store[(sptr, pptr)] = True
            return True
        if pptr < len(p) and sptr < len(s) and p[pptr] != '*':
            if p[pptr] != '?' and s[sptr] != p[pptr]:
                store[(sptr, pptr)] = False
                return False
            return check(s, p, sptr + 1, pptr + 1)
        if pptr < len(p) and sptr < len(s) and p[pptr] == '*':
            numchars = len(s) - sptr + 1
            for i in range(0, numchars):
                res = check(s, p, sptr + i, pptr + 1)
                if res:
                    return True
        store[(sptr, pptr)] = False
        return False

    return check(s, p, 0, 0)
