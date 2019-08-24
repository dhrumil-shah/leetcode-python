class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if (len(strs) == 0 or strs is None or (strs == []) or (strs == [""])):
            return ""
        
        # prefix = strs[0][0]
        shortestWord = len(strs[0])
        for index in range(0, len(strs)):
            wordLen = len(strs[index])
            if (wordLen == 0): 
                return ""
            shortestWord = wordLen <= shortestWord and wordLen or shortestWord
            matchFound = strs[0][0] == strs[index][0]
            
            if not matchFound:
                return ""
            else:
                prefix = strs[0][0]
               
        for index in range(1,shortestWord+1):
            for j in range(len(strs)):
                if strs[0][:index] != strs[j][:index] :
                    return prefix
            prefix = strs[0][:index]

        return prefix
        
    def runtests(self):
        if (self.longestCommonPrefix(['f','c','f']) == "" and self.longestCommonPrefix(['flower', 'flow', 'flight'])=="fl" and self.longestCommonPrefix(['f','f','f']) == "f" and self.longestCommonPrefix(["dog","racecar","car"]) =="" and self.longestCommonPrefix(['float','flow','flowing', 'flown']) == "flo" and self.longestCommonPrefix(['fla','fl','no']) == ""  and self.longestCommonPrefix([]) =="" and self.longestCommonPrefix([""])=="" and self.longestCommonPrefix(["",""])=="" and self.longestCommonPrefix(["","something",""])=="" and self.longestCommonPrefix(["something",""])=="" and self.longestCommonPrefix(["aa","aa"])=="aa"):
            print(True)
        else:
            print(False)    
    
sol = Solution()
sol.runtests()