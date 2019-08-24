# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carryOver = 0
        l = None
        List1Over = False
        List2Over = False
        node = None
        while True:
            num1 = 0
            num2 = 0
            if (l1 is not None ):
                # num1 = num1*10 + l1.val
                num1 = l1.val
            if (l2 is not None ):
                # num2 = num2*10 + l2.val
                num2 = l2.val

            num = num1 + num2 + carryOver
            if (num ==0 and carryOver !=0):
                num = carryOver
            if (num >= 10):
                carryOver = 1 #if (num - 10 == 0) else num-10
                num = num-10
            else:
                carryOver = 0
            newNode = ListNode(num)
            newNode.next = None
            if (l is None):
                l = newNode                
                node = l
            else:                
                node.next = newNode
                node = newNode
            l1 = l1.next if (l1 is not None) else None
            if (l1 is None):
                List1Over = True
            l2 = l2.next if (l2 is not None) else None
            if (l2 is None):
                List2Over = True
            if (List1Over and List2Over and carryOver == 0):
                break
        return l