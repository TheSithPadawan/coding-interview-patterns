"""
lc: https://leetcode.com/problems/basic-calculator-ii/
top question for fb and msft

key idea:
there is a [delay] in evaluation
when we see a number, update the number 
when we see an operator, update the stack for results. 
This update refers to updating the recorded operator (previous sign) and previous number

This template can be easily adapted to evaluating expressions with () by adding recursion
"""

class Solution:
    def calculate(self, s: str) -> int:
        def update(sign, val):
            if sign == '+':
                st.append(val)
            elif sign == '-':
                st.append(-val)
            elif sign == '*':
                st.append(st.pop(-1) * val)
            else: 
                st.append(int(st.pop(-1) / val))
        st, it, num, sign = [], 0, 0, '+'
        while it < len(s):
            if s[it].isdigit():
                num = num * 10 + int(s[it])
            elif s[it] in '+-*/':
                update(sign, num)
                sign, num = s[it], 0
            it += 1
        update(sign, num)
        # print (st)
        return sum(st)