"""
137. Single Number II
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return int((3 * sum(set(nums)) - sum(nums))/2)
    
    def runtests(self):
        if (self.singleNumber([2,2,3,2]) == 3 \
           and self.singleNumber([0,1,0,1,0,1,99]) == 99 \
           and self.singleNumber([]) == 0 \
           ):
            print(True)
        else:
            print(False)
            
sol = Solution()
sol.runtests()