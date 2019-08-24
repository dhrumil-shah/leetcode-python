class Solution:    
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len, haystack_len = len(needle), len(haystack)
        if (needle_len == 0):
            return 0
        if (needle_len > haystack_len):
            return -1
        i = 0
        for i in range(haystack_len):
            if (haystack[i:i+needle_len] == needle) :
                return i
        return -1
    
    def runtests(self):
        if (self.strStr("hello", "h") ==0 and \
            self.strStr("aaaaa", "bba") == -1 and \
            self.strStr("aa","a") == 0 and \
            self.strStr("hello", "o") == 4 and \
            self.strStr("hellolly", "lly") == 5 and \
            self.strStr("mississippi", "issipi") == -1 and \
            self.strStr("mississippi", "issip") == 4 and \
            self.strStr("hello", "ll") ==2 ) \
        :
            print(True)
        else:
            print(False)

sol = Solution()
sol.runtests()