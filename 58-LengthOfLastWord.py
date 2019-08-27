class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # return len(s.strip().split(' ')[-1])
        s = s.strip()
        i = len(s)-1
        count = 0
        while i > -1 and s[i] != ' ':
                count+=1
                i-=1 
        return count