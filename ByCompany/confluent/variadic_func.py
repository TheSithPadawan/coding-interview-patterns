"""
Note:
If a function is marked as isVariadic=true, then the last argument can occur one or more number of times.

Example:
FuncA: [String, Integer, Integer]; isVariadic = false
FuncB: [String, Integer]; isVariadic = true
FuncC: [Integer]; isVariadic = true
FuncD: [Integer, Integer]; isVariadic = true
FuncE: [Integer, Integer, Integer]; isVariadic = false
FuncF: [String]; isVariadic = false
FuncG: [Integer]; isVariadic = false

findMatches({String}) -> [FuncF]
findMatches({Integer}) -> [FuncC, FuncG]
findMatches({Integer, Integer, Integer, Integer}) -> [FuncC, FuncD]
findMatches({Integer, Integer, Integer}) -> [FuncC, FuncD, FuncE]
findMatches({String, Integer, Integer, Integer}) -> [FuncB]
findMatches({String, Integer, Integer}) -> [FuncA, FuncB]
"""
from collections import defaultdict
# this class is given in the interview
class Function:

	def __init__ (self, name, argtypes, isvariadic):
		self.name = name
		self.argtypes = argtypes
		self.is_variadic = isvariadic

	def __str__(self):
		return '.'.join(self.argtypes)

"""
This is a Trie problem, with each trie node = function type
Algo: for each function, store in hashmap as <arg types, [function object]>
In the prefix search itself, search for each arg type prefix 
E.g.
Integer, String, Integer, String
first search Integer
then search Integer,string
then search Integer, String, Integer
finally Integer, String, Integer, String
If prefix matches, check for variadic functions for the rest of the query
Only add to result if prefix = entire function for non-variadic functions 
"""


# this class is what we need to implement in the interview
class FunctionLibrary:

	def register(self, functionset):
		"""
		given a list of function
		"""
		self.functions = defaultdict(list)
		for f in functionset:
			self.functions[str(f)].append(f)


	def findMatches(self, argtypes):
		"""
		given a list of string as argument types, find all
		the plausible function
		"""
		results = []
		prefix = ''
		for i, argtype in enumerate(argtypes):
			if not prefix:
				prefix += argtype
			else:
				prefix = prefix + '.' + argtype
			candidates = self.functions[prefix]
			for c in candidates:
				if not c.is_variadic and i == len(argtypes) - 1:
					results.append(c)
				elif c.is_variadic and len(c.argtypes) != len(argtypes):
					diff = len(argtypes) - len(c.argtypes)
					temp = '.'.join([c.argtypes[-1]] * diff)
					complete = prefix + '.' + temp
					if complete == '.'.join(argtypes):
						results.append(c)
				elif c.is_variadic and len(c.argtypes) == len(argtypes):
					results.append(c)
		return results

def main():
	funca = Function('a', ['string', 'integer', 'integer'], False)
	funcb = Function('b', ['string', 'integer'], True)
	funcc = Function('c', ['integer'], True)
	funcd = Function('d', ['integer'], False)
	lib = FunctionLibrary()
	lib.register([funca, funcb, funcc, funcd])

	# find match
	result = lib.findMatches(['integer'])
	for f in result:
		print (f.name, end = '') # prints function c and d
	print()
	result = lib.findMatches(['string', 'integer', 'integer', 'integer'])
	for f in result:
		print (f.name, end = '') # prints function b
	print ()

main()