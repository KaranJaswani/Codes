# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        ptr1 = headA
        ptr2 = headB
        while ptr1 != ptr2:
            if ptr1 != None:
                ptr1 = ptr1.next
            else:
                ptr1 = headB
            if ptr2 != None:
                ptr2 = ptr2.next
            else:
                ptr2 = headA

        return ptr2
