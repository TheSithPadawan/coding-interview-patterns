"""
lc: https://leetcode.com/problems/integer-to-roman/
Easy idea to think about during an interview:
write a recursive function to compute

For example the number is 58, how did we arrive at: LVIII?
Current number      Result
58 [- 50] = 8         L
8 [- 5] = 3           LV
3 - 3 = 0             LVIII
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        if num == 0:
                return ''
        if num < 5:
            if num == 4:
                return 'IV' # special case
            else:
                return 'I' + self.intToRoman(num - 1)
        elif num < 10:
            if num == 9: 
                return 'IX' # special case
            else:
                return 'V' + self.intToRoman(num - 5)
        elif num < 50:
            if num < 40:
                return 'X' + self.intToRoman(num - 10)
            else:
                return 'XL' + self.intToRoman(num - 40)
        elif num < 100:
            if num < 90:
                return 'L' + self.intToRoman(num - 50)
            else:
                return 'XC' + self.intToRoman(num - 90)
        elif num < 500:
            if num < 400:
                return 'C' + self.intToRoman(num - 100)
            else:
                return 'CD' + self.intToRoman(num - 400)
        elif num < 1000:
            if num < 900:
                return 'D' + self.intToRoman(num - 500)
            else:
                return 'CM' + self.intToRoman(num - 900)
        else:
            return 'M' + self.intToRoman(num - 1000)