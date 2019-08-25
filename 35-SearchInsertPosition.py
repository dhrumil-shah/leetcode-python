# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 19:11:38 2019

@author: dhrumil-shah
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)
        for i in range(length):
            if (target <= nums[i]):
                return i
        if (i == length-1):
            return length
        return i
    def runtests(self):
        if (self.searchInsert([1,3,5,6], 5) == 2 \
           and self.searchInsert([1,3,5,6], 0) ==0 \
            and self.searchInsert([1,3,5,6], 1) ==0 \
            and self.searchInsert([1,3,5,6], 7) ==4 \
            and self.searchInsert([1,3,5,6], 6) ==3 \
           and self.searchInsert([1,3,5,6], 2) ==1):
            print(True)
        else:
            print(False)

sol = Solution()
sol.runtests()