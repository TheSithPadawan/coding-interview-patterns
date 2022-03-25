"""
lc link: https://leetcode.com/problems/basic-calculator-ii/
no stack version, adapted from stack version
please refer to the stack version first, as it is easier to understand
in no stack version, last is basically the top of stack
"""
class Solution:
    def calculate(self, s: str) -> int:
        # acc is the accumulation of results, last is the top of stack element
        acc, last = 0, 0
        def update(sign, num):
            nonlocal acc, last
            if sign == '+':
                acc += last
                last = num
            elif sign == '-':
                acc += last
                last = -num
            elif sign == '*':
                last *= num
            elif sign == '/':
                last = int(last / num)
                
        num, sign = 0, '+'
        for it, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in '+-*/':
                update(sign, num)
                num, sign = 0, c
        update(sign, num)
        acc += last
        return acc