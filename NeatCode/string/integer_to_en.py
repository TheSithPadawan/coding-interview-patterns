
"""
LC problem link: https://leetcode.com/problems/integer-to-english-words/

Idea:
process every three digits;
write a recursive function to handle three digit conversion
"""

units = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
tens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'Twenty']
more_than_twenty = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty' ,'Ninety']

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
         # handle it every three digits
        lvl = ['', 'Thousand', 'Million', 'Billion']
        index = 0
        result = ''
        while num:
            part = num % 1000
            val = self.convert_to_en(part)
            partial = ''
            if val != '':
                partial = val + ' ' + lvl[index] + ' '
            result = partial + result
            num //= 1000
            index += 1
        return result.strip()
    
    
    def convert_to_en(self, num):
        # converts three digits and below to english and return string 
        if num < 10:
            return units[num]
        if num >= 10 and num <= 20:
            return tens[num - 10]
        if num > 20 and num < 100:
            u = num % 10 
            num //= 10
            result = more_than_twenty[num] + ' ' + units[u]
            return result.strip()
        # >= 100, call recursive function
        two_digit = num % 100
        result = units[num // 100] + ' Hundred ' + self.convert_to_en(two_digit)
        return result.strip()