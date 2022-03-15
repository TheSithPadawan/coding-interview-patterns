# Trie Search Pattern
#tree
#datastructure

Usage: prefix search
Class templates
```py
class TrieNode:
	def __init__ (self, val=None):
		self.val = val
		self.children = dict()
		# the following properties can be modified or added
		self.is_word = False
		self.word_count = 0
		self.prefix_count = 0
```

- - - -
Trie Tree iteration pattern, given a string called word
```py
for c in word:
	if c not in cur.chilren:
		# do something for example, create a new node
		cur.children[c] = TrieNode(c)
	else:
		cur = cur.children[c]
```

- - - -
TrieTree DFS for a prefix, for example, given a prefix, find all words that have this prefix and output to result.
```py
# first use iteration to set node pointing to last char of prefix
def dfs(node, result, prefix):
    if node.is_word:
        result.append(prefix)

    for c in node.children:
        dfs(node.children[c], result, prefix + c)
```

Trie + DFS Pattern to reduce some search space. 
Example: word search II [Word Search II - LeetCode](https://leetcode.com/problems/word-search-ii/)
```py
# core code 
def dfs(board, i, j, vis, node, prefix):
        if not is_safe(board, i, j) or vis[i][j]:
            return
        
        if board[i][j] not in node.children:
            return
        
        cur = node.children[board[i][j]]
        prefix += board[i][j]
        if cur.is_word:
            self.output.add(prefix)
            cur.is_word = False
        
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        
        vis[i][j] = True

        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            self.dfs(board, nx, ny, vis, cur, prefix)
            
        vis[i][j] = False
        """
		  this optimization to delete trie node after search is not needed in an actual interview
		  """
        if len(cur.children) == 0:
            node.children.pop(board[i][j])
```

