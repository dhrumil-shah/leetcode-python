"""
202. Happy Number
"""
class Solution:
"""
    is_seen = []
    def isHappy(self, n)-> bool:
        """
        :type n: int
        :rtype: bool
        """
        if n == 1: 
            return True        
        if n in self.is_seen:
            return False
        self.is_seen.append(n)
        t = n
        total = 0
        while (t):
            total += (t%10)**2
            t = int(t/10)
        print(total)
        return self.isHappy(total)
"""
     def isHappy(self, n: int) -> bool:
         arr = []        
         while n != 1:
             if n in arr: return False
             arr.append(n)
             n = sum([int(i)**2 for i in str(n)])
        
         return True
        