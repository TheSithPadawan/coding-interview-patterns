"""
lc link: https://leetcode.com/problems/design-circular-queue/
idea: just use doubly linked list
also see my cpp soln, what a cheat..
"""
"""
Use doubly linked list to represent a queue
"""
class Node:
    def __init__ (self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.cap = k
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.size + 1 <= self.cap:
            node = Node (value)
            self.tail.prev.next = node
            node.prev = self.tail.prev
            node.next = self.tail
            self.tail.prev = node
            self.size += 1
            return True
        return False

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        node = self.head.next
        self.head.next = node.next
        node.next.prev = self.head
        self.size -= 1
        return True

    def Front(self) -> int:
        return self.head.next.val

    def Rear(self) -> int:
        return self.tail.prev.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.cap