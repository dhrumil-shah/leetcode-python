class Solution:        
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for index in range(len(nums)):
            if (nums[index] != val):
                nums[i] = nums[index]
                i +=1
        return i
        
    def runtests(self):
        print (self.removeElement([1], 1) == 0)
        print (self.removeElement([2,2], 2) == 0)
        print(self.removeElement([2,2,2,2,2], 2) ==0)
        print (self.removeElement([2,2,3], 2) == 1)
        print(self.removeElement([1,2,3,4,5], 5) ==4)
        
        print(self.removeElement([3,2,2,3], 3) ==2)
        print(self.removeElement([0,1,2,2,3,0,4,2], 2) ==5)
        print(self.removeElement([0,1,2,2,3,0,4,2], 9) ==8)
        print(self.removeElement([2,0,1,2,2,3,0,4,2], 2) ==5)
        
        
sol = Solution()
sol.runtests()