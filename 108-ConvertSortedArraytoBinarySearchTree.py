"""
108. Convert Sorted Array to Binary Search Tree
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        length = len(nums)
        if length < 1: return None
        half = int(len(nums)/2)
        root = TreeNode(nums[half])
        if length == 1:
            return root
        elif length ==2:
            root.left = TreeNode(nums[0])
            return root
        elif length ==3:
            root.left = TreeNode(nums[0])
            root.right = TreeNode(nums[2])
            return root
        else:
            root.left = self.sortedArrayToBST(nums[:half])
            root.right = self.sortedArrayToBST(nums[half+1:])
        
        return root