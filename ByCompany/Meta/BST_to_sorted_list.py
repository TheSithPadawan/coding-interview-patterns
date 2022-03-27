"""
Commonly asked meta question
lc link: https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/
Question type: data structure

Template used: BST iterative traversal with prev pointer
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        head = Node(-1)
        
        stack = []
        prev = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            top = None
            if stack:
                top = stack.pop()
            if top and not head.right:
                head.right = top
            
            if prev:
                prev.right = top
                top.left = prev
            if top:
                prev = top
            
            if top and top.right:
                root = top.right
    
        # connect head to tail
        prev.right = head.right 
        head.right.left = prev
        return head.right