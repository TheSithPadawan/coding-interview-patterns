"""
Problem 2: read 4
lc link: https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/
"""

# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.end = False
        self.pos = 0
        self.buf4 = [''] * 4
        self.available = 0

    def read(self, buf: List[str], n: int) -> int:
        chars_read = 0
        # first clear everything from existing stream 
        i = 0
        while self.pos < self.available and chars_read < n:
            buf[i] = self.buf4[self.pos]
            self.pos += 1
            i += 1
            chars_read += 1

        while chars_read < n and not self.end:
            self.buf4 = [''] * 4
            self.available = read4(self.buf4)
            self.pos = 0
            if not self.available:
                self.end = True
            for j in range(self.available):
                buf[i] = self.buf4[self.pos]
                i += 1
                self.pos += 1
                chars_read += 1
                if chars_read == n:
                    break
        return chars_read
