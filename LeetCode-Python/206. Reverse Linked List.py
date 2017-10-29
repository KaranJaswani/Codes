# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        parent = None
        if head != None:
            child = head.next
        else:
            return head

        while head != None:
            head.next = parent
            parent = head
            head = child
            if child != None:
                child = child.next

        return parent