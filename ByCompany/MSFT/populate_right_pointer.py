"""
lc link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

This is an easy question, however in MSFT interviews, they like to ask you to
implement it without using the queue for BFS.

The way to go would be to link the next level tree nodes while on current level.
Basically a linked list problem
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        node = root
        next_level_head = Node()
        next_level_itr = next_level_head
        while node:
            if node.left:
                next_level_itr.next = node.left
                next_level_itr = next_level_itr.next
            if node.right:
                next_level_itr.next = node.right
                next_level_itr = next_level_itr.next
            
            node = node.next
            if not node:
                node = next_level_head.next
                next_level_head = Node()
                next_level_itr = next_level_head
        return root
