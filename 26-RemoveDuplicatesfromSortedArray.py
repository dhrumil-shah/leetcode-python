class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:        
        
        length = len(nums)
        i = 0
        # for index in range(length):
        j = i + 1
        for j in range(j, length):
            if (nums[i] == nums[j]):
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
            
        return i+1
    
    def runtests(self):
        print (self.removeDuplicates([1,1,2]) == 2)
        print (self.removeDuplicates([1,1,2,2,2]) == 2)
        print (self.removeDuplicates([1]) == 1)
        print (self.removeDuplicates([1,1]) == 1)
        print (self.removeDuplicates([1,1,1]) == 1)
        print (self.removeDuplicates([1,1,1,2]) == 2)
        print (self.removeDuplicates ([0,0,1,1,1,2,2,3,3,4]) ==5)
        
sol = Solution()
sol.runtests()