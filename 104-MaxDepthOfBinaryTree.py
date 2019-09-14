"""
104. Maximum Depth of Binary Tree
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.preOrder(root)
    
    def preOrder(self, root: TreeNode) -> int:
        if root: 
            left = self.preOrder(root.left)
            right = self.preOrder(root.right)
            return max(left,right)+1
        else:
            return 0
        