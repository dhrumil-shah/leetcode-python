class Solution:
    def findMedianByAdding(self, nums: List[int]) -> float:
        median = 0.0
        for e in nums:
            median += e
        return median / len(nums)
    
    def findMedian(self, nums: List[int]) -> float:
        if (len(nums) ==1):
            return nums[0]
        elif (len(nums) == 2):
            return (nums[0]+nums[1])/2
        else:
            halfMark = int(len(nums)/2)
            return ((self.findMedian(nums[:halfMark]) + self.findMedian(nums[halfMark:])))/2
            
    def findTotal(self, nums: List[int]) -> float:
        total = 0
        if (len(nums) ==1):
            total =  nums[0]
        elif (len(nums) == 2):
            total =  (nums[0]+nums[1])
        else:
            halfMark = int(len(nums)/2)
            total =  self.findTotal(nums[:halfMark]) + self.findTotal(nums[halfMark:])
        return total
        
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         median1 = None
#         median2 = None
#         if (len(nums1) > 0):
#             median1 = self.findMedian(nums1)
#         if (len(nums2) > 0 ):
#             median2 = self.findMedian(nums2)
        
#         print(median1)
#         print(median2)
#         if (median1 is None and median2 is None):
#             print("both lists are empty")
#             return 0
#         elif(median1 is None):
#             return median2
#         elif (median2 is None):
#             return median1
#         else:
#             return (median1 + median2) /2
        len1 = len(nums1)
        len2 = len(nums2)
        totalElem = len1 + len2
        sortedList = []
        i = 0
        j = 0
        while (i < len1 and j < len2):
            if (nums1[i] <= nums2[j]):
                print("loop1 - nums1", nums1[i])
                sortedList.append(nums1[i])
                i +=1
            else:
                print("loop1 = nums2 ", nums2[j])
                sortedList.append(nums2[j])
                j +=1
        
        while(i < len1):
            print("loop2 - nums1 ", nums1[i])
            sortedList.append(nums1[i])
            i +=1
        
        while (j < len2):
            print("loop3 - nums2 ", nums2[j])
            sortedList.append(nums2[j])            
            j +=1  
            
        # nums1.extend(nums2)
        # nums1.sort()
        # length = len(totalElem)
        halfMark = int(totalElem/2)
        if (totalElem % 2 == 0):
            print(sortedList)
            return (sortedList[halfMark-1]+sortedList[halfMark])/2
        else:
            # halfMark = int(sortedList/2)
            return sortedList[halfMark]
        # return self.findTotal(nums1) / totalElem