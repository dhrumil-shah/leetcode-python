class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        retList = [0,0]
        for i,x  in enumerate(nums):
            if (target-x) in nums[:i]:
                retList[1] = i
            if (target-x) in nums[i+1:]:
                retList[0] = i 
                #        aux = [i for i,x in enumerate(nums) if ((target - x) in nums[:i] or (target - x) in nums[i+1:])]
        #return [aux[0], aux[1]]
        
        return retList
        
        