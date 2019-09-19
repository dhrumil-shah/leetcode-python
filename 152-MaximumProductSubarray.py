"""
152. Maximum Product Subarray
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 1: return 0
        result = nums[0]
        Max = nums[0]
        Min = nums[0]
        for i in range(1,length): 
            temp = Max
            Max = max(max(Max*nums[i], Min * nums[i]),nums[i])
            Min = min(min(Min*nums[i], temp*nums[i]), nums[i])
            
            result = max(result, Max)
        return result
    
    def runtest(self):
        if (self.maxProduct([2,3,-2,4]) == 6 \
            and self.maxProduct([0,1,-2,4]) == 4 \
            and self.maxProduct([-2,0,-1]) == 0 \
            and self.maxProduct([0]) == 0 \
            and self.maxProduct([4]) == 4 \
            and self.maxProduct([]) == 0 \
            and self.maxProduct([-1]) == -1 \
           ):
            print(True)
        else:
            print(False)
            
sol = Solution()
sol.runtest()