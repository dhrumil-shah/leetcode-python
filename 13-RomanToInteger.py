class Solution:
    def romanToInt(self, s: str) -> int:
#         check prior char for 
# if V or X, L or C, D or M
        i = len(s)-1
        total = 0
        while (i >= 0):
            # print(total, i, s[i])
            if (s[i] == "I"):
                count = 1
                i -=1
                while (s[i] == "I" and i >= 0):
                    i -=1
                    count +=1
                total += count
            elif(s[i] == "V"):
                value = 5
                if(s[i-1] == "I" and i-1 >= 0):
                    value = 4
                    i -=1
                total += value
                i -=1
            elif(s[i] == "X"):
                value = 10
                if(s[i-1] == "I"and i-1 >= 0):
                    value = 9
                    i -= 1
                total += value
                i -=1
            elif(s[i] == "L"):
                value = 50
                if(s[i-1] == "X"and i-1 >= 0):
                    value = 40
                    i -= 1
                total += value
                i -=1
            elif(s[i] == "C"):
                value = 100
                if(s[i-1] == "X" and i-1 >= 0):
                    value = 90
                    i -= 1
                total +=value
                i -=1
            elif(s[i] == "D"):
                value = 500
                if(s[i-1] == "C" and i-1 >= 0):
                    value = 400
                    i -= 1
                total +=value
                i -=1
            elif(s[i] == "M"):
                value = 1000
                if(s[i-1] == "C" and i-1 >= 0):
                    value = 900
                    i -= 1
                total +=value
                i -=1                
        return total
            
    def runtests(self):
        if (self.romanToInt("VIII") == 8 and self.romanToInt("LVIII") == 58 and self.romanToInt("I") == 1             and self.romanToInt("II") == 2             and self.romanToInt("III") == 3             and self.romanToInt("IV") == 4             and self.romanToInt("V") == 5             and self.romanToInt("IX") == 9             and self.romanToInt("L") == 50             and self.romanToInt("XL") == 40             and self.romanToInt("C") == 100             and self.romanToInt("XC") == 90             and self.romanToInt("MCMXCIV") == 1994             and self.romanToInt("MMCMXCIV") == 2994 and self.romanToInt("MMMCMXCIV") == 3994 and self.romanToInt("MMMCMXCIX") == 3999) :
            print(True)
        else:
            print(False)
        
        
        
sol = Solution()
sol.runtests()