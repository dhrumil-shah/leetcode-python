"""
19. Remove Nth Node From End of List 
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nodeArray = []
        node = head
        while (node is not None):
            nodeArray.append(node)
            node = node.next
        
        length = len(nodeArray)
        if (n == length):
            return head.next
        prevNode = nodeArray[length-(n+1)] 
        if (n>1):
            nextNode= nodeArray[length-(n-1)]
            prevNode.next = nextNode
        else:
            prevNode.next = None

        return head
            