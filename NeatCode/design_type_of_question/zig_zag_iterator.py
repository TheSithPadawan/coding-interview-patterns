"""
lc link: https://leetcode.com/problems/zigzag-iterator/

Flex time: Runtime: 48 ms, faster than 96.22% of Python3 online submissions for Zigzag Iterator.

Also added code for that below. I don't recommend py users to use
generators for this question, as in the interview the person might not
understand generators well.

Common follow up of this question:
How to extend when you have k lists?
See zig_zag_k.py for merge k pattern
"""

class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.queue = []
        self.l1 = v1
        self.l2 = v2
        self.i = 0
        self.j = 0
        self.init_queue()

    def next(self) -> int:
        ans = self.queue.pop(0)
        self.init_queue()
        return ans

    def hasNext(self) -> bool:
        return len(self.queue) > 0
    
    def init_queue(self):
        if self.i < len(self.l1):
            self.queue.append(self.l1[self.i])
            self.i += 1
        if self.j < len(self.l2):
            self.queue.append(self.l2[self.j])
            self.j += 1