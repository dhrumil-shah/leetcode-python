class Solution:
    def reverse(self, x: int) -> int:
        if not x in (range(-2**31, 2**31-1)): 
            return 0 
        negative = False
        if (x < 0):
            x = abs(x)
            negative = True

        newNum = 0
        while (x > 0 ):
            digit = x % 10
            newNum = newNum*10 + digit
            x = x // 10

        if (negative):
            newNum *= -1

        return newNum if (newNum in range(-2**31, 2**31-1)) else 0