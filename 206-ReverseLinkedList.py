"""
206. Reverse Linked List
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        nextNode = None
        while temp is not None:
            node = ListNode(temp.val)
            node.next = nextNode
            nextNode = node
            temp = temp.next
        
        return nextNode
        