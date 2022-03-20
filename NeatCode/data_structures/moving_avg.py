"""
deque easy question
lc link: https://leetcode.com/problems/moving-average-from-data-stream/
"""

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.sum = 0
        self.deque = []

    def next(self, val: int) -> float:
        self.deque.append(val)
        self.sum += val
        if len(self.deque) <= self.size:
            return self.sum / len(self.deque)
        else:
            self.sum -= self.deque[0]
            self.deque.pop(0)
            return self.sum / len(self.deque)