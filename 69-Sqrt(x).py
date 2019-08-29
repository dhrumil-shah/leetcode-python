import math
class Solution:
    def mySqrt(self, x: int) -> int:
        return math.floor(self.findSqrt(0, x, x))
    
    def findSqrt(self, start: float, end: float, x: int) -> float:
        if (end == 1 or end ==0):
            return end
        mid = (start+end)/2        
        square = mid* mid
        if int(round(square,6)) == round(x,6):
            return mid
        elif (square > x):
            return self.findSqrt(start, mid,x)
        else:
            return self.findSqrt(mid, end, x)
    
    def runtests(self):
        if (self.mySqrt(1) ==1 and self.mySqrt(0) ==0 and self.mySqrt(8) ==2 and self.mySqrt(100) ==10 \
           and self.mySqrt(9) ==3 and self.mySqrt(16) ==4):
            print(True)
        else:
            print(False)
                
sol = Solution()
sol.runtests()