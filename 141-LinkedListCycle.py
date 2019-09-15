"""
141 - Linked List Cycle
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle_lookup(self, head: ListNode) -> bool:
        if head is None:
            return False
        p1 = head
        arr = []
        while (p1):
            if (p1.next in arr):
                return True
            else:
                arr.append(p1.next)
            p1 = p1.next
        return False
    
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False
        slow = head
        fast = head.next
        while slow !=fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        
        return True