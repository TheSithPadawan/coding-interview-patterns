"""
top Meta question
lc link: https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            head = Node(insertVal)
            head.next = head
            return head
        
        # case 1. find the gap to insert the value prev.val <= insertVal <= cur.val 
        # case 2. insert value is out of maximum or minimum 
        # case 3. everyone in the list is equal 
        
        prev, cur = head, head.next
        insert = False
        while True:
            if prev.val <= insertVal and insertVal <= cur.val:
                insert = True
            elif prev.val > cur.val and (insertVal >= prev.val or insertVal <= cur.val):
                insert = True
            
            if insert:
                prev.next = Node(insertVal, cur)
                return head
            
            # advance 
            prev = cur
            cur = cur.next 
            
            if prev == head: # completed one round
                break
        
        # case3. everywhere is equal
        prev.next = Node(insertVal, cur)
        return head