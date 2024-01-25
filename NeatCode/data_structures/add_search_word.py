# lc link: https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self, val=None):
        self.is_word = False
        self.children = dict()
        self.val = val

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode(c)
            node = node.children[c]
        node.is_word = True

    def search(self, word: str) -> bool:
        def dfs(root, index, is_word):
            if index == len(word):
                return is_word
            if word[index] in root.children:
                return dfs(root.children[word[index]], index + 1, root.children[word[index]].is_word)
            elif word[index] == '.':
                # iterate and match
                for k in root.children.keys():
                    if dfs(root.children[k], index + 1, root.children[k].is_word):
                        return True
            return False
        return dfs(self.root, 0, False)
