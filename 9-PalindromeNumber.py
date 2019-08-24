class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0):
            return False
        
        q = x
        ret = []
        while q != 0:
            q, r = divmod(q, 10) # Divide by 10, see the remainder
            ret.insert(0, r) # The remainder is the first to the right digit
        begin = 0
        end = len(ret)-1
        while True:
            if (begin >= end):
                break
            if (ret[begin] != ret[end]):
                return False
            begin += 1
            end -= 1            
        return True