"""
88. Merge Sorted Array
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        if (i < 0):
            j =0
            while(j < n):
                nums1[j] = nums2[j]
                j +=1
        else:
            while (i >=0 and j >=0):
                if (nums2[j] > nums1[i]):
                    nums1[i+j+1] = nums2[j]
                    j -=1
                else:
                    nums1[i+j+1] = nums1[i]
                    # nums1[i] = nums2[j]
                    i -=1
            while (j >=0):
                nums1[j] = nums2[j]
                j -=1