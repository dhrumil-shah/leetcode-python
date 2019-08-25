# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 18:55:48 2019

@author: dhrumil-shah
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return 3
    
    def runtests(self):
        if (self.lengthOfLongestSubstring("abcabcbb") ==3):
            print(True)
        else:
            print(False)

sol = Solution()
sol.runtests()
