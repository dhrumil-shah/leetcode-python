"""
136. Single Number
"""
class Solution:
    def singleNumber_1(self, nums: List[int]) -> int:
        seen = set()
        for n in nums:
            if (n in seen):
                seen.remove(n)
            else:
                seen.add(n)
        
        return seen.pop()

    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)