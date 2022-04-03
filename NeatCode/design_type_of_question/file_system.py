"""
top amazon question

lc link: https://leetcode.com/problems/design-in-memory-file-system/

Use Trie data structure
"""

class FileObject:
    def __init__(self, path=None):
        self.path = path
        # handles subdirectories
        self.children = dict()
        self.is_file = False
        self.contents = []

class FileSystem:

    def __init__(self):
        self.rootdir = FileObject()

    def ls(self, path: str) -> List[str]:
        paths = path.split('/')
        itr = self.rootdir
        for p in paths:
            if not p:
                continue
            itr = itr.children[p]
        if itr.is_file:
            return [itr.path]
        return sorted(itr.children.keys())
        

    def mkdir(self, path: str) -> None:
        paths = path.split('/')
        itr = self.rootdir
        for p in paths:
            if not p:
                continue
            if p not in itr.children:
                itr.children[p] = FileObject(p)
            itr = itr.children[p]

    def addContentToFile(self, filePath: str, content: str) -> None:
        # if filepath does not exist, create
        paths = filePath.split('/')
        itr = self.rootdir
        for p in paths:
            if not p:
                continue
            if p not in itr.children:
                itr.children[p] = FileObject(p)
            itr = itr.children[p]
        itr.is_file = True
        itr.contents.append(content)

    def readContentFromFile(self, filePath: str) -> str:
        cur = self.rootdir
        path = filePath.split('/')
        for p in path:
            if not p:
                continue
            cur = cur.children[p]
        return ''.join(cur.contents)


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)