"""
70. Climbing Stairs : interesting fibonacci series questions
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if (n ==1):
            return 1
        
        first = 1
        second = 2
        for i in range(3,n+1):
            third = first + second
            first = second
            second = third
        
        return second
    
    def climbStairs_memo(self, n: int) -> int:
        memo = [0]* n+1
        return self.climb_stairs(0, n, memo)
    
    def climb_stairs(self, i: int, n: int, memo = []) -> int:
        return 0