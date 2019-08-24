class Solution:
    def say(self, n: str) -> str:
        remaining = n                
        sayStr = ""
        prevDigit = n[0]
        count = 1
        counting = False
        for i in range(1, len(n)):
            if (prevDigit == n[i]):
                count +=1
            else:
                sayStr = sayStr + str(count) + str(prevDigit)
                prevDigit = n[i]
                count = 1
        sayStr = sayStr + str(count) + str(prevDigit)                
        return sayStr
    def countAndSay(self, n: int) -> str:
        retStr = ""
        if (n <= 1):
            return "1"
        # while (counter <= n):
        for counter in range(1,n):
            if (retStr == ""):
                retStr = str(counter)
            retStr = self.say(retStr)
            counter +=1
        
        return retStr
    
    def runtests(self):
        if (self.countAndSay(1) =="1" and self.countAndSay(2) =="11" and self.countAndSay(3) =="21" and self.countAndSay(4) =="1211" and self.countAndSay(5) =="111221" and self.countAndSay(6) =="312211" and self.countAndSay(7) =="13112221" and self.countAndSay(8) =="1113213211" and self.countAndSay(9) =="31131211131221" and self.countAndSay(12) =="3113112221232112111312211312113211"):
            print(True)
        else:
            print(False)
            
sol = Solution()
sol.runtests()