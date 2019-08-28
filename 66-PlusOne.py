class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = digits[-1]
        if (num +1 < 10):
            digits[-1] = num+1
        else:
            i = len(digits)-1
            carryOver = 0
            while (i >= 0):
                num = digits[i] + 1
                if num < 10:
                    digits[i] = num
                    carryOver = 0
                else:
                    digits[i] = num -10
                    carryOver = 1
                if carryOver ==0:
                    break
                if (i ==0 and carryOver ==1):
                    digits.insert(i,digits[i]+ carryOver)
                i -=1
        return digits
    
    def runtests(self):
        if (self.plusOne([9]) ==[1,0] and self.plusOne([0]) == [1] and self.plusOne([1,0]) == [1,1] \
           and self.plusOne([9,9]) == [1,0,0] and self.plusOne([9,9,9]) == [1,0,0,0] \
           and self.plusOne([9]) == [1,0] and self.plusOne([1,2,3]) == [1,2,4] \
           and self.plusOne([4,3,2,1]) == [4,3,2,2] and self.plusOne([2,4,9,3,9]) ==[2,4,9,4,0] \
           and self.plusOne([4,3,9,9]) == [4,4,0,0]):
            print(True)
        else:
            print(False)
            
sol = Solution()
sol.runtests()