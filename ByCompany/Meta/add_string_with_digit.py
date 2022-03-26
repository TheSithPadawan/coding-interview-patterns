"""
this is a variation of problem add strings

For example: 123.4 + 2.656 = 126.056
"""

# this is taken from LC 415 with variation

def addStrings(s1: str, s2: str, result, k):
    if len(s2) > len(s1):
        s1, s2 = s2, s1 
    i, j = len(s1) - 1, len(s2) - 1
    while i >= 0 or j >= 0:
        if j >= 0:
            curr = int(s1[i]) + int(s2[j])
            j -= 1
        else:
            curr = int(s1[i])
        temp = (curr + result[k]) % 10
        if (curr + result[k]) // 10 > 0:
            result[k-1] +=  (curr + result[k]) // 10
        result[k] = temp
        i -= 1
        k -= 1
    # i = 0
    # while i < maxsize and result[i] == 0:
    #     i += 1
    # if i == maxsize:
    #     return '0'
    # return ''.join(str(x) for x in result[i:])
    return result, k


# adding two strings with digits
"""
I simplified the problem here a bit that i assume s1 must have . and s2
must have . as well. Integer + Numeric is not in consideration here
"""
def add_strings(s1, s2):
	maxdigits = max(len(s1) - s1.find('.') - 1, len(s2) - s2.find('.'))
	maxnums = max(s1.find('.'), s2.find('.'))
	maxlen = maxdigits + maxnums # add one for decimal
	decimal_position = max(s1.find('.'), s2.find('.'))
	i, j = s1.find('.'), s2.find('.')
	d1, d2 = s1[i+1:], s2[j+1:]
	n1, n2 = s1[:i], s2[:j]
	if len(d1) < len(d2):
		d1, d2 = d2, d1
	results = [0] * maxlen
	k = maxlen - 1
	result, k = addStrings(d1, d2)
	result, k = addStrings(n1, n2)
	# finally perform some join