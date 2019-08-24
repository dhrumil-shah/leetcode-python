# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        mergedListNode = None
        startNode = None
        if (l1 is None):
            return l2
        if (l2 is None):
            return l1
        while (l1 is not None and l2 is not None):
            if (l1.val <= l2.val):
                node = ListNode(l1.val)
                # print(node)
                l1 = l1.next
            else:
                node = ListNode(l2.val)
                # print(node)
                l2 = l2.next
            if (mergedListNode is None):
                mergedListNode = node
                startNode = mergedListNode
            else:
                mergedListNode.next = node
                mergedListNode = node
        
        while (l1 is not None):
                node = ListNode(l1.val)
                # print(node)
                l1 = l1.next
                mergedListNode.next = node
                mergedListNode = node

        while (l2 is not None):
                node = ListNode(l2.val)
                # print(node)
                l2 = l2.next
                mergedListNode.next = node
                mergedListNode = node
               
        # print(startNode)
        return startNode