class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        # case 1. node has right child, successor somewhere lower in the right sub tree
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        # case 2. node has no right child, successor somewhere upper in the tree
        # go up until the node is the left child of its parent
        while node.parent and node.val > node.parent.val:
            node = node.parent
        return node.parent

# lc link: https://leetcode.com/problems/inorder-successor-in-bst-ii/
