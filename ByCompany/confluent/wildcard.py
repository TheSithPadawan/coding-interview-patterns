"""
Q1. wildcard matching 
given string s and pattern, check if pattern p matches s
(1) There is only one * in p
(2) There are multiple *s in p 
Note that DP / memoization solution is not accepted by the company 
"""
def isMatchOne(s, p) -> bool:
	index = p.find ('*')
	if index == -1:
		return s == p
	start, end = 0, len(s) - 1
	t = 0
	# match prefix of s to p[:index]
	while start < len(s) and t < index:
		if s[start] != p[t]:
			return False
		start += 1
		t += 1
	t = len(p) - 1
	start -= 1
	# match postfix of x to p[index+1:]
	while end >= 0 and t > index:
		if s[end] != p[t]:
			return False
		end -= 1
		t -= 1
	end += 1
	return start < end

def isMatchTwo(s, p) -> bool:
	"""
	version 1: p split by *, and for each token in there,
	if it is a substring of s, continue with the next token
	note that anything before the first occurrence of the token is
	replaced by *. Overall time complexity O(mn)
	For example: ("catdog","cat*cat*) tokens = (cat, cat)
	catdog => first occurrence is done then we are matching dog with (cat)
	this doesn't match, so return 
	"""
	tokens = p.split('*')
	index = 0
	for t in tokens:
		if not t:
			continue
		start = s.find(t, index)
		if start == -1:
			return False
		else:
			index = start + len(t)
	return True

def isMatchOptimized(s, p):
	"""
	average case: linear; 
	worst case: O(len(s) * len(p))
	answer adopted from lc discussion: https://leetcode.com/problems/wildcard-matching/discuss/17810/Linear-runtime-and-constant-space-solution
	"""
	sptr, pptr, saved_position, star_position = 0, 0, -1, -1
	while sptr < len(s):
		if pptr < len(p) and s[sptr] == p[pptr]: # match 
			sptr += 1
			pptr += 1
		elif pptr < len(p) and p[pptr] == '*': # found wildcard
			saved_position = sptr
			star_position = pptr
			pptr += 1
		elif pptr < len(p) and star_position != -1: # no match but there is wildcard
			saved_position += 1
			pptr = star_position + 1 # "backtrack"
			sptr = saved_position # recheck
		else: # no match and no wildcard
			return False
	# go through remaining chars if there's any in p
	while pptr < len(p) and p[pptr] == '*':
		pptr += 1
	return pptr == len(p)


def checkOneStar(cases):
	# two star algo should also work for one star case
	for case in cases:
		print ('checking for pair', case)
		print(isMatchOne(case[0], case[1]))
		print(isMatchTwo(case[0], case[1]))

def checkTwoStar(cases):
	for case in cases:
		print ('checking for pair', case)
		print ('isMatchTwo:', isMatchTwo(case[0], case[1]))
		print ('isMatchOptimized:', isMatchOptimized(case[0], case[1]))

def main():
	checkOneStar([('cat', 'c*t'), ('a', 'a*a'), ('dog', 'c*t'), ('abc', '*c'), ('abc', 'a*'), ('abc', 'ab*'), ('abbc', 'ab*bc')])
	checkTwoStar([("catdog","cat*cat*"), ('catdog', '**cat*dog**')])

main()