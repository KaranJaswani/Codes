# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        ptr = head
        pptr = None

        while ptr != None:
            if ptr.val == val:
                if pptr != None:
                    pptr.next = ptr.next
                    ptr = ptr.next
                else:
                    ptr = ptr.next
                    head = ptr
            else:
                pptr = ptr
                ptr = ptr.next


        return head