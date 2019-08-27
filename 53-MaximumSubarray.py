import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentMax = 0
        globalMax = -sys.maxsize-1
        for i in range(len(nums)):
            currentMax += nums[i]
            
            if (currentMax > globalMax):
                globalMax = currentMax            
            
            if (currentMax < 0):
                currentMax = 0 
            
        return globalMax