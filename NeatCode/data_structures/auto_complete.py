"""
lc link: https://leetcode.com/problems/design-search-autocomplete-system/
Ultimate Trie Problem: Design Auto Complete System
"""

class Node:
    
    def __init__(self, rank, prefix):
        self.rank = rank
        self.word = prefix
    
    def __lt__(self, other):
        """
        lt returns True or False. True if self is < other
        """
        if self.rank != other.rank:
            return self.rank > other.rank
        return self.word < other.word
    
class TrieNode:
    def __init__(self, val=None):
        self.val = val
        self.children = dict()
        self.rank = 0
        self.is_word = False

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.prefix = ''
        for i, s in enumerate(sentences):
            self.insert(self.root, s, times[i])
        
    def input(self, c: str) -> List[str]:
        result, maxheap = [], []
        if c != '#':
            self.prefix += c
            node = self.root
            for c in self.prefix:
                if c not in node.children:
                    return result
                node = node.children[c]
            self.dfs(node, self.prefix, maxheap)
        else:
            self.insert(self.root, self.prefix, 1)
            self.prefix = ''
            return []
        for i in range(min(3, len(maxheap))):  
            s = heapq.heappop(maxheap)          
            result.append(s.word)
        return result
    
    def dfs(self, node, prefix, maxheap):
        if not node:
            return
        if node.is_word:
            heapq.heappush(maxheap, Node(node.rank, prefix))
        for c in node.children:
            self.dfs(node.children[c], prefix + c, maxheap)
    
    def insert(self, node, word, rank):
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode(c)
            node = node.children[c]
        node.is_word = True
        node.rank += rank