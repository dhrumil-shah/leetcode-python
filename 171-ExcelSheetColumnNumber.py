"""
171. Excel Sheet Column Number
"""
class Solution:
    def titleToNumber(self, s: str) -> int:
        length = len(s)-1
        number = 0
        base = 26
        for i in range(len(s)-1, -1, -1):
            number += ((base**(length-i))*(ord(s[i])-64))
        
        return number