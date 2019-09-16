"""
8. String to Integer (atoi)
"""
class Solution:    
    digitDict = {'1':1,
                    '2': 2,
                     '3':3,
                     '4':4,
                    '5':5,
                     '6':6,
                     '7':7,
                     '8':8,
                     '9':9,
                     '0':0                     
                }
    
    def myAtoi(self, str: str) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        i = 0
        start = 0
        negative = False
        
        str = str.strip()
        length = len(str)
        if (length < 1):
            return 0
        intStr = []
        valid = ['-', '1','2','3','4','5','6','7','8','9','0']
        # if str[0] not in valid:
        #     return 0
        if str[0] == '-':
            negative = True
            start = 1
        if str[0] == '+':
            start = 1
        
        for index in range(start,length):
            if (str[index] in valid[1:]):
                # print(str[index])
                intStr.append(str[index])
            else:
                break
        # print("".join(intStr))
        power = 0
        for item in intStr[::-1]:
            i += self.digitDict[item] * (10**power)
            power +=1
        
        if negative:
            i *= -1
        if i in range(INT_MIN, INT_MAX):
            return i
        if negative:
            return INT_MIN        
        else:
            return INT_MAX
        
    def runtest(self):
        if (self.myAtoi("42") == 42 \
            and self.myAtoi("") == 0 \
            and self.myAtoi("+") == 0 \
            and self.myAtoi("+1") == 1 \
            and self.myAtoi("-") == 0 \
            and self.myAtoi(" ") == 0 \
            and self.myAtoi("words and 987") == 0 \
            and self.myAtoi("-91283472332") == -2147483648 \
            and self.myAtoi("91283472332") == 2147483647 \
            and self.myAtoi("-2147483649") == -2147483648 \
            and self.myAtoi("2147483648") == 2147483647 \
            and self.myAtoi("4193 with words") == 4193 \
            and self.myAtoi("-4193 with words") == -4193 \
            and self.myAtoi("          -42 with words") == -42 \
            and self.myAtoi("          4w2 words") == 4 \
            and self.myAtoi("          -4w2 words    ") == -4 \
            and self.myAtoi("          -4   ") == -4 \
            and self.myAtoi("          -4-2 words    ") == -4 \
            and self.myAtoi("          -words    ") == 0 \
            and self.myAtoi("          - words    ") == 0 \
           ):
            print(True)
        else:
            print(False)
            

sol = Solution()
sol.runtest()