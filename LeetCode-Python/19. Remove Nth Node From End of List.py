# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        ptr1 = head
        ptr2 = head
        pptr1 = None

        i = 0
        while i < n:
            ptr2 = ptr2.next
            i += 1

        while ptr2 != None:
            pptr1 = ptr1
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        if pptr1 != None:
            pptr1.next = ptr1.next
        else:
            head = ptr1.next

        return head




