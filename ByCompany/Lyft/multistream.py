"""
已知有一个Stream类，有一个function是ReadN(int n)。设计一个MultiStream类，需要实现三个功能，增加一个Stream，删除一个Stream，以及ReadN(int n)

# Suppose you are given a stream interface that works as follows: 
class Stream:
    def read(self, n:int) -> list[int]:
        pass
    You can call `read()` on the stream and it will return up to `n` ints as an array. 
    It's possible the call will return fewer than `n` values, 
    in which case the stream of data has been consumed completely.

Task:
Create a new class called `MultiStream` which can store other streams and has a `read()` method that is backed by other streams. 
Treat `Stream` objects like black boxes - you cannot change their implementation. Implement add(stream),read(n),remove(stream)

Example:
ms = MultiStream()
s1 = Stream(...)
s2 = Stream(...)
ms.add(s1) # first stream contents: [5, 4, 1, 4, 5]
ms.add(s2) # second stream contents: [1, 3]
ms.read(6) returns [5, 4, 1, 4, 5, 1]
ms.remove(s2) # remove [3]
ms.read(2): returns [] exhausted
ms.read(5): returns [] exhausted

Idea: 用linkedlist node来维持stream  
add(stream): adjust pointer to add the current node to linked list
read(n): read from current node to n char, call read function in the stream
remove(stream): update the prev_ and next_ pointer and file to node dict
"""
from collections import deque


READ_CHAR = 10

class Stream:
    def __init__(self, string):
        self.s = string
        self.i = 0

    def read(self, n):
        if self.i >= len(self.s):
            return ""
        ans = self.s[self.i:(self.i+n)]
        self.i += n
        return ans
    
    def __eq__(self, other):
        return self.s == other.s

    def __hash__(self) -> int:
        return hash(self.s)

class StreamNode:
    def __init__(self, stream):
        self.contents = []
        self.prev_ = None
        self.next_ = None
        # Stream object
        self.stream = stream


class MultiStream:
    def __init__(self):
        self.head = StreamNode(None)
        self.tail = StreamNode(None)
        # mapping from stream name -> stream node
        self.nodes = dict()
        self.head.next_ = self.tail
        self.tail.prev_ = self.head
        self.current_node = None
    
    def add(self, s):
        node = StreamNode(s)
        node.stream = s
        # add to linked list
        self.tail.prev_.next_ = node
        node.prev_ = self.tail.prev_
        node.next_ = self.tail
        self.tail.prev_ = node
        self.nodes[s] = node
    
    def remove(self, s):
        if s not in self.nodes:
            return
        node = self.nodes[s]
        if self.current_node == node:
            self.current_node = node.next_
        node.prev_.next_ = node.next_
        node.next_.prev_ = node.prev_
        node.next_, node.prev_ = None, None
        self.nodes.pop(s)
    
    def read(self, n):
        chars_read = 0
        p = self.head.next_ if not self.current_node else self.current_node
        # go to each stream node and read contents
        output = []
        while len(output) < n and p.stream:
            cur = p.stream.read(n - len(output))
            output += cur
            if len(output) == n:
                return output
            p = p.next_
        return output

if __name__ == '__main__':
    f1 = Stream('12345')
    f2 = Stream('13')
    ms = MultiStream()
    ms.add(f1)
    ms.add(f2)
    print(ms.read(4))
    print(ms.read(2))
    ms.remove(f2)
    print(ms.read(5))