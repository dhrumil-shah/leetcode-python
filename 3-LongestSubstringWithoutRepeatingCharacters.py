# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 18:55:48 2019

@author: dhrumil-shah
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        arr = []
        longest = 0
        for i in range(length):
            arr.append(s[i])
            for j in range(i+1, length):
                if (s[j] in arr):
                    if (len(arr) >= longest):
                        longest = len(arr)
                    arr = []
                    break
                else:
                    arr.append(s[j])
            if (len(arr) >= longest):
                longest = len(arr)
            arr = []
        
        if (len(arr) >= longest):
            longest = len(arr)
        return len(arr) if (longest == 0) else longest                    
                
            
    def lengthOfLongestSubstring_optimized(self, s: str) -> int:
        maxlen = 0
        currentlen = 0
        indHash = {}
        leftside = -1
        ls = len(s)
        for ind, ch in enumerate(s):
            if (ch in indHash) and (leftside < indHash[ch]):
                leftside = indHash[ch];
            currentlen = ind - leftside;
            if currentlen > maxlen:
                maxlen = currentlen
            indHash[ch] = ind
        currentlen = ls - leftside - 1
        if currentlen > maxlen:
            maxlen = currentlen
        return maxlen        
    
    def runtests(self):
        if (self.lengthOfLongestSubstring("") == 0 \
           and self.lengthOfLongestSubstring("abcabcbb") == 3 \
            and self.lengthOfLongestSubstring("abcabcdbb") == 4 \
            and self.lengthOfLongestSubstring(" ") == 1 \
            and self.lengthOfLongestSubstring("a") == 1 \
            and self.lengthOfLongestSubstring("ab") == 2 \
            and self.lengthOfLongestSubstring("aa") == 1 \
            and self.lengthOfLongestSubstring("aab") == 2 \
            and self.lengthOfLongestSubstring("bbbb") == 1 \
            and self.lengthOfLongestSubstring("pwwkew") == 3 \
            and self.lengthOfLongestSubstring("dvdf") == 3 \
            and self.lengthOfLongestSubstring("abad") == 3 \
           ):
            print(True)
        else:
            print(False)
        
sol = Solution()
sol.runtests()