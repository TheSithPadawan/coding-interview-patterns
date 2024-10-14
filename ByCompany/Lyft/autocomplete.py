# lc link: https://leetcode.com/problems/design-search-autocomplete-system/
class TrieNode:
    def __init__(self, val=None):
        self.val = val
        self.children = dict()
        self.count = 0
        self.end = False
    
    def __str__(self) -> str:
        return f"Node({self.val}, end={self.end})"

class AutocompleteSystem:
    def __init__(self, sentences, times) -> None:
        self.root = TrieNode()
        self.buildtrie(sentences, times)
        self.prefix = ''

    def input(self, c: str):
        result = []
        if c == '#':
            self.insert(self.root, self.prefix, 1)
            self.prefix = ''
            return []
        else:
            self.prefix += c
            node = self.root
            for ch in self.prefix:
                if ch not in node.children:
                    return result
                node = node.children[ch]
            # dfs from node
            self.dfs(node, self.prefix, result)
            result.sort(key=lambda x: (-x[0], x[1]))
            result = [x[1] for x in result]
            return result[:3]

    def buildtrie(self, sentences, times):
        for i, s in enumerate(sentences):
            self.insert(self.root, s, times[i])
        
    def insert(self, node, s, freq):
        # print('adding word', s, 'to trie')
        for ch in s:
            if ch not in node.children:
                node.children[ch] = TrieNode(ch)
            node = node.children[ch]
        # mark the end of word
        node.end = True
        node.count = freq
    
    def dfs(self, node, prefix, result):
        if not node:
            return
        if node.end:
            result.append((node.count, prefix))
        for c in node.children.keys():
            self.dfs(node.children[c], prefix + c, result)

if __name__ == '__main__':
    sentences = ["i love you", "island", "iroman", "i love leetcode"]
    times = [5, 3, 2, 2]
    autocomplete = AutocompleteSystem(sentences, times)
    print(autocomplete.input('i'))