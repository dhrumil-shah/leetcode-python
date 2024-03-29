"""
160. Intersection of Two Linked Lists
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode1(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if (headA is None or headB is None): return None
        if (headA == headB): return headA
        nodes = []
        nodeA = headA
        while (nodeA is not None):
            nodes.append(nodeA)
            nodeA = nodeA.next
        
        nodeB = headB
        while (nodeB is not None):
            if (nodeB in nodes):
                return nodeB
            nodeB = nodeB.next
        
        return None
    
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None

        A_pointer = headA
        B_pointer = headB

        while A_pointer != B_pointer:
            A_pointer = headB if A_pointer == None else A_pointer.next
            B_pointer = headA if B_pointer == None else B_pointer.next

        return A_pointer