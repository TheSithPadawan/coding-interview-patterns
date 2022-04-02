"""
lc link: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

py solution, using min heap + defaultdict to summarize
"""

class Node:
    def __init__(self, treenode, x, y):
        self.treenode = treenode
        self.x = x
        self.y = y
    
    def __lt__ (self, other):
        if self.x != other.x:
            return self.x < other.x
        return self.treenode.val < other.treenode.val
    
    
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        results = []
        if not root:
            return results
        queue = [Node(root, 0, 0)]
        nodesmap = defaultdict(list)
        while queue:
            node = queue.pop(0)
            heapq.heappush(nodesmap[node.y], node)
            if node.treenode.left:
                queue.append(Node(node.treenode.left, node.x+1, node.y-1))
            if node.treenode.right:
                queue.append(Node(node.treenode.right, node.x+1, node.y+1))
        # summarize results
        keys = sorted(nodesmap.keys())
        for k in keys:
            level = []
            while nodesmap[k]:
                node = heapq.heappop(nodesmap[k])
                level.append(node.treenode.val)
            results.append(level)
        return results